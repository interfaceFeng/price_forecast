from flask import Flask
from mongoengine import connect
import config


app = Flask(__name__)
app.config.from_object(config)


def register_blueprints(_app):
    # Prevents circular imports
    from price_interface.upload import upload
    # from views import admin
    _app.register_blueprint(upload)

register_blueprints(app)
connect(app.config.get("DATABASE_NAME"), host=app.config.get("DATABASE_HOST"))

if __name__ == '__main__':
    app.run(debug=True)
