import os
import play_scraper
from pyrogram import Client, filters
from pyrogram.types import *
from pyrogram import Client as Koshik

Bot = Client(
    "Play-Store-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('✨ ❤️ 😁 Made By 😁 ❤️ ✨', url='https://t.me/KoshikKumar17')]])



@Koshik.on_message(filters.command("app"))
async def search(bot, update):
    koshik = await update.reply_text("**Shorting your link....👤\n\nPlease wait a bit..🙃**",quote=True)
    query = update.text.split(None, 1)[1]
    reply_markup = BUTTONS
    await koshik.edit_text(
        text=search(query),
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

def search(type):
    try:
        results = play_scraper.search(update.query)
        answers = []
    
        details = "**Title:** `{}`".format(result["title"]) + "\n" \
        "**Description:** `{}`".format(result["description"]) + "\n" \
        "**App ID:** `{}`".format(result["app_id"]) + "\n" \
        "**Developer:** `{}`".format(result["developer"]) + "\n" \
        "**Developer ID:** `{}`".format(result["developer_id"]) + "\n" \
        "**Score:** `{}`".format(result["score"]) + "\n" \
        "**Price:** `{}`".format(result["price"]) + "\n" \
        "**Full Price:** `{}`".format(result["full_price"]) + "\n" \
        "**Free:** `{}`".format(result["free"]) + "\n" \
        "\n" + "Made by @FayasNoushad"
        reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Play Store", url="https://play.google.com"+result["url"])]]
        )
        try:
            answers.append(
                InlineQueryResultArticle(
                    title=result["title"],
                    description=result.get("description", None),
                    thumb_url=result.get("icon", None),
                    input_message_content=InputTextMessageContent(
                        message_text=details, disable_web_page_preview=True
                    ),
                    reply_markup=reply_markup
                )
            )
        except Exception as error:
            print(error)
            return error



