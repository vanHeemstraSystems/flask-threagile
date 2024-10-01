#!/usr/bin/env python
import bcrypt # Used for bcrypt
import hashlib # Used for hashing
import subprocess
from cryptography.fernet import Fernet # Used for encryption
from flask import Flask, request, jsonify, render_template, redirect, url_for 
from models import db, User

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db.init_app(app)

## Stage 1: Plain Text
with app.app_context():
   db.create_all()

## Stage 2: Encryption
# key = Fernet.generate_key() # Generate a key for encryption and decryption
# cipher_suite = Fernet(key)
#
# with app.app_context():
#   db.create_all()

## Stage 3: Hashing

## Stage 4: Hashing and Salting

## Stage 5: Bcrypt

def run_threagile():
    """Run Threagile analysis and generate a report."""
    command = ['threagile', 'analyze', './flask_app', '--config', 'threagile_config.yaml']     
    subprocess.run(command)

@app.before_first_request 
def before_first_request():
    run_threagile()

@app.route('/') 
def home():
    return render_template('home.html')

@app.route('/add_user', methods=['GET', 'POST']) 
def add_user():
    if request.method == 'POST':
        data = request.form
        
        ## Stage 1: Plain Text
        new_user = User(username=data['username'], email=data['email'], password=data['password'])  # Store password in plain text
       
        ## Stage 2: Encryption
        # encrypted_password = cipher_suite.encrypt(data['password'].encode())  # Encrypt the password
        # new_user = User(username=data['username'], email=data['email'], password=encrypted_password)
        
        ## Stage 3: Hashing

        ## Stage 4: Hashing and Salting
        
        ## Stage 5: Bcrypt
        # hashed_password = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt()) # Hash the password
        # new_user = User(username=data['username'], email=data['email'], password_hash=hashed_password.decode()) # Store hashed bcrypt password  
        
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('add_user'))
    return render_template('add_user.html')

@app.route('/login', methods=['GET', 'POST']) 
def login_user():
    if request.method == 'POST':
        data = request.form
        user = User.query.filter_by(username=data['username']).first()
        
        ## Stage 1: Plain Text
        if user and user.password == data['password']:  # Verify password in plain text
            return jsonify({'message': 'Login successful'}), 200
            
        ## Stage 2: Encryption
        # if user:
        #    decrypted_password = cipher_suite.decrypt(user.password).decode()  # Decrypt the stored password
        #    if decrypted_password == data['password']:
        #        return jsonify({'message': 'Login successful'}), 200
       
        ## Stage 3: Hashing

        ## Stage 4: Hashing and Salting
        
        ## Stage 5: Bcrypt
        # if user and bcrypt.checkpw(data['password'].encode(), user.password_hash.encode()): # Verify password in bcrypt
        #    return jsonify({'message': 'Login successful'}), 200
            
        return jsonify({'message': 'Invalid credentials'}), 401 
    return render_template('login.html')

@app.route('/delete_user', methods=['GET', 'POST']) 
def delete_user():
    if request.method == 'POST':
        data = request.form
        user = User.query.filter_by(username=data['username']).first() 
        if user:
            db.session.delete(user) 
            db.session.commit()
            return redirect(url_for('delete_user'))
    return render_template('delete_user.html')

@app.route('/users', methods=['GET']) 
def get_users():
    users = User.query.all()
    return render_template('users.html', users=users)

if __name__ == '__main__': 
    app.run(debug=True)
