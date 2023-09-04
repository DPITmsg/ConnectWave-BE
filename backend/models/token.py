from authlib.integrations.sqla_oauth2 import OAuth2TokenMixin
from backend.config import db
from backend.models.user import User


class Token(db.Model, OAuth2TokenMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(
        db.String(), db.ForeignKey('user.username', ondelete='CASCADE')
    )
    user = db.relationship('User')
