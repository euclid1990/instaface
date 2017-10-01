from flask import jsonify

# Implement when no JWT is received callback
def jwt_unauthorized_loader(err):
    return jsonify({'success': False, 'message': "Missing authorization header"}), 400

# Implement invalid JWT is received callback
def jwt_invalid_token_loader(err):
    return jsonify({'success': False, 'message': "Invalid access token"}), 400

# Implement invalid JWT callback
def jwt_expired_token_loader():
    return jsonify({'success': False, 'message': "Access token has expired"}), 400

# Implement a blacklisted token attempt to access a protected endpoint callback
def jwt_revoked_token_loader():
    return jsonify({'success': False, 'message': "Access token has been blacklisted"}), 400

def jwt_token_in_blacklist_loader(UserAccessToken, decoded_token):
    return UserAccessToken.is_token_blacklisted(decoded_token)
