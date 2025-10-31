
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .routes import dogs

app = FastAPI(
    title='Olive API Server',
)

@app.middleware("http")
async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        print(e)
        return JSONResponse(
            status_code=500,
            content={"message": f"An internal server error occurred. {e}"},
        )

app.include_router(dogs.router)
