# import the Flask library
from flask import Flask, render_template

# Create the Flask instance and pass the Flask
app = Flask(__name__)

# Pg
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/display')
def display():
    return render_template('display.html')


# Start with flask web app, with debug as True,# only if this is the starting page
if (__name__ == "__main__"):
    app.run(debug=True)
