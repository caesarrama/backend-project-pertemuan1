from flask import Flask, jsonify, request
from datetime import datetime
import platform

# Inisialisasi instansiasi aplikasi Flask
app = Flask(__name__)

# Endpoint 1: Root / Health Check Service
@app.route('/', methods=['GET'])
def root_health_check():
    return jsonify({
        "status": "success",
        "message": "Backend API Service Aktif dan Berjalan",
        "version": "1.0.0"
    }), 200

# Endpoint Tambahan: Status Operasional Server
@app.route('/api/v1/status', methods=['GET'])
def get_server_status():
    status_data = {
        "server_status": "running",
        "timestamp": datetime.now().isoformat(),
        "python_version": platform.python_version()
    }

    return jsonify({
        "status": "success",
        "data": status_data
    }), 200

# Endpoint 2: Informasi Akademik & Perkuliahan
@app.route('/api/v1/info', methods=['GET'])
def get_academic_info():
    response_payload = {
        "status": "success",
        "data": {
            "course": "Dasar Pemrograman Backend",
            "code": "KK112105",
            "institution": "STIKOM PGRI Banyuwangi",
            "meeting": 1,
            "topic": "Environment Setup & Flask Core Concept"
        }
    }
    return jsonify(response_payload), 200

# Endpoint 3: Profil Data Mahasiswa (Dummy)
@app.route('/api/v1/mahasiswa', methods=['GET'])
def get_mahasiswa_profile():
    profile_data = {
        "status": "success",
        "data": {
            "nim": "202611001",
            "nama": "Mahasiswa Backend",
            "prodi": "Teknik Informatika",
            "status_akademik": "Aktif"
        }
    }
    return jsonify(profile_data), 200

# Blok Eksekusi Aplikasi
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)