import sqlalchemy.exc
import telebot
from sqlalchemy import select

import db
import utils

from os import environ
from parse_ctf import Parser

bot = telebot.TeleBot(environ.get('TOKEN'))
parser = Parser()
connection = db.engine.connect()


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет!\n\nЯ бот, который поможет тебе находить ближайшие CTF и отслеживать '
                                      'свой '
                                      'рейтинг!\n\nВведите /register "ссылка на команду на ctftime.org", что бы '
                                      'зарегистрироваться.')


@bot.message_handler(commands=['list'])
def get_list_ctf(message):
    bot.send_message(message.chat.id, parser.get_ctf_list())


@bot.message_handler(commands=['next'])
def get_next_ctf(message):
    bot.send_message(message.chat.id, parser.get_next_ctf())


@bot.message_handler(commands=['top'])
def get_command_place(message):
    try:
        user_id = message.from_user.id
        team_link = select(db.users.c.team_link).filter(db.users.c.id == user_id)
        team_link = connection.execute(team_link).fetchone()[0]
        bot.send_message(message.chat.id, parser.get_team_rank(team_link=team_link))
    except:
        bot.send_message(message.chat.id, "Похоже у меня не получилось найти твою ссылку на команду или возможно она "
                                          "неправильная")


@bot.message_handler(commands=['update'])
def update_team(message):
    team_link = utils.extract_arg(message.text)
    user_id = message.from_user.id

    try:
        query = db.users.update().where(db.users.c.id == user_id).values(team_link=team_link)
        connection.execute(query)
    except:
        bot.send_message(message.chat.id, "Что-то не получилось")
        return

    bot.send_message(message.chat.id, "Успех!")


@bot.message_handler(commands=['register'])
def register(message):
    try:
        team_link = utils.extract_arg(message.text)
        user_id = message.from_user.id
        user_name = message.from_user.username
        query = db.users.insert().values(id=user_id, name=user_name, team_link=team_link)
        connection.execute(query)
        bot.send_message(message.chat.id, "Ты успешно зарегистрировался!")
    except IndexError:
        bot.send_message(message.chat.id, "Забыл указать ссылку на команду")
    except sqlalchemy.exc.IntegrityError:
        bot.send_message(message.chat.id, 'Не, ну сорян, пока ты не можешь поменять свой команду')
    except:
        bot.send_message(message.chat.id, 'Что-то не получается...')


if __name__ == '__main__':
    bot.polling(none_stop=True)
