import os
class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    CAPTION = os.environ.get("CAPTION", "╔════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ═════╗\n♻️ 𝙅𝙊𝙄𝙉 :- @nasrani_update\n♻️ 𝙅𝙊𝙄𝙉 :- @NasraniSeries\n╚════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ═════╝")
    BUTTON_TEXT = os.environ.get("BUTTON", "🔻Join Channel🔻")
    URL_LINK = os.environ.get("LINK", "T.ME/Nasrani_update")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "MINNAL_MURALI_ROBOT")



