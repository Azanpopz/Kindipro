from pyrogram import enums
import os
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup




@Client.send_poll(filters.command(["poll"]))

await app.send_poll(
chat_id=chat_id
poll=f"Is this a poll question?", ["Yes", "No", "Maybe"])
