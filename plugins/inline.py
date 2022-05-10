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



@Client.on_message(filters.private & filters.text)
async def filter_text(bot, update):
    results = requests.get(API + requests.utils.requote_uri(update.query)).json()["result"][:50]
    answers = []
    await update.reply_text(
        title=update.query.capitalize(),
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


@Client.on_inline_query(["im"])
results = requests.get(API + requests.utils.requote_uri(update.query)).json()["result"][:50]
answers = []
    for result in results:
        answers.append(
            InlineQueryResultPhoto(
                title=update.query.capitalize(),
                description=result,
                caption="Made by @FayasNoushad",
                photo_url=result
            )
        )
    await update.answer(answers)



