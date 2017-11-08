from requests_oauthlib import OAuth2Session
from config import Config

def authorize(client_id=None, scopes=None, redirect_uri=None):
    authorization_base_url = "https://github.com/login/oauth/authorize"
    if client_id is None:
        client_id = Config.GITHUB.GITHUB_CLIENT_ID
    if scopes is None:
        scopes = Config.GITHUB.GITHUB_SCOPE
    if Config.GITHUB.GITHUB_REDIRECT_URI is not None:
        redirect_uri = Config.GITHUB.GITHUB_REDIRECT_URI
    github = OAuth2Session(client_id=client_id, scope=scopes, redirect_uri=redirect_uri)
    authorization_url, state = github.authorization_url(authorization_base_url)
    return authorization_url, state

def callback(client_id=None, client_secret=None, state=None, authorization_response=None):
    token_url = "https://github.com/login/oauth/access_token"
    if client_id is None:
        client_id = Config.GITHUB.GITHUB_CLIENT_ID
    if client_secret is None:
        client_secret = Config.GITHUB.GITHUB_CLIENT_SECRET
    github = OAuth2Session(client_id=client_id, state=state)
    token = github.fetch_token(token_url=token_url, client_secret=client_secret, authorization_response=authorization_response)
    user = github.get("https://api.github.com/user").json()
    result = dict(uid=user['id'], login=user['login'], avatar=user['avatar_url'], provider='github',
        access_token=token['access_token'], refresh_token=token.get('refresh_token'), token_type=token['token_type'], scope=','.join(token['scope']))
    return result
