# Ported By @VckyouuBitch Geez - Projects
# FROM GeezProjects <https://github.com/Vckyou/GeezProjects>
# Copyright (c) Team Ultroid From Geez Projects

from userbot import CMD_HELP, bot
from userbot.events import geezbot_cmd
from userbot import CUSTOM_CMD as geez


@bot.on(geezbot_cmd(outgoing=True, pattern="xogame (.*)"))
async def _(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()


@bot.on(geezbot_cmd(outgoing=True, pattern="whisp (.*)"))
async def _(event):
    if event.fwd_from:
        return
    wwwspr = event.pattern_match.group(1)
    botusername = "@whisperBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, wwwspr)
    await tap[0].click(event.chat_id)
    await event.delete()


@bot.on(geezbot_cmd(outgoing=True, pattern="mod (.*)"))
async def _(event):
    if event.fwd_from:
        return
    modr = event.pattern_match.group(1)
    botusername = "@PremiumAppBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, modr)
    await tap[0].click(event.chat_id)
    await event.delete()

CMD_HELP.update({
    "games":
    f"πΎπ€π’π’ππ£π: `{geez}xogame`\
\nβ³ : Mainkan game XO bersama temanmu.\
\n\nπΎπ€π’π’ππ£π: `{geez}mod <nama app>`\
\nβ³ : Dapatkan applikasi mod\
\n\nπΎπ€π’π’ππ£π: `{geez}whisp <teks> <username/ID>`\
\nβ³ : Berikan pesan rahasia"})
