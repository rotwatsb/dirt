import os
from flask import Flask

def create_app():
    # create and configure the app
    # __name__ is the name of the current Python module
    app = Flask(__name__, instance_relative_config=False)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
