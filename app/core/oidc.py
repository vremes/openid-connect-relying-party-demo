from flask import g
from flask_oidc.model import User

def get_authenticated_user() -> User | None:
    if not g.oidc_user:
        return None
    
    if g.oidc_user.logged_in is False:
        return None
    
    return g.oidc_user
