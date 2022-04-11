import os
from pathlib import Path
from dotenv import load_dotenv


basepath = Path()
basedir = str(basepath.cwd())
envars = basepath.cwd() / '.env'
load_dotenv(envars)

TOKEN = os.getenv("TOKEN")
open_weather_token = os.getenv("WEATHER_TOKEN")
admin_id = os.getenv("ADMIN_ID")
host = os.getenv("PGHOST")
PG_USER = os.getenv("PG_USER")
PG_PASS = os.getenv("PG_PASS")




URL_APPLES = 'vk.com'
URL_PEAR = 'instagram.com'

url_apples = URL_APPLES
url_pear = URL_PEAR

# admin_id = ADMINS
