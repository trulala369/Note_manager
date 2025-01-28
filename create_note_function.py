# Функция создания заметки

def create_note():
    from datetime import datetime
    date_now = datetime.now().strftime('%d-%m-%Y')  # Текущая дата

    # список для добавленных заметок
    note_dict = []
    while True:
        n = 0
        new = input('\nХотите ввести новую заметку? (да/нет)\n ').lower()
        if not new or new == 'нет':  # если ввод пустой или 'нет', выход
            break
            # return note_dict
        else:
            while new != 'да':  # если введено еще что-то кроме 'да'
                print('Это не похоже на "да" или "нет", попробуйте еще раз')
                new = input('\nХотите ввести новую заметку? (да/нет) ').lower()

            username = input('Введите ваше имя: ').strip()
            while not username:  # обработка пустого ввода
                print('Имя пользователя не может быть пустым')
                username = input('\nВведите ваше имя: ').strip()

            title = input('Введите название заметки: ').strip()
            while not title:  # обработка пустого ввода
                print('Название заметки не может быть пустым')
                title = input('\nВведите название заметки: ').strip()

            # Продолжаем ввод
            content = input('Введите текст заметки: ').strip()
            while not content:  # обработка пустого ввода
                print('Содержание заметки не может быть пустым')
                content = input('\nВведите текст заметки: ').strip()
            # продолжаем ввод
            status_ = ['новая', 'в процессе', 'выполнено']  # определяем список со статусами
            status = input(f'Введите статус заметки ({','.join(status_)}): ').strip().lower()
            while status not in status_:  # обработка ошибки ввода
                print(f'Ошибка! Возможные варианты: {', '.join(status_)}')
                status = input(f'\nВведите статус заметки ({','.join(status_)}): ').strip().lower()

            # Дата создания заметки-текущая дата
            created_date = date_now
            print('Дата начала работы: сегодня ' + created_date)  # вывод текущей даты
            # Продолжаем ввод
            issue_date = input('Введите дату дедлайна (дд-мм-гггг): ').strip()
            while True:  # обработка ошибки ввода при помощи функции
                try:
                    datetime.strptime(issue_date, "%d-%m-%Y")
                    break
                except ValueError:
                    print('Ошибка при вводе даты! Используйте формат (дд-мм-гггг)')
                    issue_date = input('Введите дату дедлайна (дд-мм-гггг): ').strip()

            # вывод новой заметки
            #n = n + 1
            print(f'\n Ваша новая заметка:\n{"-"*25}\n Имя: {username} \n Заголовок: {title} \n Описание: {content}')
            print(f' Статус: {status}\n Дата создания: {created_date}\n Дедлайн: {issue_date}')

            # формирование словаря из добавленной заметки
            note_dict.append({
                "username": username,
                "title": title,
                "content": content,
                "status": status,
                "created_date": created_date,
                "issue_date": issue_date
            })

    return note_dict

if __name__ == "__main__":
    # Импорт необходимых модулей
    from datetime import datetime

    date_now = datetime.now().strftime('%d-%m-%Y')  # Текущая дата
    print('Сегодня ', date_now)
    print('Добро пожаловать в "менеджер заметок"!')

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

    note = create_note()
    notes.extend(note)
    print('\nСписок введенных заметок:')
    print(note)


