import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "BOT_TOKEN"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    """
    This handler receives the text entered by the user and sends it as a reverse message
    """
    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
