from flask import Flask, request, jsonify, send_from_directory, render_template
from routes.store import store_blueprint
from routes.marketing import marketing_blueprint
from config import Config
from database import db
import os

app = Flask(__name__, static_folder="../frontend/build", template_folder="../frontend/build")

app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Register Blueprints (modular routing)
app.register_blueprint(store_blueprint, url_prefix="/store")
app.register_blueprint(marketing_blueprint, url_prefix="/marketing")

# Serve React/HTML Frontend
@app.route("/")
def serve_frontend():
    return render_template("index.html")

@app.route("/<path:path>")
def serve_static_files(path):
    """Serve static assets like CSS/JS from the frontend build directory."""
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
