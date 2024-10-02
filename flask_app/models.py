#!/usr/bin/env python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Stage 1: Plain Text
     password = db.Column(db.String(128), nullable=False)  # Store password in plain text
    # End Stage 1

    ## Stage 2: Encryption
    # password = db.Column(db.LargeBinary, nullable=False)  # Store encrypted password
    ## End Stage 2
  
    ## Stage 3: Hashing
    # password = db.Column(db.String(64), nullable=False)  # Store hashed password
    ## End Stage 3
  
    ## Stage 4: Hashing and Salting
    # password_hash = db.Column(db.String(128), nullable=False)  # Store hashed and salted password
    ## End Stage 4
  
    ## Stage 5: BCrypt  
    # password_hash = db.Column(db.String(128), nullable=False) # Store hashed password with bcrypt
    ## End Stage 5

def __repr__(self):
return f'<User {self.username}>'
