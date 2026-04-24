from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        self.connections: dict[int, WebSocket] = {}

    async def connect(self, user_id: int, websocket: WebSocket):
        await websocket.accept()
        self.connections[user_id] = websocket
        print(f"Usuário {user_id} conectado")

    def disconnect(self, user_id: int):
        if user_id in self.connections:
            del self.connections[user_id]
            print(f"Usuário {user_id} desconectado")

    async def send_to_user(self, user_id: int, message: dict):
        websocket = self.connections.get(user_id)
        if websocket:
            await websocket.send_json(message)
        else:
            print(f"Usuário {user_id} não está conectado")

    async def broadcast(self, message: dict):
        for websocket in self.connections.values():
            await websocket.send_json(message)

manager = ConnectionManager()