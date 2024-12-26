#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
import re
from os import environ
import os

id_pattern = re.compile(r'^.\d+$')


API_ID = os.environ.get("API_ID", "13963336")
API_HASH = os.environ.get("API_HASH", "a144d1e22ef0b29738e8c00713d02678")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8154487335:AAGQFJcKAlbHwylgPHujmjzBv6efv9q0JAA")
ADMIN = int(os.environ.get("ADMIN", '7910994767'))
FSUB_UPDATES = os.environ.get("FSUB_CHANNEL", "nyyybots")
FSUB_GROUP = os.environ.get("FSUB_GROUP", "nyyyygrop")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Nischay999:Nischay999@cluster0.5kufo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
CAPTION = os.environ.get("CAPTION", "")
group = environ.get('GROUP', '-1002173560131')
GROUP = int(group) if group and id_pattern.search(group) else None
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
SUNRISES_PIC= "https://graph.org/file/bd91761f6e938e2e6d23a.jpg"  # Replace with your Telegraph link
AUTH_USERS = int(os.environ.get("AUTH_USERS", '2103299862'))
WEBHOOK = bool(os.environ.get("WEBHOOK", True))
PORT = int(os.environ.get("PORT", "8080"))
LOG_CHANNEL_ID = os.environ.get("LOG_CHANNEL_ID", -1002421238378)
