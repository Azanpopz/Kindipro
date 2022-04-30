import random
import asyncio
from Vars import Var
from info import PICS, ADMINS
from pyrogram import filters, Client
from utils import temp
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto

NEW_ABOUT_TEXT = """<b>😊 Use these buttons to know about me. Send /start to reload me.</b>"""

NEW_ABOUT_HOME = """<b>😊 Use these buttons to know about me. Send /start to reload me.</b>"""

RATING_TEXT = """This is rating text."""

SOURCE_TEXT = """This is source text."""

DONATE_TEXT = """This is donate text."""

NEW_HELP_TEXT = """<b>🧩 Here is the help of my commands. Send /about to know about me.</b>"""

NEW_HELP_HOME_TEXT = """<b>🧩 Here is the help of my commands. Send /about to know about me.</b>"""

FILE_STREAM_TEXT = """This is file stream text."""

FILE_STORE_TEXT = """This is file store text."""

INSTRUCTIONS_TEXT = """This is instructions text."""

TUTORIALS_TEXT = """This is tutorials text."""

WARNING_TEXT = """This is warning text."""

FILE_TEXT = """ This file has been deleted due to Pornographic reasons."""

VIDEO_TEXT = """ This file has been deleted due to Copyrighted material."""

AUDIO_TEXT = """ This file has been deleted due to Other reasons."""

FILE = ["https://telegra.ph/file/b2b658b749bb6b976ea8d.jpg"]

VIDEO = ["https://telegra.ph/file/bafed7e9c21f326193963.jpg"]

AUDIO = ["https://telegra.ph/file/a1900232d1715b8b9adbb.jpg"]

NEW_ABOUT_HOME_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⭐️ Rating', callback_data='rating'),
            InlineKeyboardButton('❤️ Source', callback_data='source'),
            ],[
            InlineKeyboardButton('💰 Donate', callback_data='donate')
            ]]
       )     

NEW_HELP_HOME_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('📥 File Stream', callback_data='file_stream'),
            InlineKeyboardButton('📦 File Store', callback_data='file_store'),
            ],[
            InlineKeyboardButton('⚙️ Instructions', callback_data='instructions'),
            InlineKeyboardButton('🕹 Tutorials', callback_data='tutorials'),
            ],[
            InlineKeyboardButton('⚠️ Warning', callback_data='warning')
            ]]
         )

ABOUT_BACK_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🔙 Back', callback_data='new_about_home')
            ]]
        )

HELP_BACK_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🔙 Back', callback_data='new_help_home')
            ]]
        )

