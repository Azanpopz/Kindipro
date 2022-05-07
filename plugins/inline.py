import logging
from pyrogram import Client, emoji, filters
from pyrogram.errors.exceptions.bad_request_400 import QueryIdInvalid
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultCachedDocument, InlineQuery, Message
from database.ia_filterdb import get_search_results
from utils import is_subscribed, get_size, temp
from info import CACHE_TIME, AUTH_USERS, AUTH_CHANNEL, CUSTOM_FILE_CAPTION

import asyncio
from pyrogram import Client, filters
from pyrogram.errors import QueryIdInvalid, FloodWait
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, InlineQuery, InlineQueryResultArticle, \
    InputTextMessageContent

from configs import Config
from tool import SearchYTS, SearchAnime, Search1337x, SearchPirateBay



logger = logging.getLogger(__name__)
cache_time = 0 if AUTH_USERS or AUTH_CHANNEL else CACHE_TIME

async def inline_users(query: InlineQuery):
    if AUTH_USERS:
        if query.from_user and query.from_user.id in AUTH_USERS:
            return True
        else:
            return False
    if query.from_user and query.from_user.id not in temp.BANNED_USERS:
        return True
    return False


@Client.on_inline_query()
async def answer(bot, query):
    """Show search results for given inline query"""
    
   
    if not await inline_users(query):
        await query.answer(results=[],
                           cache_time=0,
                           switch_pm_text='okDa',
                           switch_pm_parameter="hehe")
        return

    if AUTH_CHANNEL and not await is_subscribed(bot, query):
        await query.answer(results=[],
                           cache_time=0,
                           switch_pm_text='You have to subscribe my channel to use the bot',
                           switch_pm_parameter="subscribe")
        return

    results = []
    if '|' in query.query:
        string, file_type = query.query.split('|', maxsplit=1)
        string = string.strip()
        file_type = file_type.strip().lower()
    else:
        string = query.query.strip()
        file_type = None

    offset = int(query.offset or 0)
    reply_markup = get_reply_markup(query=string)
    files, next_offset, total = await get_search_results(string,
                                                  file_type=file_type,
                                                  max_results=10,
                                                  offset=offset)

    for file in files:
        title=file.file_name
        size=get_size(file.file_size)
        f_caption=file.caption
        if CUSTOM_FILE_CAPTION:
            try:
                f_caption=CUSTOM_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='' if f_caption is None else f_caption)
            except Exception as e:
                logger.exception(e)
                f_caption=f_caption
        if f_caption is None:
            f_caption = f"{file.file_name}"
        results.append(
            InlineQueryResultCachedDocument(
                title=file.file_name,
                file_id=file.file_id,
                caption=f_caption,
                description=f'Size: {get_size(file.file_size)}\nType: {file.file_type}',
                reply_markup=reply_markup))

    if results:
        switch_pm_text = f"{emoji.FILE_FOLDER} Results - {total}"
        if string:
            switch_pm_text += f" for {string}"
        try:
            await query.answer(results=results,
                           is_personal = True,
                           cache_time=cache_time,
                           switch_pm_text=switch_pm_text,
                           switch_pm_parameter="start",
                           next_offset=str(next_offset))
        except QueryIdInvalid:
            pass
        except Exception as e:
            logging.exception(str(e))
    else:
        switch_pm_text = f'{emoji.CROSS_MARK} No results'
        if string:
            switch_pm_text += f' for "{string}"'

        await query.answer(results=[],
                           is_personal = True,
                           cache_time=cache_time,
                           switch_pm_text=switch_pm_text,
                           switch_pm_parameter="okay")


def get_reply_markup(query):
    buttons = [
        [
            InlineKeyboardButton('Search again', url="https://play.google.com")
        ]
        ]
    return InlineKeyboardMarkup(buttons)



