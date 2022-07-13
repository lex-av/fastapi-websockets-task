from fastapi import FastAPI

main_app = FastAPI(
    title="messages",
    description="service",
    version="1.0.0",
)


@main_app.get("/")
async def root():
    return {"message": "Hello World"}
