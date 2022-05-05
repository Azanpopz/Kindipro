import logging
from pyrogram import Client, emoji, filters
from pyrogram.errors.exceptions.bad_request_400 import QueryIdInvalid
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultCachedDocument, InlineQuery
from database.ia_filterdb import get_search_results
from utils import is_subscribed, get_size, temp
from info import CACHE_TIME, AUTH_USERS, AUTH_CHANNEL, CUSTOM_FILE_CAPTION
import os
import play_scraper
from pyrogram import Client, filters
from pyrogram.types import *

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
    results = play_scraper.search(update.query)
    answers = []
    for result in results:
        details = "**Title:** `{}`".format(result["title"]) + "\n" \
        "**Description:** `{}`".format(result["description"]) + "\n" \
        "**App ID:** `{}`".format(result["app_id"]) + "\n" \
        "**Developer:** `{}`".format(result["developer"]) + "\n" \
        "**Developer ID:** `{}`".format(result["developer_id"]) + "\n" \
        "**Score:** `{}`".format(result["score"]) + "\n" \
        "**Price:** `{}`".format(result["price"]) + "\n" \
        "**Full Price:** `{}`".format(result["full_price"]) + "\n" \
        "**Free:** `{}`".format(result["free"]) + "\n" \
        "\n" + "Made by @FayasNoushad"
        reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Play Store", url="https://play.google.com"+result["url"])]]
        )
        try:
            answers.append(
                InlineQueryResultArticle(
                    title=result["title"],
                    description=result.get("description", None),
                    thumb_url=result.get("icon", None),
                    input_message_content=InputTextMessageContent(
                        message_text=details, disable_web_page_preview=True
                    ),
                    reply_markup=reply_markup
                )
            )
        except Exception as error:
            print(error)
    await query.answer(answers)
   
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
            InlineKeyboardButton('Search again', url="https://play.google.com"+result["url"])
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



