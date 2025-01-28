# Функция обновления заметки

import datetime

def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False

def update_note(note):
    print("=== Обновление заметки ===\n")
    print("Текущие данные заметки:")
    for key, value in note.items():
        print(f"{key}: {value}")

    updatable_fields = ["username", "title", "content", "status", "issue_date"]
    value_status = ['новая', 'в процессе', 'выполнено']
    while True:
        field = input(f"\nКакие данные вы хотите обновить?\n"
                      f"Выберите из списка:{', '.join(updatable_fields)}: ").strip().lower()
        if field not in updatable_fields:
            print(f"Ошибка: Поле '{field}' не найдено. Пожалуйста, выберите поле из списка.")
            continue

        if field == "issue_date":
            new_value = input(f"Введите новое значение для поля {field} (дд-мм-гггг): ").strip()
            while not validate_date(new_value):
                new_value = input("Ошибка: Неверный формат даты. Используйте формат 'дд-мм-гггг': ")
                continue
        elif field == "status":
            # проверка на доступный статус
            new_value = input(f"Введите новое значение для поля {field}.\n"
                              f"Возможные значения: новая, в процессе, выполнено: ").strip().lower()
            while not new_value or new_value not in value_status:
                new_value = input(f"Ошибка!Возможные значения: новая, в процессе, выполнено: ")
                continue
        else:
            new_value = input(f"Введите новое значение для {field}: ").strip()
            while not new_value:
                print(f"Ошибка! Значение для поля {field} не может быть пустым.")
                new_value = input(f"Введите новое значение для {field}: ").strip()
                continue

        note[field] = new_value
        print(f"\nЗаметка успешно обновлена: {field} -> {new_value}")
        print('-'*50)
        return note

if __name__ == "__main__":
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

    updated_note = update_note(note)
    print("\nОбновлённая заметка:")
    print(updated_note)
