import os

import os
import re
import sys
import heroku3


ENVIRONMENT = bool(os.environ.get('ENVIRONMENT', False))

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
else:
    # Fill the Values
    API_ID = 0
    API_HASH = ""
    BOT_TOKEN = ""




class Configs:

    # Mendatory Variables
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", None)
    REPLY_MESSAGE = REPLY_MESSAGE or None
