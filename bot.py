import telebot
import config
from parser import Parser

bot = telebot.TeleBot(config.TOKEN)


parser = Parser()

@bot.message_handler(commands=['start'])
def main(message):
	bot.send_message(message.chat.id, 'q!')


if __name__ == '__main__':
	bot.polling(none_stop=True)