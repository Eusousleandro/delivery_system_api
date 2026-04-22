from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.infrastructure.websockets.connection_manager import manager

router = APIRouter()

@router.websocket('/ws/ords/{id}')
async def websocket_endpoint(websocket: WebSocket, id: int):
    await manager.connect(id, websocket)
    try: 
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(id)