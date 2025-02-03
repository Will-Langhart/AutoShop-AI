from flask import Flask, render_template
from routes.store import store_blueprint
from routes.marketing import marketing_blueprint
from config import Config
from database import db

app = Flask(__name__, template_folder="templates")  # Specify the template folder
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Register Blueprints
app.register_blueprint(store_blueprint, url_prefix="/store")  # Ensure this is correct
app.register_blueprint(marketing_blueprint, url_prefix="/marketing")

@app.route("/")
def home():
    return render_template("index.html")  # Serve the homepage

if __name__ == "__main__":
    app.run(debug=True, port=5002)
