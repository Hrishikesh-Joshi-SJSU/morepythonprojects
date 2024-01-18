# ----------------------------------------------------------------------
# Name:        flaskappdb
# Purpose:     Demonstrate web development with Flask and Alchemy
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Module containing a starter web application with database access.

Download and save into your PyCharm project.
Run the program.
Point your browser to http://localhost:5000/
"""
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cs122.db'
db = SQLAlchemy(app)
class Review(db.Model):
    """
    Class to represent and access the review table.
    Attributes:
    id (integer)
    comment (string)
    grade (string)
    """
    __tablename__ = "review"
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    grade = db.Column(db.String)
@app.route('/')
@app.route('/home')
def welcome():
    return render_template('home.html')
@app.route('/about')
def about():
    results = Review.query.all()
    results.reverse()
    return render_template('about.html', results=results)
@app.route('/review', methods=["POST", "GET"])
def review():
    if request.method == "POST":
        comment_input= request.form.get('comment')
        # we are getting and storing data from input of form
        grade_input = request.form.get('grade')
        new_review = Review(comment=comment_input, grade=grade_input)
        db.session.add(new_review)
        # creating a new instance and adding it to database.
        db.session.commit()

    return render_template('review.html')
@app.route('/more', methods=['POST', 'GET'])
def more():
    results = []
    grade = ''
    if request.method == 'POST':
        grade = request.form.get('grade')
        query = Review.query
        if grade:
            query = query.filter(Review.grade==grade)
        results = query.all()
    return render_template('more.html', results=results, grade=grade)
@ app.route('/delete', methods=['POST', 'GET'])
def delete():
    if request.method == 'POST':
        id = request.form.get('id')
        to_delete = Review.query.get('id')
        if to_delete:
            db.session.delete(to_delete)
            db.session.commit()
    return render_template('delete.html')
#def update():
    # slides
def main():
    app.run(debug=True)
if __name__ == "__main__":
    main()
