import os
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest
from myscript import script


pr0fess0r_99=Client(
    "Auto Approved Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

CHAT_ID=int(os.environ.get("CHAT_ID", None))
TEXT=os.environ.get("APPROVED_WELCOME_TEXT", "ʜᴇʟʟᴏ {mention}\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴍʏ ᴄʜᴀɴɴᴇʟ.{title}\n\nᴏɴʟʏ ɴᴇᴡ ᴀɴᴅ ʟᴏᴡ ꜱɪᴢᴇ ᴍᴏᴠɪᴇ ᴀᴠᴀɪʟᴀʙʟᴇ. ᴇɴᴊᴏʏɪɴɢ🔥🔥")
APPROVED = os.environ.get("APPROVED_WELCOME", "on").lower()

@Client.on_message(filters.private & filters.command(["🙂"]))
async def start(client: pr0fess0r_99, message: Message):
    approvedbot = await client.get_me() 
    button = [[ InlineKeyboardButton("📦 Repo", url="t.me/nasrani_update"), InlineKeyboardButton("Updates 📢", url="t.me/nasrani_update") ],
              [ InlineKeyboardButton("➕️ Add Me To Your Chat ➕️", url=f"http://t.me/{approvedbot.username}?startgroup=botstart") ]]
    await client.send_message(chat_id=message.chat.id, text=f"**__Hello {message.from_user.mention} Iam Auto Approver Join Request Bot Just [Add Me To Your Group Channnl](http://t.me/{approvedbot.username}?startgroup=botstart) || Repo t.me/nasrani_update||**__", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)



@Client.on_chat_join_request(filters.chat(CHAT_ID))
async def autoapprove(client: pr0fess0r_99, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} Joined 🤝") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        buttons = [[
            InlineKeyboardButton('🧩𝐉𝐎𝐈𝐍 𝐆𝐑𝐎𝐔𝐏🧩', url=f'https://t.me/nasrani_update')
            
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title),
        reply_markup=reply_markup,
        parse_mode='html'
    )
        print("Welcome....")

print("Auto Approved Bot")

