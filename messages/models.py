from databases.conf_db import db, BaseDBModel
from datetime import datetime

class MessageModel(db.Model, BaseDBModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(120), nullable=False)
    message = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Message "{self.subject}">'
