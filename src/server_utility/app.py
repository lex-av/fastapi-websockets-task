from pathlib import Path

from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

main_app = FastAPI(
    title="messages",
    description="service",
    version="1.0.0",
)

main_app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)

templates = Jinja2Templates(directory="client_utility")


@main_app.get("/")
async def root(request: Request):
    # return FileResponse("client_utility/main_page_ws.html")
    return templates.TemplateResponse("main_page_ws.html", {"request": request})


@main_app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    counter = 1  # Used to numerate messages on main page
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            await websocket.send_json({"msg": data["value"], "counter": counter})
            counter += 1
    except WebSocketDisconnect:
        print("Client disconnected")
