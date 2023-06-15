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
RANDOM_TASKS = [
    "Погулять 30 минут",
    "Сделать зарядку",
    "Проверить почту",
    "Составить план на день",
    "Вынести мусор",
    "Почистить зубы",
    "Прочитать главу книги",
    "Подкачать велосипед",
    "Забрать посылку",
    "Позвонить маме",
    "Купить продукты",
    "Заняться медитацией",
    "Сделать уборку",
    "Подготовить обед",
    "Написать отчет",
    "Записать видео",
    "Прогуляться по парку",
    "Починить сломанную лампочку",
    "Провести совещание",
    "Оплатить счета",
    "Сделать маникюр",
    "Приготовить чай",
    "Почитать новости",
    "Выучить новое слово",
    "Написать письмо другу",
    "Заняться йогой",
    "Посадить цветы",
    "Сделать закупки",
    "Заказать такси",
    "Сходить на встречу с коллегами",
    "Забронировать отпуск",
    "Сделать фотографии",
    "Посмотреть новый фильм",
    "Подготовиться к презентации",
    "Сходить в спортзал",
    "Прочитать статью",
    "Составить список дел на следующую неделю",
    "Проверить запасы продуктов",
    "Приготовить ужин",
    "Почистить окна",
    "Выучить новую компьютерную программу",
    "Сделать заметки на встрече",
    "Организовать посиделку с друзьями",
    "Заказать еду на доставку",
    "Найти новую книгу для чтения",
    "Составить бюджет на месяц",
    "Проверить работу электронной почты",
    "Сделать звонок клиенту",
    "Подготовиться к собеседованию"
]
RANDOM_DAYS = ["сегодня", "завтра", "послезавтра", "после второго пришествия", "после майских"]
CATEGORIES = [
    None,
    "Здоровье",
    "Работа",
    "Личное развитие",
    "Семья",
    "Финансы",
    "Хобби",
    "Путешествия",
    "Образование",
    "Домашние дела",
    "Творчество"
]
PRIORITIES = [
    None,
    "Низкая",
    "Средняя",
    "Высокая",
    "Критическая",
    "Срочная",
    "Обычная",
    "Неотложная",
    "Важная",
    "Неважная",
    "Ключевая"
]

schedule = {}

HELP = '''
Список доступных команд:
/showtoday  - печать задачи на сегодня
/showall - печатать все задачи
/show [дата] - печать задачи на определенный день
/add [дата] [задача] - добавить задачу
/random - добавить случайную задачу на случайный день
/random_x10 - добавить 10 случайных задач 
/help - Напечатать help
'''


def add_task(date, task, category=None, priority=None):
    date = date.lower()
    if schedule.get(date) is not None:
        schedule[date].append(task)
    else:
        schedule[date] = [task]


@bot.message_handler(commands=['help'])
def _help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=['random'])
def random(message, print_report=True):
    task = choice(RANDOM_TASKS)
    day = choice(RANDOM_DAYS)
    #TODO после изменения add_task, добавить рандомные категории и важности для дел
    add_task(day, task)
    if print_report:
        bot.send_message(message.chat.id, f'Задача {task} добавлена на {day}')


@bot.message_handler(commands=['random_x10'])
def random_x10(message):
    for i in range(10):
        random(message=message, print_report=False)
    bot.send_message(message.chat.id, f'Добавлено 10 случайных задач, посмотреть все задачи /showall')


@bot.message_handler(commands=['add'])
def add(message):
    if message.text.count(" ") > 1:
        _, date, tail = message.text.split(maxsplit=2)
        if len(tail) > 3:
            task = ' '.join([tail])
            add_task(date, task)
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
    if date in schedule:
        tasks = f'Задачи на {date}:\n'
        for task in schedule[date]:
            tasks += f'[ ] {task}\n'
    else:
        tasks = 'На сегодня нет задач'
    bot.send_message(message.chat.id, tasks)


@bot.message_handler(commands=['showall'])
def print_all(message):
    exsist_days = list(schedule.keys())
    if len(exsist_days) == 0:
        bot.send_message(message.chat.id, "Задач нет во всем календаре")
    for date in exsist_days:
        tasks = f'Задачи на {date}:\n'
        for task in schedule[date]:
            tasks += f'[ ] {task}\n'
        bot.send_message(message.chat.id, tasks)
    pprint.pprint(schedule)


@bot.message_handler(commands=['show'])
def print_some_days(message):
    if message.text.count(" ") >= 1:
        dates = message.text.split()
        print(dates)
        dates = dates[1:]
        for date in dates:
            if date in schedule:
                tasks = f'Задачи на {date}:\n'
                for task in schedule[date]:
                    tasks += f'[ ] {task}\n'
            else:
                tasks = f'На дату {date} нет задач'
            bot.send_message(message.chat.id, tasks)
    else:
        tasks = 'Некорректный запрос'
        bot.send_message(message.chat.id, tasks)


bot.polling(none_stop=True)
