# chat/consumers.py
from asgiref.sync import async_to_sync
from django.contrib.auth import get_user_model
from channels.generic.websocket import WebsocketConsumer

from .models import ChatMessage

import json

User = get_user_model()

class ChatConsumer(WebsocketConsumer):
    # Connects to the websocket and joins a group (broadcast) with the static name 'chat'
    def connect(self):
        async_to_sync(self.channel_layer.group_add)("chat", self.channel_name)
        self.accept()

    # Disconnects from the websocket and broadcast group with the static name 'chat'
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("chat", self.channel_name)

    # Receiver
    def receive(self, text_data):
        get_key_val = json.loads(text_data)
        user = get_key_val['user']
        time = get_key_val['time']
        message = get_key_val['message']

        # Save to Model
        find_user = User.objects.get(username=user)
        ChatMessage.objects.create(
            user = find_user,
            message = message,
            time = time,
        )

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            "chat",
            {
                "type": "chat_message",
                "user": user,
                "time": time,
                "message": message
            }
        )

    # Sender
    def chat_message(self, event):
        user = event["user"]
        time = event["time"]
        message = event["message"]
        
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            "user": user, 
            "time": time,
            "message": message
        }))

