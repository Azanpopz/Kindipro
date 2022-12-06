import asyncio
import os
import time
import aiohttp
import logging
import requests
import traceback
import pyperclip

from gtts import gTTS
from io import BytesIO
from typing import List, Dict
from googletrans import Translator
from pyrogram import Client, filters, enums
from asyncio import get_running_loop
from info import IMDB_TEMPLATE, SHORT_LINK_API_KEY
from utils import extract_user, get_file_id, get_poster, last_online
from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, MediaEmpty, PhotoInvalidDimensions, \
    WebpageMediaEmpty

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


@Client.on_message(filters.command('id'))
async def showid(client, message):
    chat_type = message.chat.type
    if chat_type.name == enums.ChatType.PRIVATE:
        user_id = message.chat.id
        first = message.from_user.first_name
        last = message.from_user.last_name or ""
        username = message.from_user.username
        dc_id = message.from_user.dc_id or ""
        await message.reply_text(
            f"<b>➲ First Name:</b> {first}\n<b>➲ Last Name:</b> {last}\n<b>➲ Username:</b> {username}\n<b>➲ Telegram ID:</b> <code>{user_id}</code>\n<b>➲ Data Centre:</b> <code>{dc_id}</code>",
            quote=True
        )

    elif chat_type.name in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        _id = ""
        _id += (
            "<b>➲ Chat ID</b>: "
            f"<code>{message.chat.id}</code>\n"
        )
        if message.reply_to_message:
            _id += (
                "<b>➲ User ID</b>: "
                f"<code>{message.from_user.id if message.from_user else 'Anonymous'}</code>\n"
                "<b>➲ Replied User ID</b>: "
                f"<code>{message.reply_to_message.from_user.id if message.reply_to_message.from_user else 'Anonymous'}</code>\n"
            )
            file_info = get_file_id(message.reply_to_message)
        else:
            _id += (
                "<b>➲ User ID</b>: "
                f"<code>{message.from_user.id if message.from_user else 'Anonymous'}</code>\n"
            )
            file_info = get_file_id(message)
        if file_info:
            _id += (
                f"<b>{file_info.message_type}</b>: "
                f"<code>{file_info.file_id}</code>\n"
            )
        await message.reply_text(
            _id,
            quote=True
        )


