# Функция обновления заметки

import datetime

def validate_date(date_str):
    try:
        # дд-мм-гггг
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
        #print(f"\nЗаметка успешно обновлена: {field} -> {new_value}")

        another_update = input("\nХотите обновить ещё одно поле? (да/нет): ").strip().lower()
        if not another_update or another_update == "нет": # если пустой ввод или нет
            print(another_update)
            break
        while another_update != "да" and another_update != "нет": # что-то, кроме да и нет
            print(f"Ошибка! Это не похоже на 'да' или 'нет'. ")
            another_update = input("\nХотите обновить ещё одно поле? (да/нет): ").strip().lower()

    return note


#if name == "__main__":
note = {
    "username": "Алексей",
    "title": "Список покупок",
    "content": "Купить продукты на неделю",
    "status": "новая",
    "created_date": "27-11-2024",
    "issue_date": "30-11-2024"
}

updated_note = update_note(note)
print("\nОбновлённая заметка:")
print(updated_note)
