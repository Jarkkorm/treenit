from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, validators, SubmitField, SelectField, IntegerField

class RegistrationForm(FlaskForm):
  username = StringField("Nimi", [validators.DataRequired(), validators.Length(min=4, max=25)])
  password = PasswordField("Salasana", [validators.DataRequired(), validators.Length(min=4, max=25)])
  submit = SubmitField("Luo tunnus")

class LoginForm(FlaskForm):
  username = StringField("Nimi", [validators.DataRequired(), validators.Length(min=4, max=25)])
  password = PasswordField("Salasana", [validators.DataRequired(), validators.Length(min=4, max=25)])
  submit = SubmitField("Kirjaudu")

class AddRoutineForm(FlaskForm):
  sets = IntegerField("Kierroksia", [validators.InputRequired(), validators.NumberRange(0,1000)])
  reps = IntegerField("Toistoja", [validators.InputRequired(), validators.NumberRange(0,1000)])
  quantity = StringField("Painot/aika", [validators.DataRequired(), validators.Length(min=2, max=25)])
  exercise = SelectField("Liike", coerce=int)
  submit = SubmitField("Tallenna")

class AddExerciseForm(FlaskForm):
  name = StringField("Treenin nimi", [validators.DataRequired(), validators.Length(min=4, max=25)])
  description = StringField("Treenin kuvaus", [validators.DataRequired(), validators.Length(min=4, max=25)])
  submit = SubmitField("Tallenna")

class AddPlanForm(FlaskForm):
  name = StringField("Suunnitelman nimi", [validators.DataRequired(), validators.Length(min=4, max=25)])
  duration = StringField("Pituus", [validators.DataRequired(), validators.Length(min=4, max=25)])
  submit = SubmitField("Tallenna")

class AddToHistoryForm(FlaskForm):
  submit = SubmitField("Merkitse tehdyksi")