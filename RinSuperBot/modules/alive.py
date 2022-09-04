import random

from pyrogram import __version__ as pyrover
from telegram import __version__ as telever
from telethon import Button
from telethon import __version__ as tlhver

from FallenRobot import OWNER_USERNAME, SUPPORT_CHAT, dispatcher
from FallenRobot import telethn as tbot
from FallenRobot.events import register

PHOTO = [
    "https://telegra.ph/file/99199d6ba4cd738bdf012.png",
    "https://telegra.ph/file/1319425b8356d6f786324.jpg",
]


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"❆ **Hᴇʏ​ Bᴀᴋᴀ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nI Aᴍ {dispatcher.bot.first_name}** \n\n"
    TEXT += f"❆ **Mʏ Dᴇᴠᴇʟᴏᴘᴇʀ​ : [S L A D E](https://t.me/{OWNER_USERNAME})** \n\n"
    TEXT += f"❆ **Lɪʙʀᴀʀʏ Vᴇʀsɪᴏɴ :** `{telever}` \n\n"
    TEXT += f"❆ **Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
    TEXT += f"❆ **Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ :** `{pyrover}` \n\n"
    BUTTON = [
        [
            Button.url("Hᴇʟᴘ​", f"https://t.me/{dispatcher.bot.username}?start=help"),
            Button.url("Sᴜᴘᴘᴏʀᴛ​", f"https://t.me/{SUPPORT_CHAT}"),
        ]
    ]
    ran = random.choice(PHOTO)
    await tbot.send_file(event.chat_id, ran, caption=TEXT, buttons=BUTTON)


__mod_name__ = "Aʟɪᴠᴇ"
