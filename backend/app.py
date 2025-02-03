from flask import Flask, request, jsonify, send_from_directory, render_template
from routes.store import store_blueprint
from routes.marketing import marketing_blueprint
from config import Config
from database import db
import os

# Ensure correct paths for serving frontend
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
FRONTEND_BUILD_DIR = os.path.join(BASE_DIR, "../frontend/build")

app = Flask(__name__, static_folder=FRONTEND_BUILD_DIR, template_folder=FRONTEND_BUILD_DIR)
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Register Blueprints (modular routing)
app.register_blueprint(store_blueprint, url_prefix="/store")
app.register_blueprint(marketing_blueprint, url_prefix="/marketing")

# Serve React Frontend
@app.route("/")
def serve_frontend():
    """Serve the React `index.html` file as the main page."""
    return render_template("index.html")

# Serve Static Files (CSS, JS, Images)
@app.route("/<path:path>")
def serve_static_files(path):
    """Serve static assets like CSS/JS from the frontend build directory."""
    file_path = os.path.join(app.static_folder, path)
    if os.path.exists(file_path):
        return send_from_directory(app.static_folder, path)
    return render_template("index.html")  # Fallback to React frontend for 404s

if __name__ == "__main__":
    app.run(debug=True, port=5002)
