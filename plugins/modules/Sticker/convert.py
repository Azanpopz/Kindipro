import os
from PIL import Image
from pyrogram.types import Message
from pyrogram import Client, filters
import requests 




@Client.on_message((filters.private | filters.sticker | filters.photo | filters.group) & filters.command('con'))
async def sticker_image(_, msg: Message):
        
        message = await msg.reply("Converting...")
        if msg.photo:
            user_id = msg.from_user.id
            message_id = msg.message_id
            name_format = f"StarkBots_{user_id}_{message_id}"
    
            image = await msg.download(file_name=f"{name_format}.jpg")
            await message.edit("Sending...")
            im = Image.open(image).convert("RGB")
            im.save(f"{name_format}.webp", "webp")
            sticker = f"{name_format}.webp"
            await msg.reply_sticker(sticker)
            await message.delete()
            os.remove(sticker)
            os.remove(image)
      
