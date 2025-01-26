#Функция для отображения меню

#from colorama import init, Fore, Style

from create_note_function import create_note
from update_note_function import update_note
from display_notes_function import display_notes
from search_notes_function import search_notes

# Инициализация библиотеки
init(autoreset=True)

def delete_note(notes):
    # Реализовать тело функции
    return notes

def display_menu(notes):
    while True:
        print(notes)
        input()
        # Отобразить меню
        print(f"\nМеню действий:") #{Fore.GREEN}
        print(f"1. Создать новую заметку") #{Fore.BLUE}
        print(f"2. Показать все заметки") #{Fore.YELLOW}
        print(f"3. Обновить заметку") # {Fore.RED}
        print(f"4. Удалить заметку") #{Fore.CYAN}
        print(f"5. Найти заметки") # {Style.BRIGHT}{Fore.MAGENTA}
        print("6. Выйти из программы")

        try:
            choice = input("Ваш выбор: ")
            if choice == "1":
                note = create_note()
                notes.append(note)
            elif choice == "2":
                display_notes(notes)
            elif choice == "3":
                if notes:
                    display_notes(notes)
                    index = int(input("Введите номер заметки для обновления: ")) - 1
                    if 0 <= index < len(notes):
                        notes[index] = update_note(notes[index])
                    else:
                        print("Неверный номер заметки.")
                else:
                    print("Список заметок пуст.")
            elif choice == "4":
                # Реализуйте функцию удаления заметки
                notes = delete_note(notes)
            elif choice == "5":
                keyword = input("Введите ключевое слово для поиска: ")
                status = input("Введите статус для поиска (или оставьте пустым): ")
                found_notes = search_notes(notes, keyword, status)
                display_notes(found_notes)
            elif choice == "6":
                print("Программа завершена. Спасибо за использование!")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
        except ValueError:
            print("Ошибка: введите число от 1 до 6.")

# Запуск меню
if __name__ == "__main__":
    notes = [
        {"title": "Заголовок 1", "username": "Имя 1"},
        {"title": "Заголовок 2", "username": "Имя 2"},
    ]
    print(notes)
    input()
    display_menu(notes)