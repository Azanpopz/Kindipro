# (©)𝙐𝙁𝙎 𝘽𝙤𝙩𝙯

import base64
import re
import asyncio
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.errors import FloodWait
from pyrogram.types.messages_and_media import message


async def encode(string):
    string_bytes = string.encode("ascii")
    base64_bytes = base64.b64encode(string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string


async def decode(base64_string):
    base64_bytes = base64_string.encode("ascii")
    string_bytes = base64.b64decode(base64_bytes) 
    string = string_bytes.decode("ascii")
    return string


async def get_messages(client, message_id, channel_id):
    messages = []
    total_messages = 0
    while total_messages != len(message_id):
        temb_ids = message_id[total_messages:total_messages+200]
        # for id in message_id:
        try:
            msgs = await client.get_messages(
                chat_id=channel_id,
                message_ids=temb_ids
            )
        except FloodWait as e:
            await asyncio.sleep(e.x)
            msgs = await client.get_messages(
                chat_id=channel_id,
                message_ids=temb_ids
            )
        except:
            pass
        total_messages += len(temb_ids)
        messages.extend(msgs)
    return messages


async def get_message_id(client, message, fwd_channel_id):
    if message.forward_from_chat:
        if message.forward_from_chat.id == fwd_channel_id:
            return message.forward_from_message_id
        else:
            return 0
    elif message.via_bot:
        return message.id
    elif message.forward_sender_name:
        return 0
    elif message.text:
        pattern = "https://t.me/(?:c/)?(.*)/(\d+)"
        matches = re.match(pattern, message.text)
        if not matches:
            return 0
        channel_id = matches.group(1)
        msg_id = int(matches.group(2))
        if channel_id.isdigit():
            if f"-100{channel_id}" == str(fwd_channel_id):
                return msg_id
        else:
            if channel_id == client.db_channel.username:
                return msg_id
    else:
        return 0


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
                setattr(obj, "message_type", message_type)
                return obj


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + " Dᴀʏs, ") if days else "")
        + ((str(hours) + " Hᴏᴜʀs, ") if hours else "")
        + ((str(minutes) + " Mɪɴᴜᴛᴇs, ") if minutes else "")
        + ((str(seconds) + " Sᴇᴄᴏɴᴅs, ") if seconds else "")
        + ((str(milliseconds) + " Mɪʟʟɪsᴇᴄᴏɴᴅs, ") if milliseconds else "")
    )
    return tmp[:-2]


# class CustomFilters(object):
#     class _Supporters(BaseFilter):
#         def filter(self, message: Message):
#             return bool(message.from_user and message.from_user.id in SUPPORT_USERS)
#
#     support_filter = _Supporters()
#
#     class _Sudoers(BaseFilter):
#         def filter(self, message: Message):
#             return bool(message.from_user and message.from_user.id in SUDO_USERS)
#
#     sudo_filter = _Sudoers()
#
#     class _MimeType(BaseFilter):
#         def __init__(self, mimetype):
#             self.mime_type = mimetype
#             self.name = "CustomFilters.mime_type({})".format(self.mime_type)
#
#         def filter(self, message: Message):
#             return bool(message.document and message.document.mime_type == self.mime_type)
#
#     mime_type = _MimeType
#
#     class _HasText(BaseFilter):
#         def filter(self, message: Message):
#             return bool(message.text or message.sticker or message.photo or message.document or message.video)
#
#     has_text = _HasText()
