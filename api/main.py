from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel  # Agregamos esta línea
from typing import List, Optional

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    quantity = Column(Integer)
    description = Column(String)
    price = Column(Float)

Base.metadata.create_all(bind=engine)

class ProductCreate(BaseModel):
    title: str
    quantity: int
    description: str
    price: float

class ProductResponse(BaseModel):
    id: int
    title: str
    quantity: int
    description: str
    price: float

# Ruta para crear un nuevo producto
@app.post("/products/", response_model=ProductResponse)
def create_product(product: ProductCreate):
    db = SessionLocal()
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Ruta para obtener la lista de productos
@app.get("/products/", response_model=List[ProductResponse])
def get_products(skip: int = 0, limit: int = 10):
    db = SessionLocal()
    products = db.query(Product).offset(skip).limit(limit).all()
    return products

# Ruta para obtener un producto por su ID
@app.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int):
    db = SessionLocal()
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product

# Ruta para actualizar un producto por su ID
@app.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductCreate):
    db = SessionLocal()
    existing_product = db.query(Product).filter(Product.id == product_id).first()
    if existing_product is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    for key, value in product.dict().items():
        setattr(existing_product, key, value)
    db.commit()
    db.refresh(existing_product)
    return existing_product

# Ruta para eliminar un producto por su ID
@app.delete("/products/{product_id}", response_model=ProductResponse)
def delete_product(product_id: int):
    db = SessionLocal()
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(product)
    db.commit()
    return product

# ... (código anterior)

# Crear productos de prueba iniciales
initial_products = [
    Product(
        title=f"Producto {i}",
        quantity=i * 10,
        description=f"Descripción del producto {i}",
        price=i * 9.99
    )
    for i in range(10)
]

db = SessionLocal()
for product in initial_products:
    db.add(product)
db.commit()
db.close()

