from . import routes

def setup(app):
    app.router.add_route("POST", "/pip", routes.pip)