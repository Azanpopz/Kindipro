import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import pyrogram
from pyrogram import filters
from caption_status import autocaption
from status import Config
from caption_text import Translation
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery




caption_button=InlineKeyboardMarkup(
        [
              [
                  InlineKeyboardButton("🖋 Current Caption", callback_data = "status_data")
              ], 
              [
                  InlineKeyboardButton("🤩 Help", callback_data = "help_data"), 
                  InlineKeyboardButton("🛡 About", callback_data = "about_data")
              ], 
              [
                  InlineKeyboardButton("🔐 Close", callback_data = "close_data")
              ] 
        ]
)

@Client.on_message(filters.command("caption") & filters.private)
async def start(bot, cmd):
      await bot.send_message(
          chat_id = cmd.chat.id,
          text = Translation.START_TEXT.format(cmd.from_user.first_name, Config.ADMIN), 
          reply_to_message_id = cmd.message_id,
          parse_mode = "markdown",
          disable_web_page_preview = True, 
          reply_markup = start_button
      )


@Client.on_callback_query()
async def button(bot, cmd: CallbackQuery):
    cb_data = cmd.data
    if "about_data" in cb_data:
        await cmd.message.edit(
             text = Translation.ABOUT_TEXT,
             parse_mode="markdown", 
             disable_web_page_preview=True, 
             reply_markup=InlineKeyboardMarkup(
                 [
                     [
                      InlineKeyboardButton("⬇️ BACK", callback_data="back_data"),
                      InlineKeyboardButton("🔐 CLOSE", callback_data="close_data")
                     ]
 
                 ] 
             ) 
        )
    elif "back_data" in cb_data:
          await cmd.message.edit(
               text=Translation.START_TEXT.format(cmd.from_user.first_name, Config.ADMIN),
               parse_mode="markdown", 
               disable_web_page_preview=True, 
               reply_markup=InlineKeyboardMarkup(
                   [
                      
                       [
                        InlineKeyboardButton("🖋 Current Caption", callback_data = "status_data")
                       ], 
                       [
                        InlineKeyboardButton("🍃 Follow Me", url="https://Instagram.com/proavipatil"),
                        InlineKeyboardButton("📕 About Me", callback_data="about_data")
                       ],
                       [
                        InlineKeyboardButton("💡 Help", callback_data="help_data"),
                        InlineKeyboardButton("🔐 Close", callback_data="close_data")
                       ]
                   ]
               )
          )


    elif "status_data" in cb_data:
          await cmd.message.edit(
               text=Translation.STATUS_DATA.format(Config.CAPTION_TEXT, Config.CAPTION_POSITION),
               parse_mode="html", 
               disable_web_page_preview=True, 
               reply_markup=InlineKeyboardMarkup(
                   [
                       [
                        InlineKeyboardButton("⬇️ BACK", callback_data="back_data"),
                        InlineKeyboardButton("🔐 CLOSE", callback_data="close_data")
                       ]
 
                   ] 
               ) 
          )
           
