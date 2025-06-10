from flask import Blueprint, jsonify
from controller.category_controller import CategoryController

category_routes = Blueprint("category_routes", __name__)

@category_routes.route("/categories")
def get_categories():
    return jsonify(CategoryController.fetch_categories()), 200
