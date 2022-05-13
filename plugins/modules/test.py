from pyrogram import enums
import os
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup




@Client.send_poll(filters.command(["poll"]))

await client.send_poll(chat_id, "Is this a poll question?", ["Yes", "No", "Maybe"])
