from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db = SQLAlchemy(app)

# Import views after app is created to avoid circular imports
from . import views
