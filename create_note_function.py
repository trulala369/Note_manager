# Функция создания заметки

#Импорт необходимых модулей
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU')

date_now = datetime.now().strftime('%d-%m-%Y')  # Текущая дата
print('Сегодня ', date_now ) #.strftime('%B,%d'))
print('Добро пожаловать в "менеджер заметок"!')

# Функция ввода заметок и проверки ввода
def create_note():
    # функция обработки ошибки ввода даты
    def err_date(date_str):
        try:
            datetime.strptime(date_str, "%d-%m-%Y")
            return True
        except ValueError:
            return False

    while True:
        n = 0
        global date_now
        new = input('\nХотите ввести новую заметку? (да/нет) ').lower()
        if not new or new == 'нет':  # если ввод пустой или 'нет', выход
            break
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
            created_date = date_now   #.strftime('%d-%m-%Y')
            print('Дата начала работы: сегодня ' + created_date)  # вывод текущей даты
            # Продолжаем ввод
            issue_date = input('Введите дату дедлайна (дд-мм-гггг): ').strip()
            while not err_date(issue_date):  # обработка ошибки ввода при помощи функции
                print('Ошибка при вводе даты! Используйте формат (дд-мм-гггг)')
                issue_date = input('Введите дату дедлайна (дд-мм-гггг): ').strip()
            # вывод новой заметки
            n = n + 1
            print(f'\n Ваша новая заметка:\n Имя: {username} \n Заголовок: {title} \n Описание: {content}')
            print(f' Статус: {status}\n Дата создания: {created_date}\n Дедлайн: {issue_date}')

            # формирование словаря из добавленной заметки
            dict_note = {}
            dict_note.update({
                "username": username,
                "title": title,
                "content": content,
                "status": status,
                "created_date": created_date,
                "issue_date": issue_date
            })
            return dict_note

dict_=create_note()
print('\nСловарь с заметкой:')
print( dict_)

