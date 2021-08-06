import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer

from face_recognition_app.app.face_finder import FaceIdentifier


class FaceConsumer(AsyncJsonWebsocketConsumer):
    """

    """
    face_identifier = FaceIdentifier()

    async def connect(self):
        """
        """
        self.room_name = self.scope['url_route']['kwargs']['room_code']
        self.room_group_name = 'room_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        print("Disconnected")
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        response = json.load(text_data)
        data = response.get('data', None)

        self.channel_layer.group_send(self.room_group_name, {})

    async def send_message(self, res):
        """ Receive message from room group """
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "payload": res,
        }))
