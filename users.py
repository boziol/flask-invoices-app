from flask import Flask, request, jsonify, render_template, session, redirect, url_for
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
import re
from decorators.auth_required import auth_required
from bson import ObjectId
import requests

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/invoices'
app.config['SECRET_KEY'] = 'abcd4321'

mongo = PyMongo(app)
db = mongo.db

@app.route('/register', methods = ['GET','POST'])

def register():
    data = request.form
    email = data['email']
    password = data['password']
    firstname = data['firstname']

    if not re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
        return jsonify({
            'message':'Hasło musi składać się z minimum 8 znaków itp... bla bla'
        })


    existing_user = db.users.find_one({'email': email})

    

    if existing_user is None:

        hashed_password = generate_password_hash(password)
        new_data = {
            'email':email,
            'password':hashed_password,
            'firstname':firstname
        }
        user = db.users.insert_one(new_data)
        session['user_id'] = str(user.inserted_id)
        return redirect(url_for('dashboard'))
    
    else:
        error = "Uzupełnij wszystkie pola"
        return render_template('register.html', error=error)

@app.route("/login", methods = ['POST'])
def login():
    if request.method == "POST":
        data = request.form
        email = data['email']
        password = data['password']
        user = db['users'].find_one({'email':email})

        if user and check_password_hash(user['password'], password):
            session['user_id'] = str(user['_id'])
            return redirect(url_for('dashboard'))

        else:
            error = 'Podano błędne hasło lub email'
            return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('user_id')
    return jsonify({
        'message':'Pomyslnie wylogowano'
    })




@app.route("/show-all")

@auth_required

def show_all():

    

        data = list(mongo.db['users'].find({},{'password':0}))
        all_users = mongo.db['users'].count_documents({})

        for item in data:
            item['_id'] = str(item['_id'])


        return jsonify({
        'data': data,
        'message': f'Pobrano listę wszystkich użytkowników {all_users}'
        })

@app.route('/user-details/<id>')
def user_details(id):
    user = db['users'].find_one({'_id': ObjectId(id)})
    user['_id'] = str(user['_id'])
    return jsonify({
          'data': user,
          'message':'Informacje o użytkowniku'
     })



@app.route("/whoami")
@auth_required
def whoami():
     user = db['users'].find_one({'_id': ObjectId(session['user_id'])})
     user['_id'] = str(user['_id'])
     return jsonify({
          'data': user,
          'message':'Informacje o użytkowniku'
     })

#Views


@app.route("/")
@auth_required
def dashboard():
     id = session["user_id"]
     user = requests.get(f"http://127.0.0.1:5000/user-details/{id}").json()
     print(user)
     return render_template("index.html", user=user)

@app.route('/zaloguj sie', methods= ['GET','POST']) 
def login_page():
    return render_template('login.html')

@app.route('/zarejestruj sie', methods= ['GET','POST']) 
def register_page():
    return render_template('register.html')