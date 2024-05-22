from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'EYSvJCa;McG_29 8t?CFX#5J5@$LPX'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefex='/') 
    app.register_blueprint(auth, url_prefex='/') 

    return app