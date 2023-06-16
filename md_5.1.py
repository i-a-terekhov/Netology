# Выводить ошибку при добавлении задачи, в которой меньше 3-х символов.
# Печатать задачи на несколько дат: принимать в команде print не одну дату, а произвольное количество.
# При добавлении задачи учитывать отдельным параметром ее категорию. При выводе печатать
# категории задач со знаком @: Помыть посуду @Домашние дела.

import telebot
from random import choice
import re
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
    "Личное",
    "Семья",
    "Финансы",
    "Хобби",
    "Путешествия",
    "Образование",
    "Домашние",
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
/add [дата] [задача] [@категория] [@@приоритет] - добавить задачу
/random - добавить случайную задачу на случайный день
/random_x10 - добавить 10 случайных задач 
/help - Напечатать help
'''


def add_task(date, task, category=None, priority=None):
    date = date.lower()
    if schedule.get(date) is not None:
        schedule[date].append([category, priority, task])
    else:
        schedule[date] = [[category, priority, task]]


def loger(message, *args):
    print("Фиксируем сообщение от пользователя:")
    print(message.text)
    print("Полученные арги")
    print(*args)


@bot.message_handler(commands=['help'])
def _help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=['random'])
def random(message, print_report=True):
    day = choice(RANDOM_DAYS)
    category = choice(CATEGORIES)
    priority = choice(PRIORITIES)
    task = choice(RANDOM_TASKS)
    add_task(day, task, category=category, priority=priority)
    if print_report:
        bot.send_message(message.chat.id, f'Задача {task} добавлена на {day}, приоритет {priority}, категория {category}')


@bot.message_handler(commands=['random_x10'])
def random_x10(message):
    for i in range(10):
        random(message=message, print_report=False)
    bot.send_message(message.chat.id, f'Добавлено 10 случайных задач, посмотреть все задачи /showall')


#TODO Выделить обработку регулярками в отдельную функцию, возвражающую либо текст, либо None


def message_split(message):
    

@bot.message_handler(commands=['add'])
def add(message):
    if " " in message.text:
        mess_text = message.text.split(maxsplit=1)[1]
        date = re.match(r'[^ ]*', mess_text)
        task = re.search(r'(?<= )[^@]+(?!@)', mess_text)
        category = re.search(r'(?<=@)[^@| ]+(?!@)', mess_text)
        priority = re.search(r'(?<=@@)[^@| ]+(?!@)', mess_text)

        loger(message, date.group(0), task, category, priority)

        if date is None or task is None:
            bot.send_message(message.chat.id, f'Формат команды некорректный, попробуйте еще раз')
        elif len(task.group(0)) > 3:
            add_task(date.group(0), task.group(0), category=category, priority=priority)
            bot.send_message(message.chat.id, f'На {date} добавлена задача {task} с категорией {category} и приоритетом {priority}')
        else:
            bot.send_message(message.chat.id, f'Описание задачи слишком короткое, попробуйте еще раз')
    else:
        bot.send_message(message.chat.id, f'Формат команды некорректный, не найдены пробелы')

#TODO сделать рефактор функций печати: вынести печать единичного таска в отдельную функцию
#TODO сделать функцию сборки тасков по дню или категории для печати в одном сообщении

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
