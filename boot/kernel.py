from boot import app
from ports.user import blueprint as user
from ports.session import blueprint as session

app.register_blueprint(user)
app.register_blueprint(session)
