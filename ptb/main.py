from telegram.ext import (
                        ApplicationBuilder,
                        ContextTypes,
                        CommandHandler,
                        filters,
                        MessageHandler,
                        )
from telegram import Update

import logging

from config import Settings


logging.basicConfig(
    style='{',
    format="{asctime} | {name} | {levelname} | {message}",
    level=logging.INFO,  
)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="OK")


async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=" ".join(context.args))
        return
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Not args")


async def unknow_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Unknow message, sorry")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

if __name__ == "__main__":
    token = Settings.token
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler(command="start", callback=start_command))
    app.add_handler(CommandHandler(command="info", callback=info_command))
    app.add_handler(MessageHandler(filters=filters.COMMAND, callback=unknow_command))
    app.add_handler(MessageHandler(filters=filters.TEXT, callback=echo))
    app.run_polling()