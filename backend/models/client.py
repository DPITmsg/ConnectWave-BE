from backend.config import db
from backend.models.user import User
from authlib.integrations.sqla_oauth2 import OAuth2ClientMixin


class Client(db.Model, OAuth2ClientMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), db.ForeignKey('user.username', ondelete='CASCADE'))
    user = db.Relationship('User')
