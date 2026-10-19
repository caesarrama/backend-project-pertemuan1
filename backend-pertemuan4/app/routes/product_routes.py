from flask import Blueprint, jsonify, request
from app.services.product_service import (
    get_products,
    create_product
)

product_bp = Blueprint("products", __name__)


@product_bp.route("/api/v1/products", methods=["GET"])
def list_products():
    products = get_products()

    return jsonify({
        "status": "success",
        "total": len(products),
        "data": products
    }), 200


@product_bp.route("/api/v1/products", methods=["POST"])
def add_new_product():
    data = request.get_json(silent=True)

    product, error = create_product(data)

    if error:
        return jsonify({
            "status": "error",
            "message": error
        }), 400

    return jsonify({
        "status": "success",
        "message": "Produk berhasil ditambahkan",
        "data": product
    }), 201