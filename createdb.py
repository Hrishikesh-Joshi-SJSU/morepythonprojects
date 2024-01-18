# ----------------------------------------------------------------------
# Name:        createdb
# Purpose:     Create sqlite DB to be used with flaskappdb
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Create sqlite database to be used with the flaskappdb module

The database cs122.db is created in the instance directory.
It contains the review table corresponding to the Review class
defined in the flaskappdb module.
"""
from flaskappdb import app
from flaskappdb import db


def main():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    main()
