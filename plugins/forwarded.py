# short and repost forwarded message

from pyrogram import Client, filters
from config import CHANNEL_ID, FORWARD_MESSAGE, CHANNELS
import json
from utils import replace_mdisk_link, get_mdisk
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message
from pyrogram.types import MessageEntity
import ast
from pyrogram.types.list import List


# edit forwarded message

async def caption_ent(caption_entities):
    x = []
    string = str(caption_entities)
    res = ast.literal_eval(string)
    try:
        for i in res:
            print(i)

            if "url" in i:
                print("Url")
                x.append(
                    MessageEntity(type=i["type"], offset=i["offset"], length=i["length"], url=await get_mdisk(i["url"])))
            elif "user" in i:
                print("user")
                x.append(MessageEntity(type=i["type"], offset=i["offset"], length=i["length"], url=i["user"]))
            else:
                print("others")
                x.append(MessageEntity(type=i["type"], offset=i["offset"], length=i["length"]))
          
        entities = List(x)
        
    except:
        entities = caption_entities
        
    return entities


@Client.on_message(filters.chat(CHANNEL_ID) & (
        filters.channel | filters.group) & filters.incoming & ~filters.private & filters.forwarded)
async def channel_forward_link_handler(bot, message: Message):
    if FORWARD_MESSAGE and CHANNELS is True:

        # reply markup - button post

        if message.reply_markup:
            await message.delete()
            txt = message.text
            caption = message.caption
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
                await message.reply(text=txt, reply_markup=InlineKeyboardMarkup(buttsons))
            elif message.photo:
                txt = await replace_mdisk_link(caption)
                await message.reply_photo(photo=message.photo.file_id,
                                          caption=txt,
                                          reply_markup=InlineKeyboardMarkup(buttsons),
                                          )
            elif message.document:
                txt = await replace_mdisk_link(caption)
                await message.reply_document(document=message.document.file_id,
                                             caption=txt,
                                             reply_markup=InlineKeyboardMarkup(buttsons),
                                          )

        # For text messages

        elif message.text:
            text = message.text
            text = await replace_mdisk_link(text)
            await message.reply_text(text)
            await message.delete()

        # For media or document messages

        elif message.photo:  # for media messages
            fileid = message.photo.file_id
            text = message.caption
            link = await replace_mdisk_link(text)
            if link == text:
                print("The given link is either excluded domain link or a droplink link")
            else:
                await message.reply_photo(fileid, caption=link)
                await message.delete()

        elif message.document:  # for document messages
            fileid = message.document.file_id
            text = message.caption
            alias = ""
            link = await replace_mdisk_link(text)
            if link == text:
                print("The given link is either excluded domain link or a droplink link")
            else:
                await message.reply_document(fileid, caption=link)
                await message.delete()
