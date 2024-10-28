from flask import Blueprint, render_template, g
from app.core.oidc import get_authenticated_user

main_bp = Blueprint('main', __name__)

@main_bp.get('/')
def root():
    return render_template('main.html', user=get_authenticated_user())
