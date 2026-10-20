
from flask import Flask
from datetime import datetime
import sys

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

    @app.route("/api/v1/status", methods=["GET"])
    def status():
        return {
            "status": "running",
            "timestamp": datetime.now().isoformat(),
            "python_version": sys.version.split()[0]
        }

    @app.route("/api/v1/info", methods=["GET"])
    def info():
        return {
            "course": "Dasar Pemrograman Backend",
            "code": "KK112105",
            "campus": "STIKOM PGRI Banyuwangi",
            "meeting": 4
        }

    return app
