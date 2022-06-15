from application import db

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(300))
    completed = db.Column(db.Boolean, default=False)