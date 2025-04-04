from flask import Blueprint, jsonify, request, session, flash, redirect, url_for
from db.connection import get_db

admin_bp = Blueprint("admin", __name__)

@admin_bp.before_request
def before_request_func():
    if request.path == '/admin/login':
        return
    
    cms_user = session.get("cms_user")

    if cms_user is None:
        flash("Je moet er ingelogd zijn om dit pagina te bekijken!")
        return redirect(url_for("admin.login"))
    elif(bool(cms_user.get("is_admin")) == False):
        flash("Je moet een admin zijn om dit pagina te bekijken")
        return redirect(url_for("admin.login"))

    return
    
@admin_bp.route("/")
def index():
    return "Hello!"

@admin_bp.route("/login")
def login():
    return "Hello!"
