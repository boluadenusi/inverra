from flask import Flask
from inverra.api import bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp, url_prefix='/api')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)