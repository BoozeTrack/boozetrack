import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# Initialize our application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('HEROKU_POSTGRESQL_JADE_URL')
db = SQLAlchemy(app)

# Import views.  Make sure this is the LAST line in the file
import booze.views
