import os
from PIL import Image
from pyrogram.types import Message
from pyrogram import Client, filters
import requests 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 






@Client.on_message((filters.private | filters.sticker | filters.photo | filters.group) & filters.command('conv'))
async def sng(bot, message):
        if not message.reply_to_message:
          await message.reply_text("Please reply to a message")
        else:          
          mee = await message.reply_text("`Searching 🔎`")
          image = await message.download(file_name=f"{name_format}.jpg")
          user_id = message.from_user.id
          im = Image.open(image).convert("RGB")
          im.save(f"{name_format}.webp", "webp")
          sticker = f"{name_format}.webp"  
          await mee.delete()
          try:
            await mee.delete()
            await bot.send_message(user_id, message_id, name_format,reply_to_message_id = message.message_id, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs ", url = f"t.me/xd_botz")]]))
          except Exception as e:                            
            await message.reply_sticker(sticker)
            await message.delete()
            os.remove(sticker)
            os.remove(image)


@Client.on_message((filters.private | filters.sticker | filters.photo | filters.group) & filters.command('con'))
async def sticker_image(_, msg: Message):
    user_id = msg.from_user.id
    message_id = msg.message_id
    name_format = f"StarkBots_{user_id}_{message_id}"
    if msg.photo:
        message = await msg.reply("Converting...")
        image = await msg.download(file_name=f"{name_format}.jpg")
        await message.edit("Sending...")
        im = Image.open(image).convert("RGB")
        im.save(f"{name_format}.webp", "webp")
        sticker = f"{name_format}.webp"
        await msg.reply_sticker(sticker)
        await message.delete()
        os.remove(sticker)
        os.remove(image)
    elif msg.sticker.is_animated:
        await msg.reply("Animated stickers are not supported !", quote=True)
    else:
        message = await msg.reply("Converting...")
        sticker = await msg.download(file_name=f"{name_format}.webp")
        await message.edit("Sending...")
        im = Image.open(sticker).convert("RGB")
        im.save(f"{name_format}.jpg", "jpeg")
        image = f"{name_format}.jpg"
        await msg.reply_photo(image)
        await message.delete()
        os.remove(image)
        os.remove(sticker)
