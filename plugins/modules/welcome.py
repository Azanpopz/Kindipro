import os 
from os import error
import logging
import pyrogram
import time
from decouple import config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message, Sticker, Document, ChatMember

Munnipopz = Client(
    "Member-Sticker-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

HELP = """
● Still Wonder How I Work ? 
● Use /How get a Full Brief
● Use /Donate to Donate
"""
START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ABOUT', url='https://t.me/nasrani_update'),
        InlineKeyboardButton('HELP', url='https://t.me/nasrani_update')
        ],
        [
        InlineKeyboardButton('↗ Join Here ↗', url='https://t.me/nasrani_update'),
        ],
        [InlineKeyboardButton('↗ ADD ME TO A GROUP ↗', url="https://t.me/nasrani_update")
        ]]
        
    )

@Client.on_message(filters.new_chat_members & filters.group)
async def sticker_group(bot, message):
   try:
      reply_markup = START_BUTTON
      chat_id = int(message.chat.id)
      count = await bot.get_chat_members_count(chat_id)
      await bot.message_text(
          text=HELP,
          reply_markup=reply_markup,
          quote=True
      )
          
          
