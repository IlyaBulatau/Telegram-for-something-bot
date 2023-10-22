from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    filters,
    MessageHandler,
    CallbackQueryHandler,
)
from telegram import Update

import logging

from keyboards import keyboard_for_some_choose as KB
from config import Settings


logging.basicConfig(
    style="{",
    format="{asctime} | {name} | {levelname} | {message}",
    level=logging.INFO,
)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="Do choose", reply_markup=KB()
    )


async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text=" ".join(context.args)
        )
        return
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Not args")


async def unknow_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="Unknow message, sorry"
    )


async def choose_option_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    callback_query = update.callback_query
    callback_data: str = callback_query.data

    await callback_query.edit_message_text(text=f"Your choose - {callback_data}")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text
    )


if __name__ == "__main__":
    token = Settings.token
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler(command="start", callback=start_command))
    app.add_handler(CommandHandler(command="info", callback=info_command))
    app.add_handler(CallbackQueryHandler(callback=choose_option_handler))
    app.add_handler(MessageHandler(filters=filters.COMMAND, callback=unknow_command))
    app.add_handler(MessageHandler(filters=filters.TEXT, callback=echo))
    app.run_polling()
