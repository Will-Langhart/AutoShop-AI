import requests
import os

STABLE_DIFFUSION_API = "https://api.stablediffusion.com/v1/generate"

def generate_ai_images(product_names):
    images = []
    for product in product_names:
        response = requests.post(STABLE_DIFFUSION_API, json={"prompt": f"High-quality eCommerce image of {product}"})
        images.append(response.json().get("image_url", ""))
    
    return images
