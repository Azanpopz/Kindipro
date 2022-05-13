# (c) @KoshikKumar17
import os
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

BTN = InlineKeyboardMarkup([[InlineKeyboardButton('✨ 🇮🇳 ❤️ INDIA ❤️ 🇮🇳✨', url='https://india.gov.in')]])

A = """▭▭ ▭▭ ▭▭  ▭▭ ▭▭ ▭▭\nSEARCHING...    𝟎𝟎/𝟏𝟎𝟎%\n▭▭ ▭▭ ▭▭  ▭▭ ▭▭ ▭▭"""
B = """▬▬ ▬▭ ▭▭  ▭▭ ▭▭ ▭▭\nSEARCHING...     𝟐𝟓/𝟏𝟎𝟎%\n▬▬ ▬▭ ▭▭  ▭▭ ▭▭ ▭▭"""
C = """▬▬ ▬▬ ▬▭  ▭▭ ▭▭ ▭▭\nSEARCHING...     𝟓𝟎/𝟏𝟎𝟎%\n▬▬ ▬▬ ▬▭  ▭▭ ▭▭ ▭▭"""
D = """▬▬ ▬▬ ▬▬  ▭▭ ▭▭ ▭▭\nSEARCHING...     𝟕𝟓/𝟏𝟎𝟎%\n▬▬ ▬▬ ▬▬  ▭▭ ▭▭ ▭▭"""
E = """▬▬ ▬▬ ▬▬  ▬▬ ▬▭  ▭▭\nSEARCHING...     𝟖𝟓/𝟏𝟎𝟎%\n▬▬ ▬▬ ▬▬  ▬▬ ▬▭ ▭▭"""
F = """▬▬ ▬▬ ▬▬  ▬▬ ▬▬ ▬▬\nSEARCHING...    𝟏𝟎𝟎/𝟏𝟎𝟎%\n▬▬ ▬▬ ▬▬  ▬▬ ▬▬ ▬▬"""
INDIAN = """▬▬ ▬▬ ▬▬  ▬▬ ▬▬ ▬▬\nSEARCHING...    𝟏𝟎𝟎/𝟏𝟎𝟎%\n▬▬ ▬▬ ▬▬  ▬▬ ▬▬ ▬▬"""




@Client.on_message(filters.private & filters.command(["india"]))
async def india_art(bot, update):
        await update.reply_chat_action("typing")
        px = await update.reply_text(A,quote=True)
        await px.edit_text(text=C, reply_markup=BTN)
        await px.edit_text(text=E, reply_markup=BTN)
        
        await px.delete()
        await update.reply_text(text=INDIAN,quote=True,reply_markup=BTN)
