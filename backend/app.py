from flask import Flask, render_template
from routes.store import store_blueprint
from routes.marketing import marketing_blueprint
from config import Config
from database import db

app = Flask(__name__, template_folder="templates")  # Specify the template folder
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Register Blueprints (modular routing)
app.register_blueprint(store_blueprint, url_prefix="/store")
app.register_blueprint(marketing_blueprint, url_prefix="/marketing")

@app.route("/")
def home():
    return render_template("index.html")  # Render the index.html template

if __name__ == "__main__":
    app.run(debug=True, port=5002)
