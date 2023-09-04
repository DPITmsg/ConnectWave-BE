from backend.config import db, app
from backend.models.client import Client
from backend.models.token import Token
from authlib.integrations.flask_oauth2 import AuthorizationServer


def query_client(client_id):
    return Client.query.filter_by(client_id=client_id).first()


def save_token(token_data, request):
    if request.user:
        user_id = request.user.get_user_id()
    else:
        # client_credentials grant_type
        username = request.client.username
    token = Token(
        client_id=request.client.client_id,
        username=username,
        **token_data
    )
    with app.app_context():
        db.session.add(token)
        db.session.commit()


server = AuthorizationServer(
    app, query_client=query_client, save_token=save_token
)
