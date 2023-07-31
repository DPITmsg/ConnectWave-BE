from backend import app, db

app.app_context().push()


class Activity(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=50), nullable=False)
    description = db.Column(db.String(length=1000))
    number_of_participants = db.Column(db.Integer(), nullable=False, default=0)
    location = db.Column(db.String(length=50), nullable=False)
