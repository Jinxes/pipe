from boot import app
from ports.user import blueprint as user

app.register_blueprint(user)
