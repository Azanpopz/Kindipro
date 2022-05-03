# ✋ Hand Written by  @KoshikKumar17
import os
from os import error
import pyrogram
from info import LOG_CHANNEL
from pyrogram import Client as Koshik
from pyrogram import filters

A = """#report ....“
**Name:-** {}

**UserName:-** {}

**User ID:-** {}

**Direct link:-** {}

Else:- tg://openmessage?user_id={}„
--->
His Reported Message:- 👇👇"""

@Koshik.on_message(filters.command(["report"]))
async def report_me(bot, message):
    if message.reply_to_message:
        await message.reply_chat_action("typing")
        k = await message.reply_text("**Processing...⏳**", quote=True)
        await bot.send_message(LOG_CHANNEL, A.format(message.from_user.first_name, message.from_user.username, message.from_user.id, message.from_user.mention, message.from_user.id))
        await message.reply_to_message.forward(chat_id=LOG_CHANNEL)
        await k.edit_text("**Thanks for Reporting.** ❤️\n..\n**I have forwarded your message to my Owner. He will reply you When ever he will be free. ✌️**")
    else:
        await message.reply_text("**Please Send me a message** and **Then Reply that message with __/report__ , so that I can report that to my Owner**")

    
