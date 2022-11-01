import logging
from os import system
from asyncio import run
from BotMethods import bot

if __name__ == '__main__':

    # Clear Terminal
    system('cls')

    # Init logger
    logging.basicConfig(format='%(asctime)s - %(name)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__).info

    # Init Bot Token and owner of Bot
    BOT_TOKEN = '5484436077:AAHRLCdLdDzLyRbU2M3iWsRkOHIM_DmFQeE'
    BOT_OWNER = 'igor531205'

    # Run bot
    run(bot(BOT_TOKEN, BOT_OWNER))
