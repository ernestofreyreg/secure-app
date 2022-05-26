from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=False, nullable=True)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    games = db.relationship("SoccerGame")

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')

    def __repr__(self):
        return f"<Account {self.id}>"
    
    def serialize(self):
        return {
            'id': self.id,
            'total': self.total
        }


class SoccerGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey("user.id"))
    game_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<SoccerGame {}".format(self.id)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user.id,
            "game_time": self.game_time
        }
