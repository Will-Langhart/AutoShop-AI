from flask import Flask, send_from_directory
import os

# Define paths
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
FRONTEND_BUILD_DIR = os.path.join(BASE_DIR, "build")

# Initialize Flask app
app = Flask(__name__, static_folder=FRONTEND_BUILD_DIR, template_folder=FRONTEND_BUILD_DIR)

# Serve React Frontend (Main Page)
@app.route("/")
def serve_frontend():
    """Serve the React `index.html` file as the main page."""
    try:
        return send_from_directory(FRONTEND_BUILD_DIR, "index.html")
    except Exception as e:
        return f"Error: {e}", 500

# Serve Static Assets (CSS, JS, Images)
@app.route("/<path:path>")
def serve_static_files(path):
    """Serve static assets like CSS/JS from the frontend build directory."""
    try:
        return send_from_directory(FRONTEND_BUILD_DIR, path)
    except Exception as e:
        return f"File Not Found: {path}", 404

if __name__ == "__main__":
    app.run(debug=True, port=5002)
