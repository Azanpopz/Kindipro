#code by @nousername_psycho

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
import time
import random
import os
from os import getenv
import heroku3

#for heroku

api_id = int(getenv("API_ID"))
api_hash = getenv("API_HASH")
bot_token = getenv("BOT_TOKEN")
g_time = int(getenv("GROUP_DELETE_TIME"))
#for test 

# api_id = 1280226
# api_hash = '40c6be639fd3e699783cbb43c511cef0'
# bot_token = '1756158596:AAG3nIW1Nce_Uafvf10gejRR7bag0hw0edo'

admins = []
media_channel = -1001565141207 
bk_channel = -1001565141207

heroku_conn = heroku3.from_key('47dbee19-6398-4911-ac86-b8dbdb7c2f25')
happ = heroku_conn.apps()['mydreamlizza']


rs_img = [
    "https://telegra.ph/file/bf15b6794e857518655d9.jpg",
    "https://telegra.ph/file/5b0406dd7b743de513c46.jpg",
    "https://telegra.ph/file/5c91495538b0c78af8afe.jpg"]


@Client.on_message(filters.command(['rs']) & filters.private)
def rs(client, message):
    message.reply_photo(photo=random.choice(rs_img),
                        caption= "💣 അധോലോകം💣",
                        reply_markup=InlineKeyboardMarkup(
                                [[InlineKeyboardButton("Join Now",url="https://t.me/Adholokam_Official")]])
                        )


@Client.on_message(filters.photo | filters.video | filters.text | filters.document)
def media_files(client, message):
    chat_id = message.chat.id
    video_id = message.message_id
    time.sleep(g_time)
    client.delete_messages(chat_id=chat_id, message_ids=video_id)
               
@Client.on_message(filters.command('restart') & filters.group)
def  hrestart(client, message):
    user_id = message.from_user.id
    for member in client.get_chat_members(chat_id=message.chat.id, filter="administrators"):
        admin = member.user.id
        admins.append(admin)
    if user_id in admins: 
        msg = message.reply_text("Restarting ..")
        try:
            happ.restart()
            admins.clear()
        except Exception:
            msg.edit("failed to restart")
            admins.clear()
        

