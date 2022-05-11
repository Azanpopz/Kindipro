import os
class Config(object):
    BT_TOKEN = os.environ.get("BT_TOKEN", "5199038181:AAGJIsXbVjtAiwh0yS4Ir3Q0sktjzIGzro8")
    ID = int(os.environ.get("ID", "1778836"))
    HASH = os.environ.get("HASH", "7bcf61fcd32b8652cd5876b02dcf57ae")
    CAPTION = os.environ.get("CAPTION", "╔════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ═════╗\n♻️ 𝙅𝙊𝙄𝙉 :- @nasrani_update\n♻️ 𝙅𝙊𝙄𝙉 :- @NasraniSeries\n╚════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ═════╝")
    BUTTON_TEXT = os.environ.get("BUTTON", "🔻Join Channel🔻")
    URL_LINK = os.environ.get("LINK", "T.ME/Nasrani_update")
    BT_USERNAME = os.environ.get("BT_USERNAME", "LIZZA_CAPTION_BOT")


class mdisk(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    API_ID = int(os.environ.get("API_ID", 123456))

    API_HASH = os.environ.get("API_HASH", "")
    
    API_KEY = os.environ.get("API_KEY", "tHRFNVu8CkjkdstzXNsp")

    # AUTH_USERS = set(str(x) for x in os.environ.get("AUTH_USERS", "").split())

    # PRIVATE = bool(os.environ.get("PRIVATE", ""))
