# функция для отображения заметок
from selectors import SelectSelector


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

    # список заметок для тестирования
    notes = [
        {'username': 'Иван', 'title': 'Расходы', 'content': 'Купить продукты на неделю', 'status': 'новая',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Мария', 'title': 'Кастинг', 'content': 'Выучить текст', 'status': 'выполнено',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Иван', 'title': 'Выходные', 'content': 'Отключить тлфн', 'status': 'новая',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Алексей', 'title': 'Поездка в горы', 'content': 'Позвонить Олегу', 'status': 'новая',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Мария', 'title': 'Свадьба', 'content': 'Купить туфли', 'status': 'новая',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Елена', 'title': 'Учеба', 'content': 'Выполнить задание 5', 'status': 'новая',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Петр', 'title': 'Свидание', 'content': 'Купить цветы', 'status': 'новая',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Иван', 'title': 'Поход', 'content': 'Купить палатку', 'status': 'новая',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'}
    ]
    n = 0
    end_index = 0
    #display_notes(notes=notes, page_number=n)
    display_notes(notes, n)
