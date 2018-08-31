from devAppOne import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html', title="Home")
@app.route('/tour/')
def tour():
    return render_template('tour.html', title="Tour")
