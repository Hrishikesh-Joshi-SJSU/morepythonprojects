# ----------------------------------------------------------------------
# Name:        flaskapp
# Purpose:     Demonstrate web development with Flask
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Module containing a starter web application.

Download and save into your PyCharm project.
Run the program.
Point your browser to http://localhost:5000
"""
from flask import Flask, request, render_template
app = Flask(__name__)
#what is this?
# allows us to map urls to functions
@app.route('/home')
@app.route('/')
def welcome():
    return 'hello'
@app.route('/about')
def course_description():
    return render_template('home.html')
def main():
    app.run(debug=True)
    # adding debug=True does?

if __name__ == "__main__":
    main()
