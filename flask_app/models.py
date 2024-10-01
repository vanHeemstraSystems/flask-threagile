from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    ## Stage 1: Plain Text
    #

    ## Stage 2: Encryption
    #
  
    ## Stage 3: Hashing
    #
  
    ## Stage 4: Hashing and Salting
    #
  
    ## Stage 5: BCrypt  
    password_hash = db.Column(db.String(128), nullable=False) # Store hashed password

def __repr__(self):
return f'<User {self.username}>'
