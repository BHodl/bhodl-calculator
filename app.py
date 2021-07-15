import datetime
from flask import Flask, render_template
from calc import get_hodl
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.fields.html5 import DateField, IntegerField
from wtforms.validators import DataRequired
#from flask.ext.navigation import Navigation

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hgflkjhzsldkjhfkjzhsdf'

Bootstrap(app)

#nav = Navigation(app)

#nar.Bar('left', [
#    nav.Item('Home', '/'),
#    nav.Item('Stack', 'stack'),
#    nv.Item('DCA', 'dca'),
#])

class CalcForm(FlaskForm):
    amount = IntegerField('Amount : ', validators=[DataRequired()])
    currency = SelectField('Currency : ', choices=['cad','usd','jpy','aud'], validators=[DataRequired()])
    date = DateField('Date : ', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CalcForm()
    amount = int(1000)
    currency = 'cad'
    date = datetime.datetime.strptime('01-01-2015', '%d-%m-%Y')
    data = [currency, date, amount]
    response = get_hodl(data)
    month = date.strftime("%B")
    if form.is_submitted():
        amount = form.amount.data
        currency = form.currency.data
        date = form.date.data
        data = [currency, date, amount]
        response = get_hodl(data)
        month = date.strftime("%B")
    date = "{} {} {}".format(date.day, month, date.year)
    return render_template('index.html', form=form, amount=amount, currency=currency, date=date, response=response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
