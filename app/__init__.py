import os
from flask import Flask

app = Flask(__name__)

# Set the environment from an environment variable, default to 'development'
env = os.getenv('FLASK_ENV', 'development')
app.config['ENV'] = env

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

from app import views