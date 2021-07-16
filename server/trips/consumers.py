from channels.generic.websocket import AsyncJsonWebsocketConsumer


class UberConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, code):
        await super().disconnect(code)