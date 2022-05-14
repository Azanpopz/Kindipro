import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

Munnipoz= Client(
    "Welcome-Bot",
     bot_token = os.environ["BOT_TOKEN"],
     api_id = int(os.environ["API_ID"]),
     api_hash = os.environ["API_HASH"]
)




    
@Client.on_message(filters.new_chat_members)
async def auto_welcome(bot: Client, msg: Message):
    # from PR0FESS0R-99 import ID-Bot
    first = msg.from_user.first_name
    last = msg.from_user.last_name
    mention = msg.from_user.mention
    username = msg.from_user.username
    chat_id = int(msg.chat.id)
    count = await msg.get_chat_members_count(chat_id)
    id = msg.from_user.id
    group_name = msg.chat.title
    group_username = msg.chat.username
    name_button = "🔰 JOIN NOW 🔰"
    link_button = "t.me/nasrani_update"
    button_name = os.environ.get("WELCOME_BUTTON_NAME", name_button)
    button_link = os.environ.get("WELCOME_BUTTON_LINK", link_button)
    welcome_text = f"Hey {mention}\nWelcome To {group_name} your admission no {count}"
    WELCOME_TEXT = os.environ.get("WELCOME_TEXT", welcome_text)
    print("Welcome Message Activate")
    BUTTON = bool(os.environ.get("WELCOME_BUTTON"))
    if not BUTTON:
       await msg.reply_text(text=WELCOME_TEXT.format(
           first = msg.from_user.first_name,
           last = msg.from_user.last_name,
           username = None if not msg.from_user.username else '@' + msg.from_user.username,
           mention = msg.from_user.mention,
           id = msg.from_user.id,
           group_name = msg.chat.title,
           group_username = None if not msg.chat.username else '@' + msg.chat.username
          )
       )
    else:
       await msg.reply_text(text=WELCOME_TEXT.format(
           first = msg.from_user.first_name,
           last = msg.from_user.last_name,
           username = None if not msg.from_user.username else '@' + msg.from_user.username,
           mention = msg.from_user.mention,
           id = msg.from_user.id,
           group_name = msg.chat.title,
           group_username = None if not msg.chat.username else '@' + msg.chat.username
          ),
       reply_markup=InlineKeyboardMarkup(
               [
                   [
                       InlineKeyboardButton
                           (
                               button_name, url=button_link
                           )
                   ]  
               ]
           )
       )  


print("""Auto Welcome Bot Started

Maintained By NASRANI_UPDATE""")

