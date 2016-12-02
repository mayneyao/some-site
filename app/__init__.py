from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.moment import Moment
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager
from flask.ext.pagedown import PageDown
import markdown
from .config import sql_user,sql_pwd,sql_ip,sql_name,SECRET_KEY

md = markdown.Markdown(extensions=['markdown.extensions.codehilite','markdown.extensions.extra'])
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(sql_user,sql_pwd,sql_ip,sql_name)
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] =True
    app.debug=True
    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api_1_0 import  api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint,url_prefix="/api/v1.0")

    return app

