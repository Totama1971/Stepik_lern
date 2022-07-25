from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms  import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
app=Flask(__name__)

class MessageForm(FlaskForm):
	name = StringField('Name:', validators=[DataRequired()])
	email = StringField('Email:', validators=[Email()])
	message = TextAreaField('Message:', validators=[DataRequired()])
	submit = SubmitField('Submit')

@app.route('/')
def index():
	return render_template('index.html',numbers=[1,10,100])

