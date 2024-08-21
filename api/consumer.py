import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import OtpAuth
from .serializers import OtpAuthSerializer
from asgiref.sync import sync_to_async

@sync_to_async
def take_token(username):
    user = OtpAuth.objects.filter(user__username=username)
    if user.exists():
        message = user.first().token
    else:
        message = "User does not exists"
    
    return message

class TokenConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.close()
        
    async def disconnect(self, close_code):
        pass
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        username = text_data_json['user']
        message = await take_token(username)

        # Mesajı WebSocket üzerinden gönder
        await self.send(text_data=json.dumps({
            'message': message
        }))
