from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as startlette_exception
from src.auth.routes import auth_router
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.routes.routes import router as book_router


@asynccontextmanager
async def life_span(app: FastAPI):
    print(f"server is starting...")
    await init_db()
    yield
    print(f"server has been stopped")


version = "v1"
app = FastAPI(
    title="fastapi db_webapp",
    description="simple crud app",
    version=version,
    lifespan=life_span
)

# global exception handler

# @app.exception_handler(startlette_exception)
# async def custom_http_exception_handler(
#         request: Request,
#         exc: startlette_exception
# ):
#     if exc.status_code == 404:
#         return JSONResponse(
#             status_code=status.HTTP_404_NOT_FOUND,
#             content={
#                 "message": "Oops! This API endpoint does not exist."
#             }
#         )
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={"message": exc.detail}
#     )


app.include_router(book_router, prefix=f"/api/{version}/books", tags=['books'])
app.include_router(auth_router, prefix=f"/api/{version}/auth", tags=['auth'])
