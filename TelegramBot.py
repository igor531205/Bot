
# def botik():
#     """Start the bot."""
#     from telegram import ForceReply, Update
#     from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

#     async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#         """Send a message when the command /start is issued."""
#         user = update.effective_user
#         await update.message.reply_html(
#             rf"Hi {user.mention_html()}!",
#             # reply_markup=ForceReply(selective=True),
#         )

#     async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#         """Send a message when the command /help is issued."""
#         await update.message.reply_text("Help!")

#     async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#         """Echo the user message."""
#         await update.message.reply_text(update.message.text)

#     TOKEN = '5484436077:AAHRLCdLdDzLyRbU2M3iWsRkOHIM_DmFQeE'

#     # Create the Application and pass it your bot's token.
#     application = Application.builder().token(TOKEN).build()

#     # on different commands - answer in Telegram
#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(CommandHandler("help", help_command))

#     # on non command i.e message - echo the message on Telegram
#     application.add_handler(MessageHandler(
#         filters.TEXT & ~filters.COMMAND, echo))

#     # Run the bot until the user presses Ctrl-C
#     application.run_polling()


# def bot():
#     """telegram bot.
#     """

#     from telegram import Update
#     from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

#     async def help(update: Update, context: CallbackContext):
#         """Command "Help" for user.
#         """

#         log([update.effective_user.id,
#             update.effective_user.first_name,
#             update.message.text
#              ])

#         command = ['/hello',
#                    '/time',
#                    '/add',
#                    '/sub',
#                    '/div',
#                    '/mult'
#                    ]

#         await update.message.reply_text('\n'.join(command))

#     async def hello(update: Update, context: CallbackContext):
#         """Command "hello" for user.
#         """

#         log([update.effective_user.id,
#             update.effective_user.first_name,
#             update.message.text
#              ])

#         msg = f'Hello {update.effective_user.first_name}'

#         await update.message.reply_text(msg)

#     async def time(update: Update, context: CallbackContext):
#         """Command "time" for user.
#         """

#         from datetime import datetime

#         log([update.effective_user.id,
#             update.effective_user.first_name,
#             update.message.text
#              ])

#         msg = f'Now time {datetime.now():%Y.%m.%d %H:%M}'

#         await update.message.reply_text(msg)

#     async def add(update: Update, context: CallbackContext):
#         """Command "add" for user.
#         """

#         log([update.effective_user.id,
#             update.effective_user.first_name,
#             update.message.text
#              ])

#         msg = update.message.text.split()

#         if len(msg) == 3:

#             num1 = float(msg[1])
#             num2 = float(msg[2])

#             await update.message.reply_text(
#                 f'{num1} + {num2} = {num1 + num2}')

#         else:

#             msg = [
#                 'Incorrect enter!!!',
#                 'For exemple, enter:',
#                 '/add 1 1']

#             await update.message.reply_text(
#                 '\n'.join(msg))

#     async def sub(update: Update, context: CallbackContext):
#         """Command "sub" for user.
#         """

#         log([update.effective_user.id,
#             update.effective_user.first_name,
#             update.message.text
#              ])

#         msg = update.message.text.split()

#         if len(msg) == 3:

#             num1 = float(msg[1])
#             num2 = float(msg[2])

#             await update.message.reply_text(
#                 f'{num1} - {num2} = {num1 - num2}')

#         else:

#             msg = [
#                 'Incorrect enter!!!',
#                 'For exemple, enter:',
#                 '/sub 1 1']

#             await update.message.reply_text(
#                 '\n'.join(msg))

#     async def div(update: Update, context: CallbackContext):
#         """Command "div" for user.
#         """

#         log([update.effective_user.id,
#             update.effective_user.first_name,
#             update.message.text
#              ])

#         msg = update.message.text.split()

#         if len(msg) == 3:

#             num1 = float(msg[1])
#             num2 = float(msg[2])

#             await update.message.reply_text(
#                 f'{num1} / {num2} = {num1 / num2}')

#         else:

#             msg = [
#                 'Incorrect enter!!!',
#                 'For exemple, enter:',
#                 '/div 1 1']

#             await update.message.reply_text(
#                 '\n'.join(msg))

#     async def mult(update: Update, context: CallbackContext):
#         """Command "mult" for user.
#         """

#         log([update.effective_user.id,
#             update.effective_user.first_name,
#             update.message.text
#              ])

#         msg = update.message.text.split()

#         if len(msg) == 3:

#             num1 = float(msg[1])
#             num2 = float(msg[2])

#             await update.message.reply_text(
#                 f'{num1} * {num2} = {num1 * num2}')

#         else:

#             msg = [
#                 'Incorrect enter!!!',
#                 'For exemple, enter:',
#                 '/mult 1 1']

#             await update.message.reply_text(
#                 '\n'.join(msg))

#     # Bot username: @GB_for_HomeWork_bot
#     app = ApplicationBuilder().token('5484436077:AAHRLC'
#                                      + 'dLdDzLyRbU2M3iW'
#                                      + 'sRkOHIM_DmFQeE'
#                                      ).build()

#     print('Start "CommandHandler"')

#     app.add_handler(CommandHandler('help', help))
#     app.add_handler(CommandHandler('hello', hello))
#     app.add_handler(CommandHandler('time', time))
#     app.add_handler(CommandHandler('add', add))
#     app.add_handler(CommandHandler('sub', sub))
#     app.add_handler(CommandHandler('div', div))
#     app.add_handler(CommandHandler('mult', mult))

