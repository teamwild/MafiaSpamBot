import asyncio
from spambot import *
from telethon.sync import events
from telethon.tl.types import ChannelParticipantsAdmins, ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest

permissions = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,

)

@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/banall'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/banall'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/banall'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/banall'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/banall'))
async def banall(e):
    try:
        noobs = await e.client.get_participants(e.chat_id, filter=ChannelParticipantsAdmins)
        cant_ban = [admin.id for admin in noobs]
        async for users in e.client.iter_participants(e.chat_id):
            if users.id not in cant_ban:
                await e.client(EditBannedRequest(e.chat_id, users.id, permissions))
                await asyncio.sleep(0.1)
    except Exception as e:
        print(str(e))
