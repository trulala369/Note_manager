# Функция для поиска по заметкам

# Функция, принимающая ключевое слово и статус, если есть
# Поиск заметок и добавление найденных в список
def search_notes_(notes, keyword = None, status = None):
    fields_for_search = ["title", "content", "username"] # в этих полях ищем ключевое слово
    found_notes = []  # список для найденных заметок

    for note in notes:
        keyword_criteria = False # переменные для осуществления поиска
        status_criteria = False  # по ключевому слову и по статусу

        if keyword is not None: # если поиск по ключевому слову
            for field in fields_for_search:
                if note[field].lower().find(keyword) != -1:
                    keyword_criteria = True      # ключевое слово найдено

                    if  input_crit == 1 :        # если ищем только по ключевому слову,то
                        found_notes.append(note) # добавляем заметку в список
                    break    # если ключевое слово нашлось, покидаем цикл

        if status is not None: # если поиск по статусу
            if note["status"] == status:
                status_criteria = True  # статус найден
                if  input_crit == 2:           # если ищем только по статусу,то
                    found_notes.append(note)   # добавляем заметку в список
                
        if  input_crit == 3: # если ищем по ключевому слову и по статусу
            #  если найдены и ключевое слово и статус
            if keyword_criteria == True and status_criteria == True:
                found_notes.append(note)  # добавляем заметку в список

    # возвращаем список заметок
    return found_notes

def search_notes(notes):
    global input_crit

    print('\n=================== Поиск заметок ==================')
    print(f'По ключевому слову-1,по статусу-2,по обоим критериям-3\n' 
          f'Введите цифры от 1 до 3. Выход из поиска - пустой ввод')
    while True:
        input_crit = input('\nПо какому критерию ищем заметку? ').strip()

        if input_crit.isdecimal(): # если не сделана ошибка и введена цифра
            input_crit = int(input_crit)
        if not input_crit: # если пустой ввод
            print('Поиск окончен.')
            break
        elif input_crit == 1 : # отправляем в функцию поиска заметок ключевое слово
            input_word = input('Введите ключевое слово: ').strip().lower()
            found_notes = search_notes_(notes, keyword = input_word)
        elif input_crit == 2 : # отправляем в функцию поиска статус
            input_stat = input('Введите статус (новая,в процессе,выполнено): ').strip().lower()
            # Обработка ошибочного ввода
            while input_stat != 'новая' and  input_stat != 'в процессе' and input_stat != 'выполнено':
                print(f'Ошибка ввода! Статус {input_stat} не найден.')
                input_stat = input('Введите статус (новая,в процессе,выполнено): ').strip().lower()
            found_notes = search_notes_(notes, status = input_stat)
        elif input_crit == 3:   # отправляем в функцию поиска заметок оба критерия
            input_word = input('Введите ключевое слово: ').strip().lower()
            input_stat = input('Введите статус (новая,в процессе,выполнено): ').strip().lower()
            found_notes = search_notes_(notes, keyword=input_word, status=input_stat)
        else:    # если введено не 1, 2, 3
            print('Ошибка ввода. Повторите ввод')
            continue

        if found_notes == [] :   # если заметки не были найдены вывод сообщения
            print('Заметка не найдена')
        else:     # если заметки найдены, вывод на экран
            print('='*15 + ' Найдены заметки ' + '='*15)
            for i in found_notes:
                print(f"""
                Имя пользователя: {i['username']}
                Заголовок: {i['title']}
                Содержание: {i['content']}
                Статус: {i['status']}
                Дата создания: {i['created_date']}
                Дедлайн: {i['issue_date']}
                """)
                print("-"*50)

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

    input_crit = ''
    search_notes(notes )