import os
import aiohttp
import json
from pyrogram import Client, filters, emoji
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


app = Client("trntsrcbot", api_id=int(os.environ.get("API_ID")), api_hash=os.environ.get("API_HASH"), bot_token=os.environ.get("BOT_TOKEN"))


print("\nBot Started\n")


@Client.on_message(filters.command(['starrt']))
async def start(_, message):
    await message.reply_text("Hello I'm PirateBay Torrent Scraper Bot\nSend /help To Show Help Screen\nBot by @unkusr")



@Client.on_message(filters.command(['help']))
async def help(_, message):
    await message.reply_text("Example: /trt titanic")

m = None
i = 0
a = None
query = None


@Client.on_message(filters.command(["trt"]))
async def trt(_, message):
    global m
    global i
    global a
    global query
    try:
        await message.delete()
    except:
        pass
    if len(message.command) < 2:
        await message.reply_text("Usage: /trt query")
        return
    query = message.text.split(None, 1)[1].replace(" ", "%20")
    m = await message.reply_text("Searching")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.api-zero.workers.dev/piratebay/{query}") \
                    as resp:
                a = json.loads(await resp.text())
    except:
        await m.edit("Found Nothing.")
        return
    result = (
        f"**Page - {i+1}**\n\n"
        f"➲Name: {a[i]['Name']}\n"
        f"➲{a[i]['Uploader']} on "
        f"{a[i]['Date']}\n" 
        f"➲Size: {a[i]['Size']}\n"
        f"➲Leechers: {a[i]['Leechers']} || "
        f"➲Seeders: {a[i]['Seeders']}\n"
        f"➲Type: {a[i]['Category']}\n"
        f"➲Magnet: `{a[i]['Magnet']}`\n\n\n"
    )
    await m.edit(
        result,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"Next",
                                         callback_data="next"),
                    InlineKeyboardButton(f"{emoji.CROSS_MARK}",
                                         callback_data="delete")
                ]
            ]
        ),
        parse_mode="markdown",
    )


@Client.on_callback_query(filters.regex("next"))
async def callback_query_next(_, message):
    global i
    global m
    global a
    global query
    i += 1
    result = (
        f"**Page - {i+1}**\n\n"
        f"➲Name: {a[i]['Name']}\n"
        f"➲{a[i]['Uploader']} on "
        f"{a[i]['Date']}\n" 
        f"➲Size: {a[i]['Size']}\n"
        f"➲Leechers: {a[i]['Leechers']} || "
        f"➲Seeders: {a[i]['Seeders']}\n"
        f"➲Type: {a[i]['Category']}\n"
        f"➲Magnet: `{a[i]['Magnet']}`\n\n\n"
    )
    await m.edit(
        result,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"Prev",
                                         callback_data="previous"),
                    InlineKeyboardButton(f"{emoji.CROSS_MARK}",
                                         callback_data="delete"),
                    InlineKeyboardButton(f"Next",
                                         callback_data="next")
                    
                ]
            ]
        ),
        parse_mode="markdown",
    )


@Client.on_callback_query(filters.regex("previous"))
async def callback_query_previous(_, message):
    global i
    global m
    global a
    global query
    i -= 1
    result = (
        f"**Page - {i+1}**\n\n"
        f"➲Name: {a[i]['Name']}\n"
        f"➲{a[i]['Uploader']} on "
        f"{a[i]['Date']}\n" 
        f"➲Size: {a[i]['Size']}\n"
        f"➲Leechers: {a[i]['Leechers']} || "
        f"➲Seeders: {a[i]['Seeders']}\n"
        f"➲Type: {a[i]['Category']}\n"
        f"➲Magnet: `{a[i]['Magnet']}`\n\n\n"
    )
    await m.edit(
        result,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"Prev",
                                         callback_data="previous"),
                    InlineKeyboardButton(f"{emoji.CROSS_MARK}",
                                         callback_data="delete"),
                    InlineKeyboardButton(f"Next",
                                         callback_data="next")
                ]
            ]
        ),
        parse_mode="markdown",
    )


@Client.on_callback_query(filters.regex("delete_trt"))
async def callback_query_delete_trt(_, message):
    global m
    global i
    global a
    global query
    await m.delete()
    m = None
    i = 0
    a = None
    query = None