@Client.on_message(filters.command(["info"]))
async def who_is(client, message):
    # https://github.com/SpEcHiDe/PyroGramBot/blob/master/pyrobot/plugins/admemes/whois.py#L19
    status_message = await message.reply_text(
        "`Fetching user info...`"
    )
    await status_message.edit(
        "`Processing user info...`"
    )
    from_user = None
    from_user_id, _ = extract_user(message)
    try:
        from_user = await client.get_users(from_user_id)
    except Exception as error:
        await status_message.edit(str(error))
        return
    if from_user is None:
        return await status_message.edit("no valid user_id / message specified")
    message_out_str = ""
    message_out_str += f"<b>➲First Name:</b> {from_user.first_name}\n"
    last_name = from_user.last_name or "<b>None</b>"
    message_out_str += f"<b>➲Last Name:</b> {last_name}\n"
    message_out_str += f"<b>➲Telegram ID:</b> <code>{from_user.id}</code>\n"
    username = from_user.username or "<b>None</b>"
    dc_id = from_user.dc_id or "[User Doesnt Have A Valid DP]"
    message_out_str += f"<b>➲Data Centre:</b> <code>{dc_id}</code>\n"
    message_out_str += f"<b>➲User Name:</b> @{username}\n"
    message_out_str += f"<b>➲User 𝖫𝗂𝗇𝗄:</b> <a href='tg://user?id={from_user.id}'><b>Click Here</b></a>\n"
    if message.chat.type in (enums.ChatType.SUPERGROUP, enums.ChatType.CHANNEL):
        try:
            chat_member_p = await message.chat.get_member(from_user.id)
            joined_date = datetime.fromtimestamp(
                chat_member_p.joined_date or time.time()
            ).strftime("%Y.%m.%d %H:%M:%S")
            message_out_str += (
                "<b>➲Joined this Chat on:</b> <code>"
                f"{joined_date}"
                "</code>\n"
            )
        except UserNotParticipant:
            pass
    chat_photo = from_user.photo
    if chat_photo:
        local_user_photo = await client.download_media(
            message=chat_photo.big_file_id
        )
        buttons = [[
            InlineKeyboardButton('🔐 Close', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=local_user_photo,
            quote=True,
            reply_markup=reply_markup,
            caption=message_out_str,
            disable_notification=True
        )
        os.remove(local_user_photo)
    else:
        buttons = [[
            InlineKeyboardButton('🔐 Close', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(
            text=message_out_str,
            reply_markup=reply_markup,
            quote=True,
            disable_notification=True
        )
    await status_message.delete()


@Client.on_message(filters.command(["imdb", 'search']))
async def imdb_search(client, message):
    if ' ' in message.text:
        k = await message.reply('Searching ImDB')
        r, title = message.text.split(None, 1)
        movies = await get_poster(title, bulk=True)
        if not movies:
            return await message.reply("No results Found")
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{movie.get('title')} - {movie.get('year')}",
                    callback_data=f"imdb#{movie.movieID}",
                )
            ]
            for movie in movies
        ]
        await k.edit('Here is what i found on IMDb', reply_markup=InlineKeyboardMarkup(btn))
    else:
        await message.reply('Give me a movie / series Name')


# @Client.on_callback_query(filters.regex('^imdb'))
# async def imdb_callback(bot: Client, query: CallbackQuery):
#     i, movie = query.data.split('#')
#     imdb = await get_poster(query=movie, id=True)
#     btn = [
#         [
#             InlineKeyboardButton(
#                 text=f"{imdb.get('title')}",
#                 url=imdb['url'],
#             )
#         ]
#     ]
#     if imdb:
#         caption = IMDB_TEMPLATE.format(
#             query=imdb['title'],
#             title=imdb['title'],
#             votes=imdb['votes'],
#             aka=imdb["aka"],
#             seasons=imdb["seasons"],
#             box_office=imdb['box_office'],
#             localized_title=imdb['localized_title'],
#             kind=imdb['kind'],
#             imdb_id=imdb["imdb_id"],
#             cast=imdb["cast"],
#             runtime=imdb["runtime"],
#             countries=imdb["countries"],
#             certificates=imdb["certificates"],
#             languages=imdb["languages"],
#             director=imdb["director"],
#             writer=imdb["writer"],
#             producer=imdb["producer"],
#             composer=imdb["composer"],
#             cinematographer=imdb["cinematographer"],
#             music_team=imdb["music_team"],
#             distributors=imdb["distributors"],
#             release_date=imdb['release_date'],
#             year=imdb['year'],
#             genres=imdb['genres'],
#             poster=imdb['poster'],
#             plot=imdb['plot'],
#             rating=imdb['rating'],
#             url=imdb['url'],
#             **locals()
#         )
#     else:
#         caption = "No Results"
#     if imdb.get('poster'):
#         try:
#             await query.message.reply_photo(photo=imdb['poster'], caption=caption,
#                                             reply_markup=InlineKeyboardMarkup(btn))
#         except (MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty):
#             pic = imdb.get('poster')
#             poster = pic.replace('.jpg', "._V1_UX360.jpg")
#             await query.message.reply_photo(photo=imdb['poster'], caption=caption,
#                                             reply_markup=InlineKeyboardMarkup(btn))
#         except Exception as e:
#             logger.exception(e)
#             await query.message.reply(caption, reply_markup=InlineKeyboardMarkup(btn), disable_web_page_preview=False)
#         await query.message.delete()
#     else:
#         await query.message.edit(caption, reply_markup=InlineKeyboardMarkup(btn), disable_web_page_preview=False)
#     await query.answer()


@Client.on_message(filters.command(["speech"]))
async def text_to_speech(_, message):
    if not message.reply_to_message:
        return await message.reply_text("💡 Reply To Some Texts !")
    if not message.reply_to_message.text:
        return await message.reply_text("💡 Reply To Some Texts !")
    m = await message.reply_text("Processing...😌")
    text = message.reply_to_message.text
    try:
        loop = get_running_loop()
        audio = await loop.run_in_executor(None, convert, text)
        await message.reply_audio(audio)
        await m.delete()
        audio.close()
    except Exception as e:
        await m.edit(str(e))
        es = traceback.format_exc()
        print(es)


@Client.on_message(filters.command(["tr"]))
async def lang_translate(client, message):
    if message.reply_to_message:
        try:
            lgcd = message.text.split("/tr")
            lg_cd = lgcd[1].lower().replace(" ", "")
            tr_text = message.reply_to_message.text
            translator = Translator()
            translation = translator.translate(tr_text, dest=lg_cd)
            hehek = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Lᴀɴɢᴜᴀɢᴇ Cᴏᴅᴇs", url="https://cloud.google.com/translate/docs/languages"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "✗ Cʟᴏsᴇ Tʜɪs Tʀᴀɴsʟᴀᴛᴇ ✗", callback_data="close_data"
                        )
                    ],
                ]
            )
            try:
                for i in list:
                    if list[i] == translation.src:
                        fromt = i
                    if list[i] == translation.dest:
                        to = i
                await message.reply_text(
                    f"Translated From **{fromt.capitalize()}** To **{to.capitalize()}**\n\n```{translation.text}```",
                    reply_markup=hehek, quote=True)
            except:
                await message.reply_text(
                    f"Translated from **{translation.src}** To **{translation.dest}**\n\n```{translation.text}```",
                    reply_markup=hehek, quote=True)


        except:
            print("error")
    else:
        ms = await message.reply_text("You Can Use This Command By using Reply To Message.\n\nEx:- /tr ml")
        await asyncio.sleep(3)
        await ms.delete()