async def inline_users(query: InlineQuery):
    if AUTH_USERS:
        if query.from_user and query.from_user.id in AUTH_USERS:
            return True
        else:
            return False
    if query.from_user and query.from_user.id not in temp.BANNED_USERS:
        return True
    return False


    elif search_ts.startswith("YTS"):
        query = search_ts.split(" ", 1)[-1]
        if (query == "") or (query == " "):
            answers.append(
                InlineQueryResultArticle(
                    title="YTS [text]",
                    description="𝐓𝐲𝐩𝐞 𝐭𝐡𝐞 𝐌𝐨𝐯𝐢𝐞 𝐍𝐚𝐦𝐞 ⚡️",
                    input_message_content=InputTextMessageContent(
                        message_text="`YTS [text]`\n\n𝗦𝗲𝗮𝗿𝗰𝗵 𝗬𝗧𝗦 𝗠𝗼𝘃𝗶𝗲𝘀 🥰🔥",
                        parse_mode="Markdown"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("𝗦𝗲𝗮𝗿𝗰𝗵 𝗔𝗴𝗮𝗶𝗻 🌶✨", switch_inline_query_current_chat="YTS ")]])
                )
            )
        else:
            torrentList = await SearchYTS(query)
            if not torrentList:
                answers.append(
                    InlineQueryResultArticle(
                        title="𝗡𝗼 𝗧𝗼𝗿𝗿𝗲𝗻𝘁𝘀 𝗙𝗼𝘂𝗻𝗱 🥺",
                        description=f"𝐍𝐨 𝐑𝐞𝐬𝐮𝐥𝐭𝐬 🥺 {query} !!",
                        input_message_content=InputTextMessageContent(
                            message_text=f"No YTS Torrents Found For `{query}`",
                            parse_mode="Markdown"
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("Try Again", switch_inline_query_current_chat="YTS ")]])
                    )
                )
            else:
                for i in range(len(torrentList)):
                    dl_links = "- " + "\n\n- ".join(torrentList[i]['Downloads'])
                    answers.append(
                        InlineQueryResultArticle(
                            title=f"{torrentList[i]['Name']}",
                            description=f"Language: {torrentList[i]['Language']}\nLikes: {torrentList[i]['Likes']}, Rating: {torrentList[i]['Rating']}",
                            input_message_content=InputTextMessageContent(
                                message_text=f"𝗚𝗲𝗻𝗿𝗲 🔥:** `{torrentList[i]['Genre']}`\n\n"
                                             f"𝗡𝗮𝗺𝗲 🌺:** `{torrentList[i]['Name']}`\n\n"
                                             f"𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲 ☘️:** `{torrentList[i]['Language']}`\n\n"
                                             f"𝗟𝗶𝗸𝗲𝘀 ❤️:** `{torrentList[i]['Likes']}`\n\n"
                                             f"𝗥𝗮𝘁𝗶𝗻𝗴𝘀 ⭐️:** `{torrentList[i]['Rating']}`\n\n"
                                             f"𝗗𝘂𝗿𝗮𝘁𝗶𝗼𝗻 🌶:** `{torrentList[i]['Runtime']}`\n\n"
                                             f"𝗥𝗲𝗹𝗲𝗮𝘀𝗲𝗱 𝗼𝗻 🥺🔥 {torrentList[i]['ReleaseDate']}**\n\n\n"
                                             f"𝗧𝗼𝗿𝗿𝗲𝗻𝘁 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗟𝗶𝗻𝗸𝘀 🥭🥰✨:**\n{dl_links}\n\n 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 @Ravindu_Deshanz\n\n@PantherzBot 🥰🌷",
                                parse_mode="Markdown",
                                disable_web_page_preview=True
                            ),
                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝗦𝗲𝗮𝗿𝗰𝗵 𝗔𝗴𝗮𝗶𝗻 🌶✨", switch_inline_query_current_chat="YTS ")]]),
                            thumb_url=torrentList[i]["Poster"]
                        )
                    )
    elif search_ts.startswith("!a"):
        query = search_ts.split(" ", 1)[-1]
        if (query == "") or (query == " "):
            answers.append(
                InlineQueryResultArticle(
                    title="!a [text]",
                    description="Search For Torrents for Anime ...",
                    input_message_content=InputTextMessageContent(
                        message_text="`!a [text]`\n\nSearch Anime Torrents from Inline!",
                        parse_mode="Markdown"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("🔍Search Again", switch_inline_query_current_chat="!a ")]])
                )
            )
        else:
            torrentList = await SearchAnime(query)
            if not torrentList:
                answers.append(
                    InlineQueryResultArticle(
                        title="No Anime Torrents Found!",
                        description=f"Can't find Anime torrents for {query} !!",
                        input_message_content=InputTextMessageContent(
                            message_text=f"No Anime Torrents Found For `{query}`",
                            parse_mode="Markdown"
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("Try Again", switch_inline_query_current_chat="!a ")]])
                    )
                )
            else:
                for i in range(len(torrentList)):
                    answers.append(
                        InlineQueryResultArticle(
                            title=f"{torrentList[i]['Name']}",
                            description=f"Seeders: {torrentList[i]['Seeder']}, Leechers: {torrentList[i]['Leecher']}\nSize: {torrentList[i]['Size']}",
                            input_message_content=InputTextMessageContent(
                                message_text=f"𝗧𝗼𝗿𝗿𝗲𝗻𝘁 𝗖𝗮𝘁𝗲𝗴𝗼𝗿𝘆 🌷:** `{torrentList[i]['Category']}`\n"
                                             f"𝗡𝗮𝗺𝗲 🌺:** `{torrentList[i]['Name']}`\n\n"
                                             f"𝗦𝗶𝘇𝗲 🥭:** `{torrentList[i]['Size']}`\n\n"
                                             f"𝗦𝗲𝗲𝗱𝗲𝗿𝘀 ✨:** `{torrentList[i]['Seeders']}`\n\n"
                                             f"𝗟𝗲𝗲𝗰𝗵𝗲𝗿𝘀 ⭐️:** `{torrentList[i]['Leechers']}`\n\n"
                                             f"𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗿 🎃:** `{torrentList[i]['Uploader']}`\n"
                                             f"𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗱 📅 :** {torrentList[i]['Date']}**\n\n\n"
                                             f"𝗠𝗮𝗴𝗲𝘁 🧲:**\n`{torrentList[i]['Magnet']}`\n\n 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 @Ravindu_Deshanz\n\n@PantherzBot 🥰🌷  ",
                                parse_mode="Markdown"
                            ),
                            reply_markup=InlineKeyboardMarkup(
                                [[InlineKeyboardButton("𝗦𝗲𝗮𝗿𝗰𝗵 𝗔𝗴𝗮𝗶𝗻 🌶✨", switch_inline_query_current_chat="!a ")]]
                            )
                        )
                    )
    else:
        torrentList = await Search1337x(search_ts)
        if not torrentList:
            answers.append(
                InlineQueryResultArticle(
                    title="No Torrents Found!",
                    description=f"Can't find torrents for {search_ts} !!",
                    input_message_content=InputTextMessageContent(
                        message_text=f"No Torrents Found For `{search_ts}`",
                        parse_mode="Markdown"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Try Again", switch_inline_query_current_chat="")]])
                )
            )
        else:
            for i in range(len(torrentList)):
                answers.append(
                    InlineQueryResultArticle(
                        title=f"{torrentList[i]['Name']}",
                        description=f"Seeders: {torrentList[i]['Seeders']}, Leechers: {torrentList[i]['Leechers']}\nSize: {torrentList[i]['Size']}, Downloads: {torrentList[i]['Downloads']}",
                        input_message_content=InputTextMessageContent(
                            message_text=f"𝗧𝗼𝗿𝗿𝗲𝗻𝘁 𝗖𝗮𝘁𝗲𝗴𝗼𝗿𝘆 🌷:** `{torrentList[i]['Category']}`\n\n"
                                         f"𝗡𝗮𝗺𝗲 🌺 `{torrentList[i]['Name']}`\n\n"
                                         f"Language:** `{torrentList[i]['Language']}`\n\n"
                                         f"𝗦𝗲𝗲𝗱𝗲𝗿𝘀 ✨:** `{torrentList[i]['Seeders']}`\n\n"
                                         f"𝗟𝗲𝗲𝗰𝗵𝗲𝗿𝘀 ⭐️:** `{torrentList[i]['Leechers']}`\n\n"
                                         f"𝗦𝗶𝘇𝗲 🥭:** `{torrentList[i]['Size']}`\n\n"
                                         f"Downloads:** `{torrentList[i]['Downloads']}`\n\n"
                                         f"𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗿 🎃 {torrentList[i]['UploadedBy']}__\n\n"
                                         f"𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗱 📅 {torrentList[i]['DateUploaded']}__\n\n\n"
                                         f"𝗠𝗮𝗴𝗲𝘁 🧲:**\n`{torrentList[i]['Magnet']}`\n\n𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 @Ravindu_Deshanz\n\n@PantherzBot 🥰🌷",
                            parse_mode="Markdown"
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("𝗦𝗲𝗮𝗿𝗰𝗵 𝗔𝗴𝗮𝗶𝗻 🌶✨", switch_inline_query_current_chat="")]]
                        ),
                        thumb_url=torrentList[i]['Poster']
                    )
                )
    try:
        await inline.answer(
            results=answers,
            cache_time=0
        )
        print(f"[{Config.SESSION_NAME}] - Answered Successfully - {inline.from_user.first_name}")
    except QueryIdInvalid:
        print(f"[{Config.SESSION_NAME}] - Failed to Answer - {inline.from_user.first_name} - Sleeping for 5s")
        await asyncio.sleep(5)
        try:
            await inline.answer(
                results=answers,
                cache_time=0,
                switch_pm_text="Error: Search timed out!",
                switch_pm_parameter="start",
            )
        except QueryIdInvalid:
            print(f"[{Config.SESSION_NAME}] - Failed to Answer Error - {inline.from_user.first_name} - Sleeping for 5s")
            await asyncio.sleep(5)
