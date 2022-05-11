import json
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from config import CHANNEL_ID, CHANNELS
from pyrogram import Client, filters
from utils import replace_mdisk_link, caption

import re


# Channel


@Client.on_message(filters.chat(CHANNEL_ID) & (
        filters.channel | filters.group) & filters.incoming & ~filters.edited & ~filters.private &
                   ~filters.forwarded)
async def channel_link_handler(bot, message: Message):
    if CHANNELS is True:

        if message.text:
            txt = message.text
            ent = await caption(message.entities)
            print(ent)
        elif message.caption:
            txt = message.caption
            ent = await caption(message.caption_entities)

            # reply markup - button post

        if message.reply_markup:
            reply_markup = json.loads(str(message.reply_markup))
            buttsons = []
            for i, markup in enumerate(reply_markup["inline_keyboard"]):
                buttons = []
                for j in markup:
                    text = j["text"]
                    url = j["url"]
                    url = await replace_mdisk_link(url)
                    button = InlineKeyboardButton(text, url=url)
                    buttons.append(button)
                buttsons.append(buttons)

            if message.text:
                txt = await replace_mdisk_link(txt)
                await message.edit(text=txt,
                                   reply_markup=InlineKeyboardMarkup(buttsons),
                                   entities=ent)
            elif message.caption:
                txt = await replace_mdisk_link(message.caption)
                if message.photo:
                    await message.edit_caption(caption=txt,
                                               reply_markup=InlineKeyboardMarkup(buttsons),
                                               caption_entities=ent)
                elif message.document:
                    await message.edit_caption(caption=txt,
                                               reply_markup=InlineKeyboardMarkup(buttsons),
                                               caption_entities=ent)
        # For text messages

        elif message.text:
            text = message.text
            text = await replace_mdisk_link(text)
            await message.edit_text(text, entities=ent)

        # For media or document messages

        elif message.media or message.document:
            text = message.caption
            link = await replace_mdisk_link(text)
            if link == text:
                print("The given link is either excluded domain link or a droplink link")
            else:
                await message.edit_caption(link, caption_entities=ent)
