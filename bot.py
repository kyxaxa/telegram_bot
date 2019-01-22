import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

settings = {
    'TELEGRAM_API_KEY':'',      # setup your api key
}

from settings import *

logging.basicConfig(
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO,
    filename='bot.log'
)


def main():
    updater = Updater(settings['TELEGRAM_API_KEY'])

    updater.dispatcher.add_handler(CommandHandler("start", greet_user))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    updater.start_polling()
    updater.idle()


def greet_user(bot, update):
    logging.info('{} присоединился'.format(update.message.from_user.name))
    reply_text = [
        'Привет, {}! Это очень простой бот.'.format(update.message.from_user.first_name),
        '',
        'Пока он умеет только дублировать сообщения от пользователя.',
        '',
        'Напиши что-нибудь и увидишь.'
    ]

    update.message.reply_text('\n'.join(reply_text))


def chat(bot, update):
    user_text = update.message.text
    logging.info('"{}" {}'.format(user_text, update.message.from_user.name))
    update.message.reply_text('Echo "{}"'.format(user_text))


if __name__ == '__main__':
    logging.info('Bot started')
    main()
