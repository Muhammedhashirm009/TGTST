from os import environ
import re

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

SESSION = environ.get("SESSION", "forward bot")
API_ID = "25467884"
API_HASH = "05a687da36243593d4eb624f46375341"
BOT_TOKEN = "5768391364:AAGX0HT3JZpwf_EbLDwz-IaQcQwvzt45xb4"
LOG_CHANNEL = "@h4xlogs1"
PORT = int(environ.get("PORT", "8080"))
ADMINS = 2139560486
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/Joelkb/File-Forward-Bot")
DB_URI = "mongodb+srv://hashir:CI78iFp3LCQM0GuZ@cluster0.rvkb8jf.mongodb.net/"
DB_NAME = "cluster0"
