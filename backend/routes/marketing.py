from flask import Blueprint

marketing_blueprint = Blueprint("marketing", __name__)

@marketing_blueprint.route("/marketing")
def marketing_home():
    return {"message": "Marketing API is running"}
