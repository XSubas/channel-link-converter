import os

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Mandatory variables for the bot to start
API_ID = int(os.environ.get("API_ID", "22952430"))
API_HASH = os.environ.get("API_HASH", "38d1362519cd97bad6b669ecae2929cd")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5947206267:AAGlpb03qV-1zEMhTJGD3pY59FrEpT_H4-g")
GPLINKS_API = os.environ.get("b846b403d53a4694d0829b33ec082a61b67d81aa")
MDISK_API = os.environ.get("MDISK_API", "QqTaWUfW4gRZiwHu4cdg")
ADMINS = list(int(i.strip()) for i in os.environ.get("ADMINS").split("2065355686")) if os.environ.get("ADMINS") else []
DATABASE_NAME = os.environ.get("DATABASE_NAME", "channellinkconverter")
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Raju143:Raju143@cluster0.rn7g4nh.mongodb.net/?retryWrites=true&w=majority")
WEBSITE = os.environ.get('WEBSITE')

#  Optionnal variables
INCLUDE_DOMAIN = list(i.strip() for i in os.environ.get("INCLUDE_DOMAIN").split(",")) if os.environ.get("INCLUDE_DOMAIN") else []
EXCLUDE_DOMAIN = list(i.strip() for i in os.environ.get("EXCLUDE_DOMAIN").split(",")) if os.environ.get("EXCLUDE_DOMAIN") else []
CHANNELS = is_enabled((os.environ.get('CHANNELS', "True")), True)
CHANNEL_ID = list(int(i.strip()) for i in os.environ.get("CHANNEL_ID").split("-1001849304076")) if os.environ.get("CHANNEL_ID") else []
FORWARD_MESSAGE = is_enabled((os.environ.get('FORWARD_MESSAGE', "True")), True)
SOURCE_CODE = os.environ.get("SOURCE_CODE", "https://github.com/XSubas/Channel-link-Converter")
USERNAME = os.environ.get("USERNAME", "Soren_Corporation")
HEADER_TEXT = os.environ.get("HEADER_TEXT", '')
FOOTER_TEXT = os.environ.get("FOOTER_TEXT", '')
BANNER_IMAGE = os.environ.get("BANNER_IMAGE", '')
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '')
LINK_BYPASS = is_enabled((os.environ.get('LINK_BYPASS', "False")), False)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU = True if HEROKU_API_KEY and HEROKU_APP_NAME else False
