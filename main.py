from fastapi import FastAPI
import uvicorn
# from models import Product
from config import engine, session
from database_model import Base, Product
import database_model

database_model.Base.metadata.create_all(bind = engine)
 
app = FastAPI()

# @app.get("/")
# def main():
#     return "Hello from project!"

# products = [
#     Product(id=1,name="fogg",price=200,description="no gas",qty=2),
#     Product(id=2,name="denver",price=200,description="no gas",qty=2),
#     Product(id=4,name="denver",price=200,description="no gas",qty=2)
# ]

# @app.get("/get_products")
# def get_all_products():
#     # for product in products:
#         return products

# @app.get("/product/{id}")
# def get_product_byid(id: int):
#     for product in products:
#         if id == product.id:
#             return product
    
#     return "Produt not found"

# @app.post("/product")
# def add_product(product: Product):
#     products.append(product)
#     return "product added successfully."

if __name__ =="__main__":
    uvicorn.run("main:app", reload= True)

# "main:app"
#       ↓
# Split into module + variable
#       ↓
# Import main.py
#       ↓
# Get app object
#       ↓
# Start ASGI server
#       ↓
# Handle requests
