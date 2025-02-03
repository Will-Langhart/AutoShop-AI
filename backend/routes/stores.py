from flask import Blueprint, request, jsonify
from services.gpt4_service import generate_product_descriptions
from services.image_generator import generate_ai_images
from database import db
from models import Store, Product

store_blueprint = Blueprint("store", __name__)

@store_blueprint.route("/create", methods=["POST"])
def create_store():
    data = request.json
    store_name = data.get("store_name")
    owner_email = data.get("owner_email")

    if not store_name or not owner_email:
        return jsonify({"error": "Store name and owner email are required"}), 400

    new_store = Store(name=store_name, owner_email=owner_email)
    db.session.add(new_store)
    db.session.commit()

    return jsonify({"message": "Store created successfully!", "store_id": new_store.id})

@store_blueprint.route("/products/generate", methods=["POST"])
def generate_products():
    data = request.json
    store_id = data.get("store_id")
    product_names = data.get("product_names", [])

    if not store_id or not product_names:
        return jsonify({"error": "Store ID and product names are required"}), 400

    descriptions = generate_product_descriptions(product_names)
    image_urls = generate_ai_images(product_names)

    products = []
    for name, desc, img in zip(product_names, descriptions, image_urls):
        new_product = Product(store_id=store_id, name=name, description=desc, image_url=img, price=19.99)
        db.session.add(new_product)
        products.append({
            "name": name,
            "description": desc,
            "image_url": img
        })

    db.session.commit()

    return jsonify({"message": "Products generated successfully!", "products": products})
