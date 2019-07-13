from google_auth_oauthlib.flow import InstalledAppFlow

def fetch():
    profile = "https://www.googleapis.com/auth/userinfo.profile"
    email = "https://www.googleapis.com/auth/userinfo.email"
    openid = "https://www.googleapis.com/plus/v1/people/me"
    try:
        flow = InstalledAppFlow.from_client_secrets_file("client_secret_web.json", scopes = ["openid", email, profile])
    except IOError:
        clientSecretNotFound()
        return    
    credentials = flow.run_local_server(host = "localhost", port = 8080, open_browser = True)
    return credentials.id_token
    
def clientSecretNotFound():
    clientIdUrl = "https://console.developers.google.com/apis/credentials?authuser=2&project=smart-athlete-221016"
    print "Client secret file not found.\nTo authenticate this service you will need to download a client ID JSON file from the Google APIs dashboard.\nNavigate to %s\nClick Download button next to \"Web client (Auto-created for Google Sign-in)\" and download the file to this folder as \"client_secret_web.json\".\nIf you do not have access and want access, contact abqfilmtour@gmail.com." % (clientIdUrl)

#handle file missing error
    
#socket.error: [Errno 98] Address already in use
#   occurs if a request was opened but not closed - requires a restart, should be handled
