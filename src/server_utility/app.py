from fastapi import FastAPI, WebSocket
from starlette.responses import FileResponse

main_app = FastAPI(
    title="messages",
    description="service",
    version="1.0.0",
)


@main_app.get("/")
async def root():
    return FileResponse("client_utility/main_page_ws.html")


@main_app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    counter = 1  # Used to numerate messages on main page
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        await websocket.send_json({"msg": data["value"], "counter": counter})
        counter += 1
