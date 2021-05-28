from flask import Flask , render_template, request
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, IntegerField

from formularium import growth

app = Flask(__name__)
app.config['SECRET_KEY']='dAnIel52'

@app.route('/', methods=['GET', 'POST'])
def home():

    form = growth()
    a=1
    r = 0.99
    years = 365
    xn = a * (r ** years)


    return render_template('home.html', output=xn, form=form)




"""     Here the app runs       and lives       not to touch        leave alone     logic above
"""

if __name__=='__main__':
    app.run(port=5500, host='0.0.0.0', debug=True)
