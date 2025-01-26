# функция для отображения заметок

# Функция вывода на экран одной страницы заметок
def display_page(notes, page):
    global end_index # переменная заодно служит для определения окончания вывода
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
        display_page(notes, page_number)

#notes = []
#if name == '__main__':

# Определяем список заметок
notes = [
    {"username": "1", "title": "CV"},
    {"username": "2", "title": "CV"},
    {"username": "3", "title": "CV"},
    {"username": "4", "title": "CV"},
    {"username": "5", "title": "CV"},
    {"username": "6", "title": "CV"},
    {"username": "7", "title": "CV"},
    {"username": "8", "title": "CV"},
    {"username": "9", "title": "CV"},
    {"username": "10", "title": "CV"},
]
n = 0
end_index = 0
# Цикл вывода страниц пока не закончатся заметки
while True:
    display_notes(notes = notes, page_number = n)
    if  end_index >= len(notes):
       break
    else:
        n = n + 1
