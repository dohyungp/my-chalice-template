from chalice import Chalice
from chalicelib.blueprints import authorizers
from chalicelib.core.config import settings

app: Chalice = Chalice(app_name=settings.APP_NAME)
app.debug = settings.STAGE == "dev"

@app.route('/')
def index():
    """데모"""
    return {'hello': 'world'}

app.register_blueprint(authorizers.app)