@Client.on_message(filters.command("paste"))
async def paste_func(_, message):
    global content
    if not message.reply_to_message:
        return await message.reply("Reply To A Message With /paste")
    r = message.reply_to_message

    if not r.text and not r.document:
        return await message.reply("Only Text And Documents Are Supported.")

    m = await message.reply("Pasting...")
    await asyncio.sleep(1)

    # if r.text:
    #     content = r.text
    # elif r.document:
    #     p_file = await r.download()
    #     content = open(p_file, "r").read()
    #     os.remove(p_file)

    # link, rawlink = await paste(content)
    # s_link, s_rawlink = await spaste(content)
    # kb = InlineKeyboardMarkup(
    #     [[InlineKeyboardButton("PasteBin", url=link), InlineKeyboardButton("SpaceBin", url=s_link)]])
    # await message.reply_text(
    #     f"**Pasted!**\nPasteBin: [Here]({rawlink})\nSpaceBin: [Here]({s_rawlink})",
    #     quote=True,
    #     reply_markup=kb,
    # )
    # await message.reply_text(
    #     f"**Pasted!**\n{pyperclip.paste()}",
    #     quote=True,
    # )
    logging.info(pyperclip.paste())
    await message.reply_text(
        f"{pyperclip.paste()}"
    )
    await m.delete()


@Client.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    try:
        short_link = await get_shortlink(link)
        await message.reply(f'Here Is Your [Short Link] 👉🏻 {short_link}', quote=True)
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)


async def get_shortlink(link):
    url = 'https://gplinks.in/api'
    params = {'api': SHORT_LINK_API_KEY, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]


def convert(text):
    audio = BytesIO()
    i = Translator().translate(text, dest="en")
    lang = i.src
    tts = gTTS(text, lang=lang)
    audio.name = lang + ".ogg"
    tts.write_to_fp(audio)
    return audio


async def spaste(content: str):
    siteurl = "https://spaceb.in/api/v1/documents/"
    try:
        resp = requests.post(siteurl, data={"content": content, "extension": "py"})
        response = resp.json()
        link = f"https://spaceb.in/{response['payload']['id']}"
        rawlink = f"{siteurl}{response['payload']['id']}/raw"

        # useragent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        #              'Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62'
        #              )
        # header = {
        #     "User-Agent": useragent,
        # }
        # t_resp = requests.get(rawlink, headers=header)
        # t_response = t_resp.json()
        return link, rawlink
    except Exception as e:
        print(e)
        return None


def paginate_modules(page_n: int, module_dict: Dict, prefix, chat=None) -> List:
    if not chat:
        modules = sorted(
            [EqInlineKeyboardButton(x.__mod_name__,
                                    callback_data="{}_module({})".format(prefix, x.__mod_name__.lower())) for x
             in module_dict.values()])
    else:
        modules = sorted(
            [EqInlineKeyboardButton(x.__mod_name__,
                                    callback_data="{}_module({},{})".format(prefix, chat, x.__mod_name__.lower())) for x
             in module_dict.values()])

    pairs = [modules[i * 3: (i + 1) * 3] for i in range((len(modules) + 3 - 1) // 3)]
    round_num = len(modules) / 3
    calc = len(modules) - round(round_num)
    if calc == 1:
        pairs.append((modules[-1],))
    elif calc == 2:
        pairs.append((modules[-1],))

    return pairs


class EqInlineKeyboardButton(InlineKeyboardButton):
    def __eq__(self, other):
        return self.text == other.text

    def __lt__(self, other):
        return self.text < other.text

    def __gt__(self, other):
        return self.text > other.text


__help__ = """
 - /id: Get Your ID And Some Details
        (In Private, User Details & In Group Group Id, In Group, Reply To Message, Get User Details).
 - /info: Get User Information In Detail.
 - /imdb or /search <Movie Name>: Get Your Movie Information.
 - /speech: Convert Your Text Message To Voice Note.
 - /tr <Language Code>: Translate Text Message To Given Language Code.
 - /paste: Pasting Your Copied Text.
"""

__mod_name__ = "Misc"
