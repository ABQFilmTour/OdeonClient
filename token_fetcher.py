profile = "https://www.googleapis.com/auth/userinfo.profile"
email = "https://www.googleapis.com/auth/userinfo.email"
openid = "https://www.googleapis.com/auth/plus.me"
from google_auth_oauthlib.flow import InstalledAppFlow
flow = InstalledAppFlow.from_client_secrets_file("client_secret_web.json", scopes = [profile, email, openid])
credentials = flow.run_local_server(host = "localhost", port = 8080, open_browser = True)
print "\n***YOUR TOKEN IS***"
print "Bearer " + credentials.id_token
