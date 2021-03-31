# COPYRIGHT (C) 2021 BY LEGENDX22 AND PROBOYX

"""
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
                 MADE BY LEGENDX AND PROBOYX
                   CREDITS #TEAMLEGEND 
                PLEASE DON'T REMOVE CREDITS
"""

from telethon import events, Button, custom
import re, os
from LEGEND.events import register
from LEGENDX import xbot as tbot
from LEGENDX import xbot as tgbot
PHOTO = "https://telegra.ph/file/6250ea95d8b607ebb7e2a.jpg"
@register(pattern=("/alive"))
async def awake(event):
  legendx = event.sender.first_name
  LEGENDX = "➥ASUNA HERE!! \n\n"
  LEGENDX += "➥ALL SYSTEM WORKING PROPERLY\n\n"
  LEGENDX += "➥ASUNA OS : 3.8 LATEST\n\n"
  LEGENDX += f"➥USER: {legendx} ☺️\n\n"
  LEGENDX += "➥FULLY UPDATED\n\n"
  LEGENDX += "➥TELETHON : 1.19.5 [LATEST]\n\n"
  LEGENDX += "!!THANKS FOR ADD ME HERE!!"
  BUTTON = [[Button.url("MASTER", "https://t.me/ken_kenaki"), Button.url("DEVLOPER", "https://t.me/kaneki_alt")]]
  BUTTON += [[custom.Button.inline("REPOSITORYS", data="LEGENDX")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LEGENDX,  buttons=BUTTON)




@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"LEGENDX")))
async def callback_query_handler(event):
# inline by LEGENDX22 and PROBOYX🔥
  PROBOYX = [[Button.url("REPO-ASUNA", "https://github.com/LEGENDXOP/LEGEND-BOT")]]
  PROBOYX +=[[Button.url("DEPLOY-ASUNA", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Flegendxop%2Flegend-bot&template=https%3A%2F%2Fgithub.com%2FLEGENDXOP%2FLEGEND-BOTP%2FLE")]]
  PROBOYX +=[[Button.url("SUPPORT CHANNEL", "https://t.me/kiritosupport"), Button.url("SUPPORT GROUP", "https://t.me/kiritosupport1")]]
  PROBOYX +=[[custom.Button.inline("ALIVE", data="PROBOY")]]
  await event.edit(text=f"ALL DETAILS OF REPOS", buttons=PROBOYX)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"PROBOY")))
async def callback_query_handler(event):
  global PHOTO
  legendx = event.sender.first_name
# inline by LEGENDX22 and PROBOYX 🔥
  LEGENDX = "➥ASUNA HERE!! \n\n"
  LEGENDX += "➥ALL SYSTEM WORKING PROPERLY\n\n"
  LEGENDX += "➥KIRITO OS : 3.8 LATEST\n\n"
  LEGENDX += f"➥USER: {legendx} ☺️\n\n"
  LEGENDX += "➥FULLY UPDATED BOT\n\n"
  LEGENDX += "➥TELETHON : 1.19.5 [LATEST]\n\n"
  LEGENDX += "!!THANKS FOR ADD ME HERE!!"
  BUTTONS = [[Button.url("MASTER", "https://t.me/ken_kenaki"), Button.url("DEVLOPER", "https://t.me/kenaki_alt")]]
  BUTTONS += [[custom.Button.inline("REPOSITORYS", data="LEGENDX")]]
  await event.edit(text=LEGENDX, buttons=BUTTONS)


@register(pattern=("/repo|/REPO"))
async def repo(event):
  await tbot.send_message(event.chat, "REPO OF ASUNA", buttons=[[Button.url("🛡REPO🛡", "https://github.com/prabhav921/ASUNA")]])
# PROBOYX 🔥 LEGENDX22

__help__ = """
 - /alive check bot alive or die
 - /repo for this bot repo
"""
__mod_name__ = "✨Alive✨"
