from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        self.connections : list[WebSocket] = {}

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.connections.remove(websocket)

    async def send_to_user(self, id: int, message: dict):
        websocket = self.connections.get(id)
        if websocket:
            await websocket.send_json(message)

    async def broadcast(self, message: dict):
        for conn in self.connections:
            await conn.send(message)

manager = ConnectionManager()