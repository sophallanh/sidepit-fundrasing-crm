from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from database import db
import os
from models import User

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ub3v20dpnenaat:p335bec966948c2cf84db0188da153800e2566432279821fff2a297032a190a6b@cbbirn8v9855bl.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d4ckpnjivt6h34'
app.config['SECRET_KEY'] = b'\xae\x81\xc1w\xe7\xb8\x07\x17\x97\xa1\x01\x93\xda\xbc)\xef,H\x00\x8aV\x0b\xe0\xba'

# Initialize database and login manager
db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

# User loader function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create Flask app
def create_app():
    with app.app_context():
        db.create_all()

    return app

# Routes
@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('home'))

        flash('Invalid username or password')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == "__main__": 
    app = create_app()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
