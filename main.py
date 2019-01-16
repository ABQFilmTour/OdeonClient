import token_fetcher
import requests

token = "Bearer " + token_fetcher.fetch()
print "\n***YOUR TOKEN IS***\n" + token

url = 'https://jscpeterson.com/rest/film_locations'
headers = {'authorization': token}

r = requests.get(url, headers=headers)

print r.text
