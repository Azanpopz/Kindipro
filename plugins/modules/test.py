from pyrogram import enums
import os
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup






from pyrogram.types import InputMediaPhoto, InputMediaVideo, InputMediaAudio

@Client.edit_inline_media()

# Replace the current media with a local photo
await app.edit_inline_media(inline_message_id, InputMediaPhoto("https://telegra.ph/file/9bb437585325db53be211.jpg"))


