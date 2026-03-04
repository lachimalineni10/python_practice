from fastapi import FastAPI
import uvicorn
# from models import Product
from config import engine, session
from models.product import Base, Product
from sqlalchemy import text

# Test database connection
try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("Database connection test: SUCCESS")
except Exception as e:
    print(f"Database connection test: FAILED - {e}")

Base.metadata.create_all(bind=engine)
print(f"Tables in metadata: {Base.metadata.tables.keys()}")

 
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
