from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__)
    
    # Use real DB by default, or memory DB if testing
    if test_config is None:
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '..', 'todo.db')
    else:
        app.config.update(test_config)
        
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    with app.app_context():
        from app import models
        db.create_all()
        
        from app import routes
        # Register blueprint only if it's not already registered
        if 'main' not in app.blueprints:
            app.register_blueprint(routes.bp)
            
    return app