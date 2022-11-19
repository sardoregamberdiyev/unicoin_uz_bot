from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater, CallbackQueryHandler

from services import *


def inline_btn(btn_type=None, ctg=None, tip=None, bts=None):
    if btn_type == "menu":
        btn = [
            [InlineKeyboardButton("UniCoin orqali harid qilish", url="https://unicoinuz.netlify.app/")],
            ]
    else:
        btn = [
            [InlineKeyboardButton("UniCoin orqali harid qilish", url="https://unicoinuz.netlify.app/")],
        ]
    return InlineKeyboardMarkup(btn)


try:
    create_table()
except Exception as e:
    pass


def start(update, context):
    user = update.message.from_user
    if get_one(user.id):
        a = update.message.from_user.first_name
        print(a)
    else:
        create_user(user_id=user.id, username=user.username)
    update.message.reply_text("Assalomu Alaykum. Keling, boshlaymiz {} 😁 \n\nAjoyib mahsulotlarga buyurtma berish "
                              "uchun "
                              "quyidagi tugmani "
                              "bosing ❗️\nYoki saytdan UniCoin ga harid qiling."
                              .format(update.message.from_user.first_name),
                              reply_markup=inline_btn("menu"), parse_mode="HTML")


def main():
    Token = "5949452424:AAH34pIhUWxBaAUdFIJed8Si2uxYnf9A2Q8"
    updater = Updater(Token)

    updater.dispatcher.add_handler(CommandHandler("start", start))
    # updater.dispatcher.add_handler(CallbackQueryHandler(send_document))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
