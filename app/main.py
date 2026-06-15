from fastapi import FastAPI

from app.routers import auth_router

from app.routers import users_router

from app.routers import authors_router

from app.routers import books_router

from app.routers import reviews_router


app = FastAPI(
    title="Limkokwing Library Management",
    description="Welcome to Limkokwing Library Management API System",
    version="1.0.0",
    contact={
        "name": "GROUP-F",
        "email": "ujumili3t@gmail.com"
    }
)

app.include_router(
    auth_router.router
)

app.include_router(
    users_router.router
)

app.include_router(
    authors_router.router
)

app.include_router(
    books_router.router
)

app.include_router(
    reviews_router.router
)

@app.get("/")
def root():
    return {
        "message":
        "Limkokwing Library Management API is running"
    }