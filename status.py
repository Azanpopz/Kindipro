class Config(object):
      BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
      API_ID = int(os.environ.get("APP_ID", 12345))
      API_HASH = os.environ.get("API_HASH")
      CAPTION_STATUS = os.environ.get("CAPTION_STATUS", "")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMINS = os.environ.get("ADMINS", "kinzanoufal")


