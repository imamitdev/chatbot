import json
import os
from channels.generic.websocket import AsyncWebsocketConsumer
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        user_message = data["message"]

        response = await self.get_bot_response(user_message)

        await self.send(text_data=json.dumps({"response": response}))

    async def get_bot_response(self, message):

        chunk = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=message,
        )
        return chunk.text
