# функция для отображения заметок

# Функция вывода на экран одной страницы заметок
def display_page(notes, page):
    global end_index  # переменная для определения окончания вывода

    start_index = 0 + page * 5 # начало выводимого диапазона
    end_index = 5 + page * 5   # конец выводимого диапазона

    # Заголовок страницы с ее номером
    print(f'{"_" * 10} {'Страница'} {str(page + 1)} {"_" * 10}')
    # вывод 5 заметок
    for index, note in enumerate(notes[start_index:end_index], start = start_index+1 ):
        print(f"""      
        Номер заметки: {index}
        Имя пользователя: {note["username"]}
        Заголовок: {note["title"]}
        """)

# Функция, вызывающая
def display_notes(notes, page_number):
    if len(notes) == 0:
        print("Список заметок пуст")
    else:
        while True:
            display_page(notes, page_number )
            if end_index >= len(notes):
                break
            else:
                page_number = page_number + 1

if __name__ == '__main__':

    # Определяем список заметок
    notes = [
        {"username": "Иван", "title": "Расходы"},
        {"username": "Мария", "title": "Кастинг"},
        {"username": "Иван", "title": "Выходные"},
        {"username": "Алексей", "title": "Поездка в горы"},
        {"username": "Мария", "title": "Свадьба"},
        {"username": "Елена", "title": "Учеба"},
        {"username": "Петр", "title": "Встреча с друзьями"},
        {"username": "Иван", "title": "Поход"},
        {"username": "Иван", "title": "Сессия"},
        {"username": "Петр", "title": "Учеба"},
    ]
    n = 0
    end_index = 0
    display_notes(notes=notes, page_number=n)
