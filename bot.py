
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


from getpass import getuser


def log(data_log: list):
    """log to file.
    """

    from datetime import datetime

    with open('db.csv', 'a') as data:
        data.write(','.join([f'{datetime.now():%Y.%m.%d %H:%M}']
                            + [str(item) for item in data_log])
                   + '\n')


def main():
    import os
    import signal
    from telegram import (
        Update,
        Chat,
        ChatMember,
        ParseMode,
        ChatMemberUpdated,
        ForceReply)
    from telegram.ext import (
        Updater,
        CommandHandler,
        MessageHandler,
        ChatMemberHandler,
        Filters,
        CallbackContext)

    def start(update: Update, context: CallbackContext) -> None:
        """Command start."""

        if update.effective_user.username in masters:

            user_name = update.effective_user.full_name if \
                update.effective_user.full_name is None else \
                update.effective_user.username

            update.message.reply_text(f'Hello  "{user_name}"')

            print(update.effective_chat.getChatMember)
            # chats_users[update.effective_chat.id] = TODO

    def kill(update: Update, context: CallbackContext) -> None:
        """Command kill Bot."""

        if update.effective_user.username in masters:

            update.message.reply_text('Kill Bot')

            if update.effective_chat.type != 'private':

                # TODO chats_users[update.effective_chat.id]
                update.effective_chat.leave()

            os.kill(os.getpid(), signal.SIGINT)

    def echo(update: Update, context: CallbackContext) -> None:
        """Echo the user message."""
        print('mes')
        update.message.reply_text(update.message.text)

    # from typing import Tuple, Optional

    # def extract_status_change(
    #     chat_member_update: ChatMemberUpdated,
    # ) -> Optional[Tuple[bool, bool]]:
    #     """Takes a ChatMemberUpdated instance and extracts whether the 'old_chat_member' was a member
    #     of the chat and whether the 'new_chat_member' is a member of the chat. Returns None, if
    #     the status didn't change.
    #     """
    #     status_change = chat_member_update.difference().get("status")
    #     old_is_member, new_is_member = chat_member_update.difference().get("is_member",
    #                                                                        (None, None))

    #     if status_change is None:
    #         return None

    #     old_status, new_status = status_change
    #     was_member = old_status in [
    #         ChatMember.MEMBER,
    #         ChatMember.CREATOR,
    #         ChatMember.ADMINISTRATOR,
    #     ] or (old_status == ChatMember.RESTRICTED and old_is_member is True)
    #     is_member = new_status in [
    #         ChatMember.MEMBER,
    #         ChatMember.CREATOR,
    #         ChatMember.ADMINISTRATOR,
    #     ] or (new_status == ChatMember.RESTRICTED and new_is_member is True)

    #     return was_member, is_member

    # def track_chats(update: Update, context: CallbackContext) -> None:
    #     """Tracks the chats the bot is in."""
    #     result = extract_status_change(update.my_chat_member)
    #     if result is None:
    #         return
    #     was_member, is_member = result

    #     # Let's check who is responsible for the change
    #     cause_name = update.effective_user.full_name

    #     # Handle chat types differently:
    #     chat = update.effective_chat
    #     if chat.type == Chat.PRIVATE:
    #         if not was_member and is_member:
    #             logger.info("%s started the bot", cause_name)
    #             context.bot_data.setdefault("user_ids", set()).add(chat.id)
    #         elif was_member and not is_member:
    #             logger.info("%s blocked the bot", cause_name)
    #             context.bot_data.setdefault("user_ids", set()).discard(chat.id)
    #     elif chat.type in [Chat.GROUP, Chat.SUPERGROUP]:
    #         if not was_member and is_member:
    #             logger.info("%s added the bot to the group %s",
    #                         cause_name, chat.title)
    #             context.bot_data.setdefault("group_ids", set()).add(chat.id)
    #         elif was_member and not is_member:
    #             logger.info("%s removed the bot from the group %s",
    #                         cause_name, chat.title)
    #             context.bot_data.setdefault(
    #                 "group_ids", set()).discard(chat.id)
    #     else:
    #         if not was_member and is_member:
    #             logger.info("%s added the bot to the channel %s",
    #                         cause_name, chat.title)
    #             context.bot_data.setdefault("channel_ids", set()).add(chat.id)
    #         elif was_member and not is_member:
    #             logger.info("%s removed the bot from the channel %s",
    #                         cause_name, chat.title)
    #             context.bot_data.setdefault(
    #                 "channel_ids", set()).discard(chat.id)

    # def show_chats(update: Update, context: CallbackContext) -> None:
        """Shows which chats the bot is in"""
        user_ids = ", ".join(
            str(uid) for uid in context.bot_data.setdefault("user_ids", set()))
        group_ids = ", ".join(
            str(gid) for gid in context.bot_data.setdefault("group_ids", set()))
        channel_ids = ", ".join(
            str(cid) for cid in context.bot_data.setdefault("channel_ids", set()))
        text = (
            f"@{context.bot.username} is currently in a conversation with the user IDs {user_ids}."
            f" Moreover it is a member of the groups with IDs {group_ids} "
            f"and administrator in the channels with IDs {channel_ids}."
        )
        update.effective_message.reply_text(text)

    """Start the bot."""
    MASTER = 'igor531205'
    global masters
    masters = [MASTER]
    global chats_users
    chats_users = dict()

    # Create the Updater and pass it your bot's token.
    TOKEN = '5484436077:AAHRLCdLdDzLyRbU2M3iWsRkOHIM_DmFQeE'
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # import logging

    # logging.basicConfig(
    #     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
    # )

    # logger = logging.getLogger(__name__)

    # Commands - answer in Telegram
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('kill', kill))

    # dispatcher.add_handler(CommandHandler("show_chats", show_chats))
    # dispatcher.add_handler(ChatMemberHandler(track_chats, ChatMemberHandler.MY_CHAT_MEMBER))

    def print_users(update: Update, context: CustomContext) -> None:
        """Show which users have been using this bot."""
        update.message.reply_text(
            'The following user IDs have used this bot: '
            f'{", ".join(map(str, context.bot_user_ids))}'
        )
    dispatcher.add_handler(CommandHandler("print_users", print_users))

    # Message for bot - answer in Telegram
    dispatcher.add_handler(MessageHandler(
        # TODO Filters.all & Filters.text
        ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print('Start programm')
    main()
