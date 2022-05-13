# (c) @KoshikKumar17
import os
from pyrogram import Client as Koshik
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from pyrogram.types import Message
BTN = InlineKeyboardMarkup([[InlineKeyboardButton('✨ 🇮🇳 ❤️ INDIA ❤️ 🇮🇳✨', url='https://india.gov.in')]])

A = """▭▭ ▭▭ ▭▭  ▭▭ ▭▭ ▭▭\nSEARCHING...    𝟎𝟎/𝟏𝟎𝟎%\n▭▭ ▭▭ ▭▭  ▭▭ ▭▭ ▭▭"""
B = """▬▬ ▬▭ ▭▭  ▭▭ ▭▭ ▭▭\nSEARCHING...     𝟐𝟓/𝟏𝟎𝟎%\n▬▬ ▬▭ ▭▭  ▭▭ ▭▭ ▭▭"""
C = """▬▬ ▬▬ ▬▭  ▭▭ ▭▭ ▭▭\nSEARCHING...     𝟓𝟎/𝟏𝟎𝟎%\n▬▬ ▬▬ ▬▭  ▭▭ ▭▭ ▭▭"""
D = """▬▬ ▬▬ ▬▬  ▭▭ ▭▭ ▭▭\nSEARCHING...     𝟕𝟓/𝟏𝟎𝟎%\n▬▬ ▬▬ ▬▬  ▭▭ ▭▭ ▭▭"""
E = """▬▬ ▬▬ ▬▬  ▬▬ ▬▭  ▭▭\nSEARCHING...     𝟖𝟓/𝟏𝟎𝟎%\n▬▬ ▬▬ ▬▬  ▬▬ ▬▭ ▭▭"""
F = """▬▬ ▬▬ ▬▬  ▬▬ ▬▬ ▬▬\nSEARCHING...    𝟏𝟎𝟎/𝟏𝟎𝟎%\n▬▬ ▬▬ ▬▬  ▬▬ ▬▬ ▬▬"""
INDIAN = """▬▬ ▬▬ ▬▬  ▬▬ ▬▬ ▬▬\nSEARCHING...    𝟏𝟎𝟎/𝟏𝟎𝟎%\n▬▬ ▬▬ ▬▬  ▬▬ ▬▬ ▬▬"""




@Koshik.on_message(filters.command(["india"]))
async def india_art(bot, message):
        await message.reply_chat_action("typing")
        px = await message.reply_text(A,quote=True)
        await px.edit_text(text=B, reply_markup=BTN)
        await px.edit_text(text=C, reply_markup=BTN)
        await px.edit_text(text=D, reply_markup=BTN)
        await px.edit_text(text=E, reply_markup=BTN)
        await px.edit_text(text=F, reply_markup=BTN)
        await px.delete()
        await update.reply_text(text=INDIAN,quote=True,reply_markup=BTN)
