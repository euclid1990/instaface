from requests_oauthlib import OAuth2Session
from config import Config
import base64

def authorize(client_id=None, scopes=None, redirect_uri=None):
    authorization_base_url = "https://www.chatwork.com/packages/oauth2/login.php"
    if client_id is None:
        client_id = Config.CHATWORK.CHATWORK_CLIENT_ID
    if scopes is None:
        scopes = Config.CHATWORK.CHATWORK_SCOPE
    if Config.CHATWORK.CHATWORK_REDIRECT_URI is not None:
        redirect_uri = Config.CHATWORK.CHATWORK_REDIRECT_URI
    github = OAuth2Session(client_id=client_id, scope=scopes, redirect_uri=redirect_uri)

    authorization_url, state = github.authorization_url(authorization_base_url)
    # import pdb; pdb.set_trace();
    return authorization_url, state

def callback(client_id=None, client_secret=None, state=None, authorization_response=None):
    token_url = "https://oauth.chatwork.com/token"
    if client_id is None:
        client_id = Config.CHATWORK.CHATWORK_CLIENT_ID
    if client_secret is None:
        client_secret = Config.CHATWORK.CHATWORK_CLIENT_SECRET
    chatwork = OAuth2Session(redirect_uri=Config.CHATWORK.CHATWORK_REDIRECT_URI)
    auth = "{client_id}:{client_secret}".format(client_id=client_id, client_secret=client_secret)
    auth = base64.b64encode(bytes(auth, 'utf-8'))
    auth = auth.decode('UTF-8')
    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic {}'.format(auth)
    }
    token = chatwork.fetch_token(token_url=token_url, authorization_response=authorization_response, headers=headers)
    user = chatwork.get("https://api.chatwork.com/v2/me").json()
    result = dict(uid=user['account_id'], login=user['chatwork_id'], avatar=user['avatar_image_url'], provider='chatwork',
        access_token=token['access_token'], refresh_token=token['refresh_token'], token_type=token['token_type'], scope=','.join(token['scope']))
    return result

def request(access_token, endpoint, method='GET', data=None):
    client = OAuth2Session(token={'access_token': access_token})
    if method == 'GET':
        response = client.get(endpoint).json()
    else:
        response = client.post(endpoint, data=data).json()
    return response
