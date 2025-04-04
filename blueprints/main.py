from flask import Blueprint, jsonify
from db.connection import get_db

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return "Hello!"
