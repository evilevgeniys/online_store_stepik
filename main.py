import uvicorn
from fastapi import FastAPI

from routers import categories, products

from database import Base, engine


# Создаём приложение FastAPI
app = FastAPI(
    title="FastAPI Интернет-магазин",
    version="0.1.0",
)

Base.metadata.create_all(bind=engine)

# Подключаем маршруты категорий
app.include_router(categories.router)
app.include_router(products.router)


# Корневой эндпоинт для проверки
@app.get("/")
async def root():
    """
    Корневой маршрут, подтверждающий, что API работает.
    """
    return {"message": "Добро пожаловать в API интернет-магазина!"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)