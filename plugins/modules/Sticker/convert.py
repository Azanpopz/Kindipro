import os
from PIL import Image
from pyrogram.types import Message
from pyrogram import Client, filters
import requests 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 









@Client.on_message((filters.private | filters.sticker | filters.photo | filters.group) & filters.command('con'))
async def sng(bot, message):
        if not message.reply_to_message:
          await message.reply_text("Please reply to a message")
        else:          
          message = await message.reply("Converting...")
          image = await message.download(file_name=f"{name_format}.jpg")
          user_id = message.from_user.id
          message_id = message.message_id
          name_format = f"StarkBots_{user_id}_{message_id}"
          await mee.delete()
          
      if message.photo:
          message = await message.reply("Converting...")
          image = await message.download(file_name=f"{name_format}.jpg")
          await message.edit("Sending...")
          im = Image.open(image).convert("RGB")
          im.save(f"{name_format}.webp", "webp")
          sticker = f"{name_format}.webp"
          await message.reply_sticker(sticker)
          await message.delete()
          os.remove(sticker)
          os.remove(image)
      elif msg.sticker.is_animated:
          await msg.reply("Animated stickers are not supported !", quote=True)
      else:
          message = await message.reply("Converting...")
          sticker = await message.download(file_name=f"{name_format}.webp")
          await message.edit("Sending...")
          im = Image.open(sticker).convert("RGB")
          im.save(f"{name_format}.jpg", "jpeg")
          image = f"{name_format}.jpg"
          await message.reply_photo(image)
          await message.delete()
          os.remove(image)
          os.remove(sticker)
