import logging
# import asyncio

from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler, InlineQueryHandler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm bot, please talk to me!")


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        text_caps = " ".join(context.args).upper()
    else:
        text_caps = "empty message"

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = f"список команд:\n\n/start - начать диалог\n/caps text - получить text в верхнем регистре"

    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


async def inline_caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title="Caps",
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)


if __name__ == "__main__":
    application = ApplicationBuilder().token("6122726933:AAHVD9YdOReYX2-O2BvFe0k5YWiiQCSzoLA").build()

    start_handler = CommandHandler("start", start)
    caps_handler = CommandHandler("caps", caps)
    help_handler = CommandHandler("help", help)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    inline_caps_handler = InlineQueryHandler(inline_caps)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    application.add_handler(start_handler)
    application.add_handler(caps_handler)
    application.add_handler(help_handler)
    application.add_handler(echo_handler)
    application.add_handler(inline_caps_handler)
    application.add_handler(unknown_handler)

    application.run_polling()
