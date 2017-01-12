from telegram.ext import Updater

updater = Updater(token='328623928:AAGiz2ZHVM2yDYe68Lo0w_3pF-JQHXtYtsI')
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Start Command

def start(bot, update):

	bot.sendMessage(
		chat_id = update.message.chat_id,
		pars_mode ='HTML',
		text = 'رنگ‌برند یک لیست از برندهای مطرح در ایران (چه ایرانی، چه خارجی) است. \n'
		'در این لیست، کد رنگ‌های رسمی برند‌ها برای طراحان وب فارسی و یا طراحان گرافیک آماده شده. \n '
		'منابع رنگ‌برند رو دانلود کنید /download \n'
		'یا اینکه نام برند مد نظر را نوشته تا کد  یا رو در اختیارتون بزاریم.',

		)

from telegram.ext import CommandHandler, MessageHandler, Filters

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()


# Download Command - download RangeBrand Zip file

def download(bot,update):

	bot.sendDocument(
		chat_id = update.message.chat_id,
		document = 'https://github.com/IKAcc/RangeBrand/archive/master.zip',
		caption = 'فایل زیپ شده رنگ برند',)

download_handler = CommandHandler('download', download)
dispatcher.add_handler(download_handler)

import json
from pprint import pprint
def color(bot, update,args):

	with open('rangeBrand.json') as request_brand:

		colors = json.load(request_brand)

	colors_list = colors[args]["colors"]
	colors_result = ' '.join(colors_list)

	bot.sendMessage(
		chat_id = update.message.chat_id,
		text = colors_result,
		)
color_handler = CommandHandler('color', color, pass_args = True)
dispatcher.add_handler(color_handler)



# Unknown color name 

def unknown(bot, update):

	bot.sendMessage(
		chat_id = update.message.chat_id,
		text = 'نام وارد شده معتبر نیست',
		)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)


