from flask import Flask, jsonify
from routes.store import store_blueprint
from routes.marketing import marketing_blueprint
from config import Config
from database import db

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Register Blueprints (modular routing)
app.register_blueprint(store_blueprint, url_prefix="/store")
app.register_blueprint(marketing_blueprint, url_prefix="/marketing")

@app.route("/")
def home():
    return jsonify({"message": "Welcome to AutoShop AI - AI-Powered Shopify Store Generator"})

if __name__ == "__main__":
    app.run(debug=True, port=5002)
