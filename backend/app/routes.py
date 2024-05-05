from flask import Flask

def init_app(app: Flask):
    @app.route("/")
    def index():
        return "Hello, FaceFacts backend!"

    @app.route("/hello")
    def hello():
        return "Hello World!"
