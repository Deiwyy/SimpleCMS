from flask import Blueprint, jsonify
from db.connection import get_db

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/")
def index():
    return "Hello!"
