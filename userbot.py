import os
from pyrogram import Client

TOKEN= os.environ.get('TOKEN')


userbot = Client(
    TOKEN,
    api_id=int(os.environ.get('API_ID')),
    api_hash=os.environ.get("API_HASH")
)
