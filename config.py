
import os
#!/usr/bin/env python3


"""Importing"""
from os import environ





API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
MDISK_API = os.environ.get("MDISK_API")
CHANNEL_ID = list(int(i.strip()) for i in os.environ.get("CHANNEL_ID").split(" ")) if os.environ.get("CHANNEL_ID") else []
FORWARD_MESSAGE = bool(os.environ.get("FORWARD_MESSAGE"))
ADMINS = list(int(i.strip()) for i in os.environ.get("ADMINS").split(",")) if os.environ.get("ADMINS") else []
SOURCE_CODE = "https://github.com/kevinnadar22/URL-Shortener-V2"
B = bool(os.environ.get("B"))




#!/usr/bin/env python3


"""Importing"""
from os import environ


class Con(object):
    API_ID = int(environ.get("API_ID", 0))
    API_HASH = environ.get("API_HASH", "")
    BOT_TOKEN = environ.get("BOT_TOKEN", "")
    DB_URL = environ.get("DB_URL", "")