#     app.run_polling()

# def main():
#     # Commands - answer in Telegram
#     dispatcher.add_handler(CommandHandler(start.__name__, start))
#     dispatcher.add_handler(CommandHandler('kill', kill))

#     # Message for bot - answer in Telegram
#     dispatcher.add_handler(MessageHandler(
#         Filters.all, echo))

# def log(data_log: list):
#     """log to file.
#     """

#     from datetime import datetime

#     with open('db.csv', 'a') as data:
#         data.write(','.join([f'{datetime.now():%Y.%m.%d %H:%M}']
#                             + [str(item) for item in data_log])
#                    + '\n')

# def kill(update: Update, context: CallbackContext) -> None:
#     """Command kill Bot."""

#

# def bot_command(update: Update, context: CallbackContext) -> None:
#     """Command start."""
#     user_says = " ".join(context.args)
# await update.message.reply_text("Welcome to my awesome bot!")
#     if update.effective_user.username in masters:

#         user_name = update.effective_user.full_name if \
#             update.effective_user.full_name is None else \
#             update.effective_user.username

#         # chats.append(update.effective_chat.id)

#         update.message.reply_text(f'Hello  "{user_name}"')
#     print(chats)
# chat_id = update.message.chat_id
# first_name = update.message.chat.first_name
# last_name = update.message.chat.last_name
# username = update.message.chat.username
# print("chat_id : {}; and firstname : {}; lastname : {};  username {}". format(
#     chat_id, first_name, last_name, username))

# print(ChatMemberHandler.CHAT_MEMBER)
# chats_users[update.effective_chat.id]


import os
import signal
import asyncio
import logging
from telegram import (
    Update,
    Chat,
    ChatMember,
    ParseMode,
    ChatMemberUpdated,
    ForceReply,
    SentWebAppMessage,
    Message,
    Bot)
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    ChatMemberHandler,
    Filters,
    CallbackContext,
    Handler,
    run_async)


async def telegram_bot(BOT_TOKEN: str, BOT_OWNER: str):
    """Start the bot.
    Args:
        BOT_TOKEN: Key for bot.
        BOT_OWNER: username for master of bot.
    """

    def bot_message(update: Update, context: CallbackContext) -> None:
        """Echo the user message."""

        log.info(', '.join([
            f'Chat: {update.message.chat_id}',
            f'User: {update.message.from_user.username}',
            f'FullName: {update.message.from_user.full_name}',
            f'Message: {update.message.text}']))

        if update.message.chat_id in chats:
            update.message.reply_text(update.message.text)

    def bot_start(update: Update, context: CallbackContext) -> None:
        """Command start for bot."""

        log.info(', '.join([
            f'Chat: {update.message.chat_id}',
            f'User: {update.message.from_user.username}',
            f'FullName: {update.message.from_user.full_name}',
            f'Message: {update.message.text}']))

        if update.message.from_user.username in masters:

            update.message.reply_text(
                f'Hello, {update.message.from_user.full_name}' if
                update.message.chat.type == 'private' else
                f'Hello, {update.message.from_user.full_name}' +
                ' ' + f'and other Users')

            chats.append(update.message.chat.id)
            log.info(
                f'Chat add to bot: {update.message.chat_id}')

    def bot_stop(update: Update, context: CallbackContext) -> None:
        """Command stop for bot."""

        log.info(', '.join([
            f'Chat: {update.message.chat_id}',
            f'User: {update.message.from_user.username}',
            f'FullName: {update.message.from_user.full_name}',
            f'Message: {update.message.text}']))

        if update.message.from_user.username in masters:

            update.message.reply_text(
                f'Good bye, {update.message.from_user.full_name}' if
                update.message.chat.type == 'private' else
                f'Good bye, {update.message.from_user.full_name}' +
                ' ' + f'and other Users')

            if update.message.chat.type != 'private':

                update.message.chat.leave()
                log.info(
                    f'Bot leave chat: {update.message.chat_id}')

            chats.remove(update.message.chat.id)
            log.info(
                f'Chat remove from bot: {update.message.chat_id}')

    def bot_kill(update: Update, context: CallbackContext) -> None:
        """Command kill for bot."""

        log.info(', '.join([
            f'Chat: {update.message.chat_id}',
            f'User: {update.message.from_user.username}',
            f'FullName: {update.message.from_user.full_name}',
            f'Message: {update.message.text}']))

        if update.message.from_user.username in masters:

            update.message.reply_text(
                f'You "Kill" me, {update.message.from_user.full_name}')

            os.kill(os.getpid(), signal.SIGABRT)

    global masters
    masters = [BOT_OWNER]
    global chats
    chats = []

    # Create the Logger
    log = logging.getLogger(__name__)

    # Create the Updater and pass it your bot's token.
    updater = Updater(BOT_TOKEN)
    sender = Bot(BOT_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Commands from Telegram
    dispatcher.add_handler(CommandHandler('start', bot_start))
    dispatcher.add_handler(CommandHandler('stop', bot_stop))
    dispatcher.add_handler(CommandHandler('kill', bot_kill))

    # Message from Telegram
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, bot_message))

    # Start the Bot
    updater.start_polling()
    log.info('Bot started')

    updater.idle()
    log.info('Stop bot')
