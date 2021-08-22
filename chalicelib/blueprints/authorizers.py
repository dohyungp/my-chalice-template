from chalice import AuthResponse, Blueprint
from chalice.app import AuthRequest

app = Blueprint(__name__)


@app.authorizer(ttl_seconds=120)
def my_authorizer(auth_request: AuthRequest) -> AuthResponse:
    """My Authorizer"""
    return AuthResponse(routes=[], principal_id="deny")
