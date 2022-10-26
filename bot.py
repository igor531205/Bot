def botik():
    """Start the bot."""
    from telegram import ForceReply, Update
    from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a message when the command /start is issued."""
        user = update.effective_user
        await update.message.reply_html(
            rf"Hi {user.mention_html()}!",
            # reply_markup=ForceReply(selective=True),
        )

    async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a message when the command /help is issued."""
        await update.message.reply_text("Help!")

    async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Echo the user message."""
        await update.message.reply_text(update.message.text)

    TOKEN = '5484436077:AAHRLCdLdDzLyRbU2M3iWsRkOHIM_DmFQeE'

    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


def bot():
    """telegram bot.
    """

    from telegram import Update
    from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

    async def help(update: Update, context: CallbackContext):
        """Command "Help" for user.
        """

        log([update.effective_user.id,
            update.effective_user.first_name,
            update.message.text
             ])

        command = ['/hello',
                   '/time',
                   '/add',
                   '/sub',
                   '/div',
                   '/mult'
                   ]

        await update.message.reply_text('\n'.join(command))

    async def hello(update: Update, context: CallbackContext):
        """Command "hello" for user.
        """

        log([update.effective_user.id,
            update.effective_user.first_name,
            update.message.text
             ])

        msg = f'Hello {update.effective_user.first_name}'

        await update.message.reply_text(msg)

    async def time(update: Update, context: CallbackContext):
        """Command "time" for user.
        """

        from datetime import datetime

        log([update.effective_user.id,
            update.effective_user.first_name,
            update.message.text
             ])

        msg = f'Now time {datetime.now():%Y.%m.%d %H:%M}'

        await update.message.reply_text(msg)

    async def add(update: Update, context: CallbackContext):
        """Command "add" for user.
        """

        log([update.effective_user.id,
            update.effective_user.first_name,
            update.message.text
             ])

        msg = update.message.text.split()

        if len(msg) == 3:

            num1 = float(msg[1])
            num2 = float(msg[2])

            await update.message.reply_text(
                f'{num1} + {num2} = {num1 + num2}')

        else:

            msg = [
                'Incorrect enter!!!',
                'For exemple, enter:',
                '/add 1 1']

            await update.message.reply_text(
                '\n'.join(msg))

    async def sub(update: Update, context: CallbackContext):
        """Command "sub" for user.
        """

        log([update.effective_user.id,
            update.effective_user.first_name,
            update.message.text
             ])

        msg = update.message.text.split()

        if len(msg) == 3:

            num1 = float(msg[1])
            num2 = float(msg[2])

            await update.message.reply_text(
                f'{num1} - {num2} = {num1 - num2}')

        else:

            msg = [
                'Incorrect enter!!!',
                'For exemple, enter:',
                '/sub 1 1']

            await update.message.reply_text(
                '\n'.join(msg))

    async def div(update: Update, context: CallbackContext):
        """Command "div" for user.
        """

        log([update.effective_user.id,
            update.effective_user.first_name,
            update.message.text
             ])

        msg = update.message.text.split()

        if len(msg) == 3:

            num1 = float(msg[1])
            num2 = float(msg[2])

            await update.message.reply_text(
                f'{num1} / {num2} = {num1 / num2}')

        else:

            msg = [
                'Incorrect enter!!!',
                'For exemple, enter:',
                '/div 1 1']

            await update.message.reply_text(
                '\n'.join(msg))

    async def mult(update: Update, context: CallbackContext):
        """Command "mult" for user.
        """

        log([update.effective_user.id,
            update.effective_user.first_name,
            update.message.text
             ])

        msg = update.message.text.split()

        if len(msg) == 3:

            num1 = float(msg[1])
            num2 = float(msg[2])

            await update.message.reply_text(
                f'{num1} * {num2} = {num1 * num2}')

        else:

            msg = [
                'Incorrect enter!!!',
                'For exemple, enter:',
                '/mult 1 1']

            await update.message.reply_text(
                '\n'.join(msg))

    # Bot username: @GB_for_HomeWork_bot
    app = ApplicationBuilder().token('5484436077:AAHRLC'
                                     + 'dLdDzLyRbU2M3iW'
                                     + 'sRkOHIM_DmFQeE'
                                     ).build()

    print('Start "CommandHandler"')

    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('hello', hello))
    app.add_handler(CommandHandler('time', time))
    app.add_handler(CommandHandler('add', add))
    app.add_handler(CommandHandler('sub', sub))
    app.add_handler(CommandHandler('div', div))
    app.add_handler(CommandHandler('mult', mult))

    app.run_polling()


def log(data_log: list):
    """log to file.
    """

    from datetime import datetime

    with open('db.csv', 'a') as data:
        data.write(','.join([f'{datetime.now():%Y.%m.%d %H:%M}']
                            + [str(item) for item in data_log])
                   + '\n')


if __name__ == '__main__':

    from os import system

    # system('cls')
    botik()
