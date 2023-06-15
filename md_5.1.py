# Выводить ошибку при добавлении задачи, в которой меньше 3-х символов.
# Печатать задачи на несколько дат: принимать в команде print не одну дату, а произвольное количество.
# При добавлении задачи учитывать отдельным параметром ее категорию. При выводе печатать
# категории задач со знаком @: Помыть посуду @Домашние дела.

import telebot
from random import choice
import pprint
import token

token = token.token

bot = telebot.TeleBot(token)
RANDOM_TASKS = ['Написать Гвидо письмо', 'Выучить Python', 'Записаться на курс в Нетологию',
                'Посмотреть 4 сезон Рик и Морти']
RANDOM_DAYS = ["сегодня", "завтра", "послезавтра"]
todos = dict()

HELP = '''
Список доступных команд:
* /showtoday  - печать задачи на сегодня
* /showall - печатать все задачи
* /show - печать задачи на определенный день
* /add - добавить задачу
* /random - добавить на сегодня случайную задачу
* /help - Напечатать help
'''


def add_todo(date, task):
    date = date.lower()
    if todos.get(date) is not None:
        todos[date].append(task)
    else:
        todos[date] = [task]


@bot.message_handler(commands=['help'])
def _help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=['random'])
def random(message):
    task = choice(RANDOM_TASKS)
    day = choice(RANDOM_DAYS)
    add_todo(day, task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на {day}')


@bot.message_handler(commands=['add'])
def add(message):
    if message.text.count(" ") > 1:
        _, date, tail = message.text.split(maxsplit=2)
        if len(tail) > 3:
            task = ' '.join([tail])
            add_todo(date, task)
            bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date}')
        else:
            bot.send_message(message.chat.id, f'Описание задачи слишком короткое, попробуйте еще раз')
    elif message.text.count(" ") == 1:
        bot.send_message(message.chat.id, f'Формат команды некорректный, попробуйте еще раз')
    else:
        bot.send_message(message.chat.id, f'Команда без параметров, выполняю сценарий случайной задачи')
        random(message)


@bot.message_handler(commands=['showtoday'])
def print_today(message):
    date = "сегодня"
    if date in todos:
        tasks = f'Задачи на {date}:\n'
        for task in todos[date]:
            tasks += f'[ ] {task}\n'
    else:
        tasks = 'На сегодня нет задач'
    bot.send_message(message.chat.id, tasks)


@bot.message_handler(commands=['showall'])
def print_all(message):
    exsist_days = list(todos.keys())
    if len(exsist_days) == 0:
        bot.send_message(message.chat.id, "Задач нет во всем календаре")
    for date in exsist_days:
        tasks = f'Задачи на {date}:\n'
        for task in todos[date]:
            tasks += f'[ ] {task}\n'
        bot.send_message(message.chat.id, tasks)
    pprint.pprint(todos)


@bot.message_handler(commands=['show'])
def print_some_days(message):
    if message.text.count(" ") >= 1:
        dates = message.text.split()
        print(dates)
        dates = dates[1:]
        for date in dates:
            if date in todos:
                tasks = f'Задачи на {date}:\n'
                for task in todos[date]:
                    tasks += f'[ ] {task}\n'
            else:
                tasks = f'На дату {date} нет задач'
            bot.send_message(message.chat.id, tasks)
    else:
        tasks = 'Некорректный запрос'
        bot.send_message(message.chat.id, tasks)


bot.polling(none_stop=True)
