import asyncio
import base64
import urllib.parse
from info import ADMINS
from pyrogram import Client
import logging
from typing import Any, Optional
from pyrogram import filters
from Vars import Var
from utils import temp
from pyrogram.file_id import FileId
from urllib.parse import quote_plus
from database.ia_filterdb import unpack_new_file_id
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

def get_hash(media_msg: Message) -> str:
    media = get_media_from_message(media_msg)
    return getattr(media, "file_unique_id", "")[:6]

def get_name(media_msg: Message) -> str:
    media = get_media_from_message(media_msg)
    return getattr(media, "file_name", "")

class FIleNotFound(Exception):
    message = "File not found"

async def get_file_ids(client: Client, chat_id: int, message_id: int) -> Optional[FileId]:
    message = await client.get_messages(chat_id, message_id)
    if message.empty:
        raise FIleNotFound
    media = get_media_from_message(message)
    file_unique_id = await parse_file_unique_id(message)
    file_id = await parse_file_id(message)
    setattr(file_id, "file_size", getattr(media, "file_size", 0))
    setattr(file_id, "mime_type", getattr(media, "mime_type", ""))
    setattr(file_id, "file_name", getattr(media, "file_name", ""))
    setattr(file_id, "unique_id", file_unique_id)
    return file_id

def get_media_from_message(message: "Message") -> Any:
    media_types = (
        "audio",
        "document",
        "photo",
        "sticker",
        "animation",
        "video",
        "voice",
        "video_note",
    )
    for attr in media_types:
        media = getattr(message, attr, None)
        if media:
            return media
        
def get_file_id(message):
    media=message.document or message.audio or message.video
    return media.file_id

async def banned_users(_, client, message: Message):
    return (
        message.from_user is not None or not message.sender_chat
    ) and message.from_user.id in temp.BANNED_USERS

banned_user = filters.create(banned_users)

@Client.on_callback_query()
async def cb_data(bot, update):
    if update.data == "yes":
        await update.answer('File Deleted Successfully')
        media=random.choice(YES_PHOTO)
        newtext=f"User: **{update.from_user.mention(style='md')}** Track: **#u{update.chat.id}** Hash: **#{get_hash(log_msg)}{log_msg.message_id}** Link: **[Hold Me]({short_link})**"
        await update.edit_message_media(
        media=InputMediaPhoto(media=media, caption=YES_TEXT).format(newtext),
        )
    elif update.data == "no":
        await update.answer('Cancel file deleting process.')
        newtext=f"User: **{update.from_user.mention(style='md')}** Track: **#u{update.chat.id}** Hash: **#{get_hash(log_msg)}{log_msg.message_id}** Link: **[Hold Me]({short_link})**"
        await update.edit_text(
        text=NO_TEXT.format(newtext),
        reply_markup=NO_BUTTONS,
        )
    elif update.data == "delete":
        await update.answer('Do you really want to delete this file?')
        newtext=f"User: **{update.from_user.mention(style='md')}** Track: **#u{update.chat.id}** Hash: **#{get_hash(log_msg)}{log_msg.message_id}** Link: **[Hold Me]({short_link})**"
        await update.edit_text(
        text=DELETE_TEXT.format(newtext),
        reply_markup=DELETE_BUTTONS
        )
        
@Client.on_message( filters.private & ( filters.document | filters.video | filters.audio ) & ~banned_user, group=4,)
async def media_receive_handler(bot, message):
    
    banned_user = filters.create(banned_users)
    log_msg = await bot.copy_message(chat_id=Var.BIN_CHANNEL, from_chat_id=message.chat.id, message_id=message.message_id)
    stream_link = f"{Var.URL}{log_msg.message_id}/{quote_plus(get_name(message))}?hash={get_hash(log_msg)}"
    short_link = f"{Var.URL}{get_hash(log_msg)}{log_msg.message_id}"
    logging.info(f"Generated link: {stream_link} for {message.from_user.first_name}")
    newtext=f"User: **{message.from_user.mention(style='md')}** Track: **#u{message.chat.id}** Hash: **#{get_hash(log_msg)}{log_msg.message_id}** Link: **[Hold Me]({short_link})**"
    
    await message.reply_text(
        text=f"<b>🤓 I generated link for you, <a href={short_link}>Hold me to copy.</a> Just reply the file with /link to generate an extra link.</b>",
        quote=True,
        parse_mode="html", 
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('🧩 Share link', url=f'https://t.me/share/url?url={short_link}')
                    ]
                ]
            )
        )
    
    await log_msg.edit_text(
        text=f"{newtext}",
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('🗑 Delete File', callback_data='close')
                    ]
                ]
            )
        )
    
