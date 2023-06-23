from random import choice
import pprint

RANDOM_DAYS = ["сегодня", "завтра", "послезавтра", "после второго пришествия", "после майских"]
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
RANDOM_CATEGORIES = [
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
RANDOM_PRIORITIES = [
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

for _ in range(100):
    date = choice(RANDOM_DAYS)
    task = choice(RANDOM_TASKS)
    category = choice(RANDOM_CATEGORIES)
    priority = choice(RANDOM_PRIORITIES)

    if date in schedule:
        schedule[date].append({"category": category, "priority": priority, "task": task})
    else:
        schedule[date] = [{"category": category, "priority": priority, "task": task}]

pprint.pprint(schedule)
