# (c) @KoshikKumar17
import os
import math
import json
import time
import shutil
import heroku3
import requests
from pyrogram import filters
from pyrogram import Client as Koshik
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from info import HEROKU_API_KEY, BT_STRT_TM
from utils import humanbytes

@Koshik.on_message((filters.private | filters.group) & filters.command('botstatus'))
async def bot_dyno_status(client,message):
    px = await message.reply_text("**Fetching Bot Status...✨**")
    if HEROKU_API_KEY:
        try:
            server = heroku3.from_key(HEROKU_API_KEY)

            user_agent = (
                'Mozilla/5.0 (Linux; Android 10; SM-G975F) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/80.0.3987.149 Mobile Safari/537.36'
            )
            accountid = server.account().id
            headers = {
            'User-Agent': user_agent,
            'Authorization': f'Bearer {HEROKU_API_KEY}',
            'Accept': 'application/vnd.heroku+json; version=3.account-quotas',
            }

            path = "/accounts/" + accountid + "/actions/get-quota"

            request = requests.get("https://api.heroku.com" + path, headers=headers)

            if request.status_code == 200:
                result = request.json()

                total_quota = result['account_quota']
                quota_used = result['quota_used']

                quota_left = total_quota - quota_used
                
                total = math.floor(total_quota/3600)
                used = math.floor(quota_used/3600)
                hours = math.floor(quota_left/3600)
                minutes = math.floor(quota_left/60 % 60)
                days = math.floor(hours/24)

                usedperc = math.floor(quota_used / total_quota * 100)
                leftperc = math.floor(quota_left / total_quota * 100)

                quota_details = f"""
**Heroku Account Status**
> __You have **{total} hours** of free dyno quota available each month.😉__
> __Dyno hours used this month__ ;
        - **{used} hours🙃**  ( {usedperc}% )
> __Dyno hours remaining this month__ ;
        - **{hours} hours😁**  ( {leftperc}% )
        - **Approximately {days} days!🥳🥳**
"""
            else:
                quota_details = ""
        except:
            print("`Check your Heroku API key...`")
            quota_details = ""
    else:
        quota_details = ""

    uptime = time.strftime("%Hh %Mm %Ss", time.gmtime(time.time() - BT_STRT_TM))

    await px.edit_text(
        "**🙇🏻‍♂️ Current status of This Bot! 🙇🏻‍♂️**\n\n"
        f"> __BOT Uptime__ : **{uptime}**\nBot was restarted **{uptime}** ago..\n\n"
        f"{quota_details}"
    )
