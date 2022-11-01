from os import system
from asyncio import run
from TelegramBot import bot

if __name__ == '__main__':

    # Clear Terminal
    system('cls')

    # Init Bot Token and username owner of Bot
    BOT_TOKEN = '5484436077:AAHRLCdLdDzLyRbU2M3iWsRkOHIM_DmFQeE'
    BOT_OWNER = 'igor531205'

    # Run bot
    run(bot(BOT_TOKEN, BOT_OWNER))
