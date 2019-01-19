import token_fetcher
import requests
import json
import pyperclip

URL_USERS = "https://jscpeterson.com/rest/users"
URL_LOCATIONS = "https://jscpeterson.com/rest/film_locations"
URL_PRODUCTIONS = "https://jscpeterson.com/rest/productions"
URL_COMMENTS = "https://jscpeterson.com/rest/user_comments"
URL_IMAGES = "https://jscpeterson.com/rest/images"

token = ""

def getToken():
    token = "Bearer " + token_fetcher.fetch()
    return token
    
def printToken(token):
    print "\n***YOUR TOKEN IS***\n" + token

def getJson(url, token):
    headers = {'authorization': token}
    response = requests.get(url, headers=headers)
    result = json.loads(response.text)
    return result

def printJson(url, token):
    print(json.dumps(getJson(url, token), indent=4))
    
def printLocation(locations, index):
    location = locations[index]
    print "Location Name: %s" % location["siteName"]
    print "Submitted by: %s" % location["userName"]
    print "Production: %s" % location["production"]["title"]
    print "Approved: %s" % location["approved"]
    
def printProduction(productions, index):
    production = productions[index]
    print "Title: %s" % production["title"]
    print "Type: %s" % production["type"]
    print "Released: %s" % production["releaseYear"]
    print "Plot: %s" % production["plot"]

#Check for error codes
#{u'status': 404, u'timestamp': u'2019-01-19T05:46:41.788+0000', u'message': u'No message available', u'path': u'/rest/film_productions', u'error': u'Not Found'}

"""
def test():
    token = getToken()
    getJson(URL_LOCATIONS, pyperclip.paste())
    getJson(URL_PRODUCTIONS, pyperclip.paste())
    getJson(URL_COMMENTS, pyperclip.paste())
    getJson(URL_IMAGES, pyperclip.paste())
    printJson(URL_USERS, pyperclip.paste())
"""  
    
token = getToken()
pyperclip.copy(token) # Saves the token to the clipboard.
printToken(token)

print 'Done'
