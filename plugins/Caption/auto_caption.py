#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K & PR0FESS0R-99

import os
from caption_config import Config
from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait


import os , glob
from os import error
import logging
import pyrogram
import time
import math
from decouple import config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message, Sticker, Document




CAPTION_TEXT=Config.CAPTION
BUTTON_TEXT=Config.BUTTON_TEXT
URL_LINK=Config.URL_LINK
BT_TOKEN=Config.BT_TOKEN
ID=Config.ID
HASH=Config.HASH
BT_USERNAME=Config.BT_USERNAME





@Client.on_message(filters.command(["pings"]))
async def ping(bot, message):
    start_t = time.time()
    rm = await message.reply_text("Checking")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")




@Client.on_message(filters.media & filters.channel)
async def caption(client, message: Message):
    kopp, _ = get_file_id(message)
    await message.edit(f"<b>{kopp.file_name}</b>\n\n{CAPTION_TEXT}",
          reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(f"{BUTTON_TEXT}", url=f"{URL_LINK}")
              ]]
        ))

def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker"
        ):
            obj = getattr(msg, message_type)
            if obj:
                return obj, obj.file_id

