import os
import requests
from pyrogram import Client, filters
from pyrogram.types import *


Bot = Client(
    "Image-Search-Bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

API = "https://apibu.herokuapp.com/api/y-images?query="



@Client.on_message(filters.command(["img"]) & filters.private & filters.text & filters.photo)
async def search(bot, update):
    results = requests.get(API + requests.utils.requote_uri(update.query)).json()["result"][:1]
    answers = []
    await update.reply_photo(
        title=update.bot.capitalize(),
        description=result,
        caption="Made by @FayasNoushad",
        photo_url=result,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="Search Here", switch_inline_query_current_chat=update.text)],
                [InlineKeyboardButton(text="Search in another chat", switch_inline_query=update.text)]
            ]
        ),
        disable_web_page_preview=True,
        quote=True
    )



    await update.reply_photo(answers)



