
tasks = [
    "/add",
"/add завтра сделать задание",
"/add сделать задание завтра",
"/add завтра сделать важное задание",
"/add сделать важное задание завтра",
"/add завтра сделать задание @работа",
"/add сделать задание @работа завтра",
"/add завтра @работа сделать задание",
"/add завтра сделать задание @@важно",
"/add сделать задание @@важно завтра",
"/add завтра сделать важное задание @работа",
"/add сделать важное задание @работа завтра",
"/add завтра @работа сделать задание @@важно",
"/add завтра сделать задание @работа @@важно",
"/add сделать задание @@важно завтра @работа",
"/add завтра сделать важное задание @@важно",
"/add сделать важное задание @@важно завтра",
"/add завтра @@важно сделать задание @работа",
"/add завтра сделать задание @работа @@важно",
"/add сделать задание @@важно завтра @работа",
"/add завтра сделать важное задание @работа @@важно",
         ]

for _ in tasks:

    date = ""
    task = ""
    category = ""
    priority = ""

    spl_task = _.split()[1:]
    for word in spl_task:
        if word[0:2] == "@@":
            priority = word
        elif word[0:1] == "@":
            category = word
        elif date is "":
            date = word
        elif task is "":
            task = word
        else:
            task += " " + word

    print(f"Дата: {date:{15}} Задача: {task:{30}} Категория: {category:{20}} Приоритет: {priority}")

    # print(date, task, category, priority)
