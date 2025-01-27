#Функция для отображения меню

from colorama import init, Fore, Style

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
        print(f"{Fore.GREEN}\nМеню действий:")
        print(f"{Fore.BLUE}1. Создать новую заметку")
        print(f"{Fore.YELLOW}2. Показать все заметки")
        print(f"{Fore.RED}3. Обновить заметку")
        print(f"{Fore.CYAN}4. Удалить заметку")
        print(f"{Style.BRIGHT}{Fore.MAGENTA}5. Найти заметки")
        print("6. Выйти из программы")

        try:
            choice = input("Ваш выбор: ")
            if choice == "1":
                notes.extend(create_note())
            elif choice == "2":
                page_number = 0
                end_index = 0
                display_notes(notes, page_number)
            elif choice == "3":
                if notes:
                    page_number = 0
                    end_index = 0
                    display_notes(notes, page_number)
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
                input_crit = ''
                input_crit_(notes, input_crit)
            elif choice == "6":
                print("Программа завершена. Спасибо за использование!")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
        except ValueError:
            print("Ошибка: введите число от 1 до 6.")
        print(notes)
        input()
# Запуск меню
if __name__ == "__main__":

    notes = [
        {'username': 'Иван', 'title': 'Расходы', 'content': 'Купить продукты на неделю', 'status': 'новая',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Мария', 'title': 'Кастинг', 'content': 'Выучить текст', 'status': 'выполнено',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Иван', 'title': 'Выходные', 'content': 'Отключить тлфн', 'status': 'новая',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Алексей', 'title': 'Поездка в горы', 'content': 'Позвонить Олегу', 'status': 'новая',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Мария', 'title': 'Свадьба','content': 'Купить туфли', 'status': 'новая',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Елена', 'title': 'Учеба', 'content': 'Выполнить задание 5', 'status': 'новая',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Петр', 'title': 'Свидание', 'content': 'Купить цветы', 'status': 'новая',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Иван', 'title': 'Поход', 'content': 'Купить палатку', 'status': 'новая',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'}
    ]
    display_menu(notes)
