import os
class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    CAPTION = os.environ.get("CAPTION", "╔════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ═════╗\n♻️ 𝙅𝙊𝙄𝙉 :- @nasrani_update\n♻️ 𝙅𝙊𝙄𝙉 :- @NasraniSeries\n╚════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ═════╝")
    BUTTON_TEXT = os.environ.get("BUTTON", "🔻Join Channel🔻")
    URL_LINK = os.environ.get("LINK", "T.ME/Nasrani_update")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "MINNAL_MURALI_ROBOT")


import os



class Config(object):
      BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
      API_ID = int(os.environ.get("APP_ID", 12345))
      API_HASH = os.environ.get("API_HASH")
      CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMINS = os.environ.get("ADMINS", "kinzanoufal")


class Translation(object):

      
      START_TEXT = """
🍃 **ʜᴀɪ** __{}__ , 

__I Am Auto CaptionBot Just Add In Channel and See Magic__

**ɪ ᴄᴀɴ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴀᴅᴅ ᴘʀᴇ-sᴇᴛᴛᴇᴅ ᴄᴀᴘᴛɪᴏɴ ᴛᴏ ᴛʜᴇ ғɪʟᴇs ɪɴ ᴄʜᴀɴɴᴇʟs**

__ɪ ᴀᴍ ᴄᴜʀʀᴇɴᴛʟʏ ᴡᴏʀᴋɪɴɢ ғᴏʀ ᴀ ᴄʜᴀɴɴᴇʟ ᴜsᴇ ᴍᴇ__

😈 __ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ__ 👉 __@{}__
"""    


              

     
      ABOUT_TEXT = """
📕 **𝐀𝐛𝐨𝐮𝐭 𝐌𝐞**

__○ ᴍʏ ɴᴀᴍᴇ : [CapXbot](https://t.me/Avishkarpatil)__
__○ ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ __
__○ ғʀᴀᴍᴇᴡᴏʀᴋ : ᴘʏʀᴏɢʀᴀᴍ __
__○ sᴇʀᴠᴇʀ : ʜᴇʀᴏᴋᴜ __
__○ ᴠᴇʀsɪᴏɴ : 2.0.1__
__○ ᴄʀᴇᴀᴛᴏʀ :  @AvishkarPatil__
 
**[© ᴀᴠɪsʜᴋᴀʀ ᴘᴀᴛɪʟ](https://t.me/Avishkarpatil)**
"""

      MARKDOWN_TEXT = """
🔰 <u>𝐀𝐛𝐨𝐮𝐭 𝐌𝐚𝐫𝐤𝐝𝐨𝐰𝐧</u>
👉 <b>Bold text</b>
🔸 <code>**Avishkar**</code>

👉 <b>Italic text</b>
🔹 <code>__Avishkat__</code> 

👉 <b>Code text</b>
🔸 <code>`Avishkar`</code>   

👉 <b>Hyperlink text</b>
🔹 <code>[hyperlink_text](https://avipatilweb.me)</code> 

〰〰〰〰〰〰〰〰〰〰

<b><a href="https://t.me/Avishkarpatil">© ᴀᴠɪsʜᴋᴀʀ ᴘᴀᴛɪʟ</a></b>
"""

# Bot status display

      STATUS_DATA = """
🔰 <u>𝐁𝐎𝐓 𝐒𝐓𝐀𝐓𝐔𝐒</u>

🖌️ <b>Current Caption :</b> 
{}

📐 <b>Current Position :</b> {}

<b><a href="https://t.me/Avishkarpatil">© ᴀᴠɪsʜᴋᴀʀ ᴘᴀᴛɪʟ</a></b>
"""


      SOURCE_TEXT = """

○ <b> I Am Available Open Source on Github 
      Click Below Link And Deploy Me Now </b>

○ <i>DEPLOY</i> : <b><a href="https://heroku.com/deploy?template=https://github.com/avipatilpro/Caption-Bot">On Heroku</a></b>    

○ <i>SOURCE</i> : <b><a href="https://github.com/avipatilpro/Caption-Bot">Caption Bot</a></b>  
"""





import pyrogram

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from caption_config import Config
from pyrogram import Client 
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class autocaption(Client):
    
    def __init__(self):
        super().__init__(
            session_name="Captioner",
            bot_token = Config.BOT_TOKEN,
            api_id = Config.API_ID,
            api_hash = Config.API_HASH,
            workers = 20,
            plugins = dict(
                root="Plugins"
            )
        )

if __name__ == "__main__" :
    






