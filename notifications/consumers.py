import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class NotificationConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.user = None

    def connect(self):
        self.user = self.scope['user']
        if self.user.is_authenticated:
            async_to_sync(self.channel_layer.group_add)(
                f'user_{self.user.id}'
            )
            self.accept()

    def disconnect(self, close_code):
        if self.user.is_authenticated:
            async_to_sync(self.channel_layer.group_discard)(
                f'user_{self.user.id}'
            )

    def receive(self, text_data):
        pass

    def send_notification(self, event):
        notification = event['notification']
        self.send(text_data=json.dumps(notification))
