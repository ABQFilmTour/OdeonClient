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

"""
A film location, assumed to have an existing entry in the database.
"""
class FilmLocation:

    locationId = ""
    siteName = ""
    userName = ""
    productionTitle = ""
    approved = False
    latCoordinate = 0
    longCoordinate = 0

    def __init__(self, json):
        self.json = json
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
    
    """
    def print():
        print "Location Name: %s" % location["siteName"]
        print "Submitted by: %s" % location["userName"]
        print "Production: %s" % location["production"]["title"]
        print "Approved: %s" % location["approved"]    
    """

    def getId(self):
        return self.locationId
        
    def delete(self, token):
        headers = {'authorization': token}
        url = "%s/%s" % (URL_LOCATIONS, self.json['id'])
        response = requests.delete(url, headers=headers)
        return response

    def approve(self, token):
        headers = {'authorization': token}
        self.json['approved'] = True
        response = requests.patch(URL_LOCATIONS, headers=headers, json=self.json)
        return response

class UserComment:
    def __init__(self, json):
        self.json = json
        
    def __str__(self):
        return "\
Comment: %s \n\
Submitted by: %s \n\
Approved: %s "\
% (self.json['text'], self.json['userName'], self.json['approved'])

    """
    def print(self):
        print "Author: %s" % self.json['userName']
        print "\"%s\"" % self.json['text']
        print "Approved: %s" % self.json['approved']
    """

    def delete(self, token):
        headers = {'authorization': token}
        url = "%s/%s" % (URL_COMMENTS, self.json['id'])
        response = requests.delete(url, headers=headers)
        return response

    def approve(self, token):
        headers = {'authorization': token}
        self.json['approved'] = True
        response = requests.patch(URL_COMMENTS, headers=headers, json=self.json)
        return response

class UserImage:
    def __init__(self, json):
        self.json = json

    def __str__(self):
        return "\
Image URL: %s\n\
Submitted by: %s\n\
Approved: %s"\
% (self.json['url'], self.json['userName'], self.json['approved'])

    def delete(self, token):
        headers = {'authorization': token}
        url = "%s/%s" % (URL_IMAGES, self.json['id'])
        response = requests.delete(url, headers=headers)
        return response

    def approve(self, token):
        headers = {'authorization': token}
        self.json['approved'] = True
        response = requests.patch(URL_IMAGES, headers=headers, json=self.json)
        return response

def getToken():
    token = "Bearer " + token_fetcher.fetch()
    return token
    
def printToken(token):
    print "\n***YOUR TOKEN IS***\n" + token

"""
Retrieves a list of the JSON data from a URL on the server.
"""
def getJsonFromServer(url, token):
    headers = {'authorization': token}
    response = requests.get(url, headers=headers)
    result = json.loads(response.text)
    return result    

"""
Prints formatted JSON data from a URL
"""
def printJson(url, token):
    print(json.dumps(getJson(url, token), indent=4))  

def printProduction(production):
    print "Title: %s" % production["title"]
    print "Type: %s" % production["type"]
    print "Released: %s" % production["releaseYear"]
    print "Plot: %s" % production["plot"]

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

locations = getJsonFromServer(URL_LOCATIONS, token)
lastLoc = FilmLocation(locations[0])
print "\nLast Location:"
print lastLoc

comments = getJsonFromServer(URL_COMMENTS, token)
lastCom = UserComment(comments[0])
print "\nLast Comment:"
print lastCom

images = getJsonFromServer(URL_IMAGES, token)
lastImage = UserImage(images[0])
print "\nLast Image:"
print lastImage
