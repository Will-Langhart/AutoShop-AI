import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_product_descriptions(product_names):
    descriptions = []
    for product in product_names:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert eCommerce marketer."},
                {"role": "user", "content": f"Generate a high-converting description for {product}."}
            ]
        )
        descriptions.append(response["choices"][0]["message"]["content"])
    
    return descriptions
