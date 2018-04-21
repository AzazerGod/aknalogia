from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
import wikipedia
import time as tm
import requests
import json
from time import gmtime, strftime
from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler

def main():
    updater = Updater("593544737:AAHMZ1ytEyyU3cqnxwYFvl0zHwaqnMzZhko")

    dp = updater.dispatcher

    conv_wiki = ConversationHandler(
        entry_points=[CommandHandler("start", start)],

        states={
            1: [MessageHandler(Filters.text, wikipod, pass_user_data=True)],

        },

        fallbacks=[CommandHandler('fgdfdfff', stop)]
    )
    dp.add_handler(conv_wiki)
    dp.add_handler(CommandHandler("start", start))
    wikipedia.set_lang("ru")
    updater.start_polling()
    updater.idle()

def start(bot, update):
    update.message.reply_text(
        "Введите информацию")
    return 1

def wikipod(bot ,updater, user_data):
    user_data['Information'] = updater.message.text
    try:
        ny = wikipedia.page(user_data['Information'])
        user_data['database'] = ny
        updater.message.reply_text(user_data['database'].title)
        try:
            bot.sendPhoto(
                updater.message.chat.id,
                user_data['database'].images[0]
            )
            updater.message.reply_text(wikipedia.summary(user_data['Information']))
            updater.message.reply_text("А вот ссылка на оригинал,там информации больше!")
            updater.message.reply_text(user_data['database'].url)
            return 1
        except:
            updater.message.reply_text(wikipedia.summary(user_data['Information']))
            updater.message.reply_text("А вот ссылка на оригинал,там информации больше!")
            updater.message.reply_text(user_data['database'].url)
            return 1
    except:
        updater.message.reply_text("Такую Информацию я не нашла!")
        return 1

def stop(bot, update):
    update.message.reply_text(
        "LDSGSLHJFHFD")
    return ConversationHandler.END

if __name__ == '__main__':

    main()
