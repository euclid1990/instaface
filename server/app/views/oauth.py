from flask import Blueprint, request, redirect, session, url_for
from flask.json import jsonify
import app.common.github as github
import app.common.chatwork as chatwork

mod = Blueprint('oauth', __name__, url_prefix='/oauth')

@mod.route('/authorize/<social>', methods=['GET'])
def authorize(social):
    socialList = {
        'github': github.authorize,
        'chatwork': chatwork.authorize
    }
    authorizeFn = socialList.get(social)
    redirect_uri = url_for('oauth.callback', social=social, _external=True)
    authorization_url, state = authorizeFn(redirect_uri=redirect_uri)
    session['oauth_state'] = state
    return redirect(authorization_url)

@mod.route('/callback/<social>', methods=['GET'])
def callback(social):
    socialList = {
        'github': github.callback,
        'chatwork': chatwork.callback
    }
    callbackFn = socialList.get(social)
    result = callbackFn(state=session['oauth_state'], authorization_response=request.url)
    return jsonify(result)