@Client.on_callback_query()
async def cb_data(bot, update):
    if update.data == "new_about_home":
        await update.answer('www.hagadmansa.com')
        image=random.choice(PICS)
        await update.edit_message_media(
        media=InputMediaPhoto(media=image, caption=NEW_ABOUT_HOME),
        reply_markup=NEW_ABOUT_HOME_BUTTONS
        )
    elif update.data == "rating":
        await update.answer('www.hagadmansa.com')
        image=random.choice(PICS)
        await update.edit_message_media(
        media=InputMediaPhoto(media=image, caption=RATING_TEXT),
        reply_markup=ABOUT_BACK_BUTTONS
        )
    elif update.data == "source":
        await update.answer('www.hagadmansa.com')
        image=random.choice(PICS)
        await update.edit_message_media(
        media=InputMediaPhoto(media=image, caption=SOURCE_TEXT),
        reply_markup=ABOUT_BACK_BUTTONS
        )
    elif update.data == "donate":
        await update.answer('www.hagadmansa.com')
        image=random.choice(PICS)
        await update.edit_message_media(
        media=InputMediaPhoto(media=image, caption=DONATE_TEXT),
        reply_markup=ABOUT_BACK_BUTTONS
        )
    elif update.data == "new_help_home":
        await update.answer('www.hagadmansa.com')
        image=random.choice(PICS)
        await update.edit_message_media(
        media=InputMediaPhoto(media=image, caption=NEW_HELP_HOME_TEXT),
        reply_markup=NEW_HELP_HOME_BUTTONS
        )
    elif update.data == "file_stream":
        await update.answer('www.hagadmansa.com')
        image=random.choice(PICS)
        await update.edit_message_media(
        media=InputMediaPhoto(media=image, caption=FILE_STREAM_TEXT),
        reply_markup=HELP_BACK_BUTTONS
        )
    elif update.data == "file_store":
        await update.answer('www.hagadmansa.com')
        image=random.choice(PICS)
        await update.edit_message_media(
        media=InputMediaPhoto(media=image, caption=FILE_STORE_TEXT),
        reply_markup=HELP_BACK_BUTTONS
        )
    elif update.data == "instructions":
        await update.answer('www.hagadmansa.com')
        image=random.choice(PICS)
        await update.edit_message_media(
        media=InputMediaPhoto(media=image, caption=INSTRUCTIONS_TEXT),
        reply_markup=HELP_BACK_BUTTONS
        )
    elif update.data == "tutorials":
        await update.answer('www.hagadmansa.com')
        image=random.choice(PICS)
        await update.edit_message_media(
        media=InputMediaPhoto(media=image, caption=TUTORIALS_TEXT),
        reply_markup=HELP_BACK_BUTTONS
        )
    elif update.data == "warning":
        await update.answer('www.hagadmansa.com')
        image=random.choice(PICS)
        await update.edit_message_media(
        media=InputMediaPhoto(media=image, caption=WARNING_TEXT),
        reply_markup=HELP_BACK_BUTTONS
        )
    elif update.data == "close":
        await update.answer('www.hagadmansa.com')
        await update.message.delete()
        try:
            await update.message.reply_to_message.delete()
        except:
            pass
     
@Client.on_message(filters.command("about"))
async def about(client, message):
        await message.reply_photo(
        photo=random.choice(PICS),
        caption=(NEW_ABOUT_TEXT),
        reply_markup=InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⭐️ Rating', callback_data='rating'),
            InlineKeyboardButton('❤️ Source', callback_data='source'),
            ],[
            InlineKeyboardButton('💰 Donate', callback_data='donate')
        ]]))

@Client.on_message(filters.command("help")) 
async def help(client, message):
        await message.reply_photo(
        photo=random.choice(PICS),
        caption=(NEW_HELP_TEXT),
        reply_markup=InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('📥 File Stream', callback_data='file_stream'),
            InlineKeyboardButton('📦 File Store', callback_data='file_store'),
            ],[
            InlineKeyboardButton('⚙️ Instructions', callback_data='instructions'),
            InlineKeyboardButton('🕹 Tutorials', callback_data='tutorials'),
            ],[
            InlineKeyboardButton('⚠️ Warning', callback_data='warning')
         ]]))
       
YOUARENOT = ["https://telegra.ph/file/2e8725f268df2e9e693f1.jpg"]

@Client.on_message(filters.command("new")) 
async def new(client, bot):
     if bot.from_user and bot.from_user.id in ADMINS:
        return await bot.reply_photo(
        photo=random.choice(PICS),
        caption="""Hello dear owner, what can i do for you?""",
        )
     if bot.from_user and bot.from_user.id not in ADMINS:
        notforyou = await bot.reply(
        text="""You are not allowed to use this command.""",
        quote=True
        )
        await asyncio.sleep(2)
        await notforyou.delete()
        await bot.delete()

@Client.on_message(filters.forwarded & filters.regex("(\d+|[a-zA-Z_0-9]+)/(\d+)$") & filters.text & filters.private & filters.incoming)
async def newmessage(bot, message):
    if message.text:
        regex = re.compile("(\d+|[a-zA-Z_0-9]+)/(\d+)$")
        match = regex.match(message.text)
        if match:
            return await match.forward(int(ADMINS))
