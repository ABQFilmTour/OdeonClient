import token_fetcher
import requests
import json
import pyperclip

URL_USERS = "https://jscpeterson.com/rest/users"
URL_LOCATIONS = "https://jscpeterson.com/rest/film_locations"
URL_PRODUCTIONS = "https://jscpeterson.com/rest/film_productions"
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
