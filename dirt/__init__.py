import os
from flask import Flask, g, request, jsonify
from nut.models.User import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config2.config import config # must import config before myce.api_client

def _get_db():
    if 'db_engine' not in g:
        g.db_engine = create_engine('%s://%s:%s@%s:%s/%s'%(
            config['database']['driver'],
            os.environ['DB_USER'],
            os.environ['DB_PW'],
            config['database']['domain'],
            config['database']['port'],
            config['database']['name'],
        ))

    return g.db_engine

def create_app():
    # create and configure the app
    # __name__ is the name of the current Python module
    app = Flask(__name__, instance_relative_config=False)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/user/<int:user_id>')
    def get_user(user_id):
        engine = _get_db()
        Session = sessionmaker(bind=engine)
        session = Session()
        user = session.query(User).get(user_id)
        return user

    @app.route('/user', methods=['POST'])
    def create_user():
        data = request.get_json()

        try:
            engine = _get_db()
            Session = sessionmaker(bind=engine)
            session = Session()

            session.add(User(name=data['name']))
            session.commit()

            return jsonify({ 'message': 'success' }), 201

        except Exception as inst:
            print(inst)
            return jsonify({ 'message': 'failure' }), 500

    return app
