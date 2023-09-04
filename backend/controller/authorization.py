from flask import request, render_template
from flask_login import current_user
from backend.login.server import server
from backend.config import app


def describe_scope(scope):
    pass


@app.route('/oauth/authorize', methods=['GET', 'POST'])
def authorize():

    if request.method == 'GET':
        grant = server.get_consent_grant(end_user=current_user)
        client = grant.client
        scope = client.get_allowed_scope(grant.request.scope)

        # You may add a function to extract scope into a list of scopes
        # with rich information, e.g.
        scopes = describe_scope(scope)  # returns [{'key': 'email', 'icon': '...'}]
        return render_template(
            'authorize.html',
            grant=grant,
            user=current_user,
            client=client,
            scopes=scopes,
        )
    confirmed = request.form['confirm']
    if confirmed:
        return server.create_authorization_response(grant_user=current_user)
    return server.create_authorization_response(grant_user=None)
