from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    id = IntegerField('id')
    nombre = StringField('nombre')
    apellidos = StringField('apellidos')
    email = EmailField('email')

class MaestroForm(UserForm):
    id = IntegerField('id')
    nombre = StringField('nombre')
    apellidos = StringField('apellidos')
    email = EmailField('email')
    materia = StringField('materia')
    
