from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField , EmailField
from wtforms.validators import InputRequired , Length , Email, Regexp


class RegisterForm(FlaskForm):
    firstname =StringField('Imię', validators=[
        InputRequired("Imię jest wymagane"),
        Length(min=2)

    ])
    
    email = EmailField('Adres email', validators=[
        InputRequired('Email jest wymagany'),
        Email('Podaj poprawny adres email')
    ])

    password = PasswordField('Hasło', validators=[
        InputRequired('Hasło jest wymagane'),
        Regexp('[A-Za-z0-9@#$%^&+=]{8,}', flags=0, message="Hasło musi składać z ....")
        

    ])
    
    submit = SubmitField('Rejestracja')