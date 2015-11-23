# -*- coding: utf-8 -*-

from flask import Flask
from mongoengine import connect
import config


app = Flask(__name__)
app.config.from_object(config)


def register_blueprint(_app):
    #Prevents circular imports
    from price_interface.uploads import upload
    from price_interface.updates import update
    from price_interface.downloads import download
    #from views import admin
    _app.register_blueprint(upload)
    _app.register_blueprint(update)
    _app.register_blueprint(download)

register_blueprint(app)
connect(app.config.get("DATABASE_NAME"), host=app.config.get("DATABASE_HOST"))

if __name__ == '__main__':
    app.run(debug=True)

