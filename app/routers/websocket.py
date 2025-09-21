from fastapi import APIRouter, WebSocket

router = APIRouter(prefix="/ws", tags=["WebSocket"])


@router.websocket("/echo")
async def websocket_echo(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"You said: {data}")
