from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbfdyQqq8mTQ-VOF4pVKUCyFE5c2uReiyr6Edz8IYLNwAmrlH6zeS7xGgNf8_hqDS3EBQ&usqp=CAU"

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
    

class Pet(db.Model):
    """Pet"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """Return image for pet using input or default"""

        return self.photo_url or DEFAULT_IMG