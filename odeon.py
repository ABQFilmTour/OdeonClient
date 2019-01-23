import token_fetcher
import requests
import json
import pyperclip

URL_USERS = "https://jscpeterson.com/rest/users"
URL_LOCATIONS = "https://jscpeterson.com/rest/film_locations"
URL_PRODUCTIONS = "https://jscpeterson.com/rest/productions"
URL_COMMENTS = "https://jscpeterson.com/rest/user_comments"
URL_IMAGES = "https://jscpeterson.com/rest/images"

PATH_LOCATIONS = "data/locations.json"
PATH_PRODUCTIONS = "data/productions.json"
PATH_COMMENTS = "data/comments.json"
PATH_IMAGES = "data/images.json"

token = ""

class FilmLocation:

    locationId = ""
    siteName = ""
    userName = ""
    productionTitle = ""
    approved = False
    latCoordinate = 0
    longCoordinate = 0

    def __init__(self, json):
        self.locationId = json['id']
        self.siteName = json['siteName']
        self.userName = json['userName']
        self.latCoordinate = json['latCoordinate']
        self.longCoordinate = json['longCoordinate']
        self.productionTitle = json['production']['title']
        self.approved = json['approved']

    def __str__(self):
        return "\
Site Name: %s \n\
Coordinates: %f, %f \n\
Submitted by: %s \n\
Production: %s \n\
Approved: %s "\
% (self.siteName, self.latCoordinate, self.longCoordinate, self.userName, self.productionTitle, self.approved)
    
    def printLocation(location):
        print "Location Name: %s" % location["siteName"]
        print "Submitted by: %s" % location["userName"]
        print "Production: %s" % location["production"]["title"]
        print "Approved: %s" % location["approved"]    

    def getId(self):
        return self.locationId

def getToken():
    token = "Bearer " + token_fetcher.fetch()
    return token
    
def printToken(token):
    print "\n***YOUR TOKEN IS***\n" + token

def getJsonFromServer(url, token):
    headers = {'authorization': token}
    response = requests.get(url, headers=headers)
    result = json.loads(response.text)
    return result

def printJson(url, token):
    print(json.dumps(getJson(url, token), indent=4))  

def deleteLocation(location, token):
    headers = {'authorization': token}
    url = "%s/%s" % (URL_LOCATIONS, location.getId())
    response = requests.delete(url, headers=headers)
    return response

def approveLocation(location, token):
    headers = {'authorization': token}
    location['approved'] = True
    response = requests.patch(URL_LOCATIONS, headers=headers, json=location)
    return response

def printProduction(production):
    print "Title: %s" % production["title"]
    print "Type: %s" % production["type"]
    print "Released: %s" % production["releaseYear"]
    print "Plot: %s" % production["plot"]

def printComment(comment):
    print "Author: %s" % comment['userName']
    print "\"%s\"" % comment['text']
    print "Approved: %s" % comment['approved']

def printImage(images, index):
    #TODO Print an individual image reference
    return

def writeDataToFile(path, url, token):
    locationsFile = open(path, 'w+')
    locationsFile.write(json.dumps(getJsonFromServer(url, token), indent = 4))
    locationsFile.close()
    
def saveDatabase(token):
    print "Writing location data locally..."
    writeDataToFile(PATH_LOCATIONS, URL_LOCATIONS, token)
    print "Done\nWriting production data locally..."
    writeDataToFile(PATH_PRODUCTIONS, URL_PRODUCTIONS, token)
    print "Done\nWriting comment data locally..."
    writeDataToFile(PATH_COMMENTS, URL_COMMENTS, token)
    print "Done\nWriting image data locally..."
    writeDataToFile(PATH_IMAGES, URL_IMAGES, token)
    print "Done"

def getApprovalStats(submissionList):
    approved = 0
    unapproved = 0
    for submission in submissionList:
        if submission['approved']:
            approved += 1
        else:
            unapproved += 1
    returnMessage = "%i submissions have been approved. " % (approved)
    if unapproved > 0:
        returnMessage += "%i submissions are still awaiting approval." % (unapproved)
    else:
        returnMessage += "No new submissions await approval."
    return returnMessage

#Check for error codes
#{u'status': 404, u'timestamp': u'2019-01-19T05:46:41.788+0000', u'message': u'No message available', u'path': u'/rest/film_productions', u'error': u'Not Found'}
    
token = getToken()
pyperclip.copy(token) # Saves the token to the clipboard.
printToken(token)
