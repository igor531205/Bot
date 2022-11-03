import os
import asyncio
import logging
from telegrambot import telegram_bot


if __name__ == '__main__':

    # Clear Terminal
    os.system('cls')

    # Init logger
    logging.basicConfig(filename='logging.log', filemode='a',
                        format='; '.join([
                            f'%(asctime)s',
                            f'%(name)s',
                            f'%(levelname)s',
                            f'%(message)s']),
                        level=logging.INFO, encoding='utf-8')

    # Init Bot Token and username owner of Bot "@GB_for_HomeWork_bot"
    BOT_TOKEN = '5484436077:AAHRLCdLdDzLyRbU2M3iWsRkOHIM_DmFQeE'
    BOT_OWNER = 'igor531205'

    # Run bot
    asyncio.run(telegram_bot(BOT_TOKEN, BOT_OWNER))
