import random
lines = open('C:\\Users\\User\\Desktop\\singnplur.txt').read().splitlines()
myline =random.choice(lines)

@Client.on_message(filters.command('rng') & filters.private)
def command1(bot, message):
    bot.send_message(message.chat.id, myline)
