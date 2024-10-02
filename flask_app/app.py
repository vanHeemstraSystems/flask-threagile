#!/usr/bin/env python
import bcrypt # Used for bcrypt
import hashlib # Used for hashing and salting
import subprocess
from cryptography.fernet import Fernet # Used for encryption
from flask import Flask, request, jsonify, render_template, redirect, url_for 
from models import db, User

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

def run_threagile():
    """Run Threagile analysis and generate a report."""
    command = ['threagile', 'analyze', './flask_app', '--config', 'threagile_config.yaml']     
    #subprocess.run(command)

with app.app_context():
    # your code here to do things before first request
    run_threagile()

db.init_app(app)

# # Stage 2: Encryption
# key = Fernet.generate_key() # Generate a key for encryption and decryption
# cipher_suite = Fernet(key)
# # End Stage 2

with app.app_context():
   db.create_all()

@app.route('/') 
def home():
    return render_template('home.html')

# # Stage 3: Hashing
# def hash_password(password):
#   """Hash a password using SHA-256."""
#   return hashlib.sha256(password.encode()).hexdigest()
# # End Stage 3

# Stage 4: Hashing and Salting
def hash_password(password, salt):
  """Hash a password with a salt using SHA-256."""
  return hashlib.sha256((salt + password).encode()).hexdigest()
# End Stage 4

@app.route('/add_user', methods=['GET', 'POST']) 
def add_user():
    if request.method == 'POST':
        data = request.form
        
        # # Stage 1: Plain Text
        # new_user = User(username=data['username'], email=data['email'], password=data['password'])  # Store password in plain text
        # # End Stage 1
       
        # # Stage 2: Encryption
        # encrypted_password = cipher_suite.encrypt(data['password'].encode())  # Encrypt the password
        # new_user = User(username=data['username'], email=data['email'], password=encrypted_password)
        # # End Stage 2
        
        # # Stage 3: Hashing
        # hashed_password = hash_password(data['password'])  # Hash the password
        # new_user = User(username=data['username'], email=data['email'], password=hashed_password)
        # # End Stage 3

        # Stage 4: Hashing and Salting
        salt = os.urandom(16).hex()  # Generate a random salt
        hashed_password = hash_password(data['password'], salt)  # Hash the password with the salt
        new_user = User(username=data['username'], email=data['email'], password=hashed_password + ':' + salt)  # Store hash and salt
        # End Stage 4
        
        # # Stage 5: Bcrypt
        # hashed_password = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt()) # Hash the password
        # new_user = User(username=data['username'], email=data['email'], password=hashed_password.decode()) # Store hashed bcrypt password
        # # End Stage 5
        
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('add_user'))
    return render_template('add_user.html')

@app.route('/login', methods=['GET', 'POST']) 
def login_user():
    if request.method == 'POST':
        data = request.form
        user = User.query.filter_by(username=data['username']).first()
        
        # # Stage 1: Plain Text
        # if user and user.password == data['password']:  # Compare passwords in plain text
        #     return jsonify({'message': 'Login successful'}), 200
        # # End Stage 1
            
        # # Stage 2: Encryption
        # if user:
        #    decrypted_password = cipher_suite.decrypt(user.password).decode()  # Decrypt the stored password
        #    if decrypted_password == data['password']:  # Compare decrypted passwords
        #        return jsonify({'message': 'Login successful'}), 200
        # # End Stage 2
       
        # # Stage 3: Hashing
        # if user and user.password == hash_password(data['password']):  # Compare hashed passwords
        #    return jsonify({'message': 'Login successful'}), 200
        # # End Stage 3

        # Stage 4: Hashing and Salting
        if user:
           password_hash, salt = user.password_hash.split(':')  # Split stored hash and salt
           if password_hash == hash_password(data['password'], salt):  # Compare hashed passwords
               return jsonify({'message': 'Login successful'}), 200
        # End Stage 4
   
        # # Stage 5: Bcrypt
        # if user and bcrypt.checkpw(data['password'].encode(), user.password_hash.encode()): # Verify password in bcrypt
        #    return jsonify({'message': 'Login successful'}), 200
        # # End Stage 5
            
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
