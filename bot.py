import telebot
import requests
import config

from parse_ctf import Parser


bot = telebot.TeleBot(config.TOKEN)
parser = Parser()


@bot.message_handler(commands=['start'])
def main(message):
	bot.send_message(message.chat.id, 'Привет! Я бот команды IDCZ!')


@bot.message_handler(commands=['list'])
def get_list_ctf(message):
	bot.send_message(message.chat.id, parser.get_ctf_list())


@bot.message_handler(commands=['next'])
def get_next_ctf(message):
	bot.send_message(message.chat.id, parser.get_next_ctf())


@bot.message_handler(commands=['top'])
def get_idcz_place(message):
	bot.send_message(message.chat.id, parser.get_team_rank())


@bot.message_handler(content_types=['new_chat_members'])
def new_member_handler(message):
	username = message.new_chat_members[0].first_name
	bot.send_message(message.chat.id, f"Привет, {username}!")


if __name__ == '__main__':
	bot.polling(none_stop=True)
