#Licenced under MIT License
#charset = "utf-8"
#Language = "Python3"
#Bot Framework = "python-telegram-bot"
#The Code is without Proxy, Actual code contains Proxy
#Proxy should be used is of the type SOCKS5
#Special thanks to cyberboySumanjay
#The bot will work till you press ctrl+c in the terminal or command line.,
from telegram.ext import CommandHandler, run_async, Updater, Handler, InlineQueryHandler

#import the required files
import requests
import logging
from telegram import *
from telegram.ext import *

#enable logger (optional)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

TOKEN = "U2FsdGVkX19AauE5C3NpJExPp4xAynsdXI/5eOPd+Cwwc7zJrHxLipUb8PBeRUU4"

#CommandHandler for message "Start"
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"""*Hi {update.effective_chat.first_name},* 

Welcome to the Torrent Searcher Bot. Here you will find all the torrents you search for...

Type /help to know how to use the bot.

Type /info to know about the developer.""", parse_mode=ParseMode.MARKDOWN)

#CommandHandler for message "Help"
def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("""Hey, this is not most complicated bot. Just send me the query you want to search and i will do the rest!

This bot is in the *BETA* stage. So, if any error occurs, feel free to pm me on {YOUR NAME HERE}""", parse_mode=ParseMode.MARKDOWN)


#CommandHandler to get torrents for the query
@run_async
def torr_serch(update: Update, context: CallbackContext) -> None:
    try:
        update.message.reply_text("Searching results for {}".format(update.message.text))
        url = "https://api.sumanjay.cf/torrent/?query={}".format(update.message.text)
        results = requests.get(url).json()
        print(results)
        for item in results:
            age = item.get('age')
            leech = item.get('leecher')
            mag = item.get('magnet')
            name = item.get('name')
            seed = item.get('seeder')
            size = item.get('size')
            typ= item.get('type')
            update.message.reply_text(f"""*Name:* {name}
_Uploaded {age} ago_
*Seeders:* `{seed}`
*Leechers:* `{leech}`
*Size:* `{size}`
*Type:* {typ}
*Magnet Link:* `{mag}`""", parse_mode=ParseMode.MARKDOWN)
        update.message.reply_text("End of the search results...")
    except:
        update.message.reply_text("""Search results completed...
If you've not seen any results, try researching...!""")

#CommandHnadler for message "info"
def info(update: Update, context: CallbackContext) -> None:
    #Never Mind :-)
    update.message.reply_text("""*Made with ❤️ in India by {YOUR NAME}.*

*Language:* [Python3](https://www.python.org/)

*Bot Framework:* [Python Telegram Bot](https://github.com/python-telegram-bot/python-telegram-bot)

*Server:* [Heroku](www.heroku.com)

*Source Code:* `Sore ga kuru made matsu`

If you 👍 this bot, Support the developer by just sharing the bot to Your friends...""", parse_mode=ParseMode.MARKDOWN)

#Add all handlers to the main function.
def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("info", info))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), torr_serch))
    updater.start_polling() #set bot to polling, if you use webhooks, replace this statement with the url of webhook.,
    

#Call the main function
if __name__ == '__main__':
    main()
