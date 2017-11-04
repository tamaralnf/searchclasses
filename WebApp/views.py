from flask import render_template, flash, redirect
from .forms import Specifications
from . import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/coursesearch', methods=['GET', 'POST'])
def CoursesForm():
    form = Specifications()
    if form.validate_on_submit():
        flash()
    return render_template('form.html', title='Course Search', form=form)
