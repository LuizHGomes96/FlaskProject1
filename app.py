from flask import Flask, render_template, flash
from flask_wtf import FlaskForm # type: ignore
from wtforms import StringField, SubmitField # type: ignore
from wtforms.validators import DataRequired # type: ignore
 
app=Flask(__name__)
app.config['SECRET_KEY'] = "tapauer"

# Create a Form Class
class NamesForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


# ROUTES

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about(): 
    return render_template("about.html")

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", username=name)

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamesForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successfully!")
    return render_template("name.html", name=name, form=form)



# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

