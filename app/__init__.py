from flask import Flask
import markdown

md = markdown.Markdown(extensions=['markdown.extensions.codehilite','markdown.extensions.extra'])

def create_app():
    app = Flask(__name__)
    #app.debug=True

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app

