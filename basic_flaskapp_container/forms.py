from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length

class SignupForm(FlaskForm):
	name = StringField('User name', validators=[DataRequired(), Length(min=3, max=50, message="Nombre Incorrecto")])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=30, message="Contraseña Invalida")])
	apellidos = StringField('Apellidos', validators=[DataRequired(), Length(min=3, max=50, message="Apellido invalido")])
	biografia = StringField('Biografia', validators=[DataRequired(), Length(min=3, max=50, message="Invalido")])
	correo = StringField('Correo', validators=[DataRequired(), Length(min=3, max=50, message="Correo invalido")])
	telefono = StringField('Telefono', validators=[DataRequired(), Length(min=10, max=10, message="Telefono Incorrecto ")])


class LoginForm(FlaskForm):
	name = StringField('User name', validators=[DataRequired(), Length(min=3, max=50, message="Nombre Incorrecto")])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=30, message="Contraseña Invalida")])

class ComentarioForm(FlaskForm):
	comentario = TextAreaField('Comentario', validators=[Length(min=10, max=50)])
