from flask.ext.script import Manager
from price_forecast import app
__author__ = 'saber'
manager = Manager(app)


@manager.command
def runserver():
    app.run(debug=True)

if __name__ == "__main__":
    manager.run()

