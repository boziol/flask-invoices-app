from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField , EmailField, IntegerField, FloatField, SelectField, SubmitField
from wtforms.validators import InputRequired , Length , Email, Regexp, DataRequired


class InvoiceForm(FlaskForm):
    invoice_number =StringField('Numer faktury', validators=[
        DataRequired("Numer jest wymagany"),
        Length(min=5)
    ])

    buyer_name = StringField('Nazwa nabywcy', validators=[
        DataRequired("Nazwa nabywcy jest wymagana"),       
    ])

    buyer_nip =StringField('Numer NIP', validators=[
        DataRequired("Numer NIP jest wymagany"),
        Regexp('^[0-9]*$', flags=0, message="NIP musi składać się z cyfr"),
        Length(min=10, max=10, message='Numer NIP musi składać się z 10 liczb'),
    ])

    item_name =StringField('Nazwa towaru', validators=[
        DataRequired("Nazwa towaru jest wymagana"),
        Length(min=2)
    ])
    item_quantity =IntegerField('Ilość towaru', validators=[
        DataRequired("Musisz podać ilość"),
    ])
    item_price =FloatField('Cena towaru', validators=[
        DataRequired("Musisz podać cenę"),
    ])
    tax_value = SelectField('Podatek', choices=[
        (0,'ZW'),
        (9,'9%'),
        (12,"12%"),
        (23,"23%")
    ], validators=[
        DataRequired('Musisz wybrać podatek'),
    
    ])
    submit = SubmitField('Zarejestruj')
        
        
