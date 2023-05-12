from flask import Flask,render_template,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import (StringField,BooleanField,DateTimeField,RadioField,
                     SelectField,TextAreaField,SubmitField)
from wtforms.validators import DataRequired


app = Flask(__name__)

app.config['SECRET_KEY']='mykey'

class InfoForm(FlaskForm):
    country = StringField('Which country you are from ?' , validators=[DataRequired()])
    cricket = BooleanField('Do you like cricket?')
    team = RadioField('Please choose your fav ipl team',choices=[(1,'MI'),(2,'CSK'),(3,'GT')])
    player = SelectField('Please pick your fav player',choices=[(1,'Dhoni'),(2,'Virat Kohli'),(3,'Rohit Sharma')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')

@app.route('/',methods= ['GET','POST'])
def index():

    form = InfoForm()
    if form.validate_on_submit():
        session['country']=form.country.data
        session['cricket']=form.cricket.data
        session['team']=form.team.data 
        session['player']=form.player.data
        session['feedback']=form.feedback.data

        return redirect(url_for('thankyou'))
    return render_template('indexpage.html',form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html') 

if __name__ == '__main__' :
    app.run(debug=True)     