from flask import Flask
from app.routes.product_routes import product_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(product_bp)

    @app.route("/")
    def home():
        return {
            "message": "API Produk Berhasil Berjalan",
            "version": "1.0.0"
        }

    return app