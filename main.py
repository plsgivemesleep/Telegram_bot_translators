import logging
import translators as ts

from aiogram import Bot, Dispatcher, executor, types


# Уровень логирования (чето важное)
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера (чето важное)
bot = Bot(token="5174473999:AAFtdxxyOsQ3APxV9-bSQEbfFLtQk-xv20k")
dp = Dispatcher(bot)


# reply_markup=types.ReplyKeyboardRemove() - удаляет клавиатуру

# reply_markup = mn.*** - выводим клавиатуру из mn которая в свою очередь достает клавиатуру из menu.py

# @dp.message_handler(commands=['***'])
# async def send_welcome(message: types.Message):             - это основа любого сообщения
#     await message.answer("***")



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
	await message.answer("Это переводчик любого текста с любого языка на русский.")
	await message.answer("Команда  для перевода ts en \"текст\"")
	await message.answer("Команда  для перевода ts \"текст\" автоматический распознает язык.")


@dp.message_handler(commands=['help'])
async def info(message: types.Message):
	await message.answer("Команда для перевода. \n\
		ts en \"текст\"")
	await message.answer("Вместо \"en\" можно использовать другой язык. Вот список:\n\
		ab: Абхазский\n\
		av: Аварский\n\
		bg: Болгарский\n\
		hu: Венгерский\n\
		el: Греческий (Новогреческий)\n\
		es: Испанский\n\
		it: Итальянский\n\
		zh: Китайский\n\
		lv: Латышский\n\
		lt: Литовский\n\
		de: Немецкий\n\
		nl: Нидерландский (Голландский)\n\
		pl: Польский\n\
		pt: Португальский\n\
		ro: Румынский\n\
		sk: Словацкий\n\
		sl: Словенский\n\
		fi: Финский\n\
		fr: Французский\n\
		cs: Чешский\n\
		sv: Шведский\n\
		et: Эстонский\n\
		ja: Японский\n\
		en: Английский")

spln = ["ab", "av", "bg", "hu", "el", "es", "it", "zh", "lv", "lt", "de", "nl", "pl", "pt", "ro", "sk", "sl", "fi", "fr", "cs", "sv", "et", "ja","en"]

@dp.message_handler(commands=['info'])
async def help(message: types.Message):
    await message.answer("Я перевожу текст отправленный мне.")

@dp.message_handler()
async def echo_message(message: types.Message):
	text = message.text
	text = text.split()
	if text[0] != "ts":
		await message.answer("Убедитесь что правильно ввели команду")
	elif text[1] in spln:
		trln = text[1]
		text.remove("ts")
		text.remove(text[0])
		text = " ".join(text)
		tstext = (ts.google(text, to_language='ru', from_language=trln))
		await message.answer(tstext)
	else:
		text.remove("ts")
		text = " ".join(text)
		tstext = (ts.google(text, to_language='ru'))
		await message.answer(tstext)



# Запуск long-polling (чето важное)
if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)