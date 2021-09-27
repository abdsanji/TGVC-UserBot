# import logging
from pyrogram import Client, idle

app = Client("tgvc")
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> I STARTED DAMN!')
idle()
app.stop()
print('\n>>> I STOPPED DAMN!')
