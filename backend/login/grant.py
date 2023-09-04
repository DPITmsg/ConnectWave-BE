from backend.config import db
from backend.login.server import server
from authlib.integrations.sqla_oauth2 import OAuth2AuthorizationCodeMixin
from backend.models.user import User


class AuthorizationCode(db.Model, OAuth2AuthorizationCodeMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(
        db.String(), db.ForeignKey('user.username', ondelete='CASCADE')
    )
    user = db.relationship('User')

    from authlib.oauth2.rfc6749 import grants

    class AuthorizationCodeGrant(grants.AuthorizationCodeGrant):
        def save_authorization_code(self, code, request):
            client = request.client
            auth_code = AuthorizationCode(
                code=code,
                client_id=client.client_id,
                redirect_uri=request.redirect_uri,
                scope=request.scope,
                username=request.user.username,
            )
            db.session.add(auth_code)
            db.session.commit()
            return auth_code

        def query_authorization_code(self, code, client):
            item = AuthorizationCode.query.filter_by(
                code=code, client_id=client.client_id).first()
            if item and not item.is_expired():
                return item

        def delete_authorization_code(self, authorization_code):
            db.session.delete(authorization_code)
            db.session.commit()

        def authenticate_user(self, authorization_code):
            return User.query.get(authorization_code.user_id)

    server.register_grant(AuthorizationCodeGrant)
