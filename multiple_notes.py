#Импорт необходимых модулей
from datetime import datetime
import locale
from sys import excepthook

locale.setlocale(locale.LC_ALL, 'ru_RU')

#Функция обработки ошибки при вводе даты
def err_date(date_str):
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False

date_now = datetime.now().date() # Текущая дата
print('\nСегодня ', date_now.strftime('%B,%d'))
print('Добро пожаловать в "менеджер заметок"!')

note_dict = {} # словарь для хранения заметок
n = 0 # номер заметки
new = ''
# Основной блок ввода заметок и проверки ввода
while True:
    new = input('\nХотите ввести новую заметку? (да/нет) ').lower()
    if not new or new == 'нет': # если ввод пустой или 'нет', выход
        break
    else:
        while new != 'да': # если введено еще что-то кроме 'да'
            print('Это не похоже на "да" или "нет", попробуйте еще раз')
            new = input('\nХотите ввести новую заметку? (да/нет) ').lower()

        username = input('Введите ваше имя: ').strip()
        while not username: # обработка пустого ввода
            print('Имя пользователя не может быть пустым')
            username = input('Введите ваше имя: ').strip()

        n = n + 1
        title = input('Введите название заметки: ').strip()
        while not title:  # обработка пустого ввода
            print('Название заметки не может быть пустым')
            title = input('Введите название заметки: ').strip()

        list_ = note_dict.get(title, [])  # возвращаем список с заметкой или пустой список

        while note_dict and title in list_: # если в списке уже есть заголовок
            print('ВНИМАНИЕ! Такой заголовок уже существует')
            title = input('Введите название заметки: ').strip()

        content = input('Введите текст заметки: ').strip()
        while not content: # обработка пустого ввода
            print('Содержание заметки не может быть пустым')
            content = input('Введите текст заметки: ').strip()

        status_ = ['новая', 'в процессе', 'выполнено'] # список со статусами
        status = input(f'Введите статус заметки ({','.join(status_)}): ').strip().lower()
        while status not in status_: # обработка ошибки ввода
            print(f'Ошибка! Возможные варианты: {', '.join(status_)}')
            status = input(f'Введите статус заметки ({','.join(status_)}): ').strip().lower()

        created_date = date_now.strftime('%d-%m-%Y')
        print('Дата начала работы: сегодня ' +str(created_date) ) # вывод текущей даты

        issue_date_ = input( 'Введите дату дедлайна (дд-мм-гггг): ').strip()
        while not err_date(issue_date_): # обработка ошибки ввода при помощи функции
            print('Ошибка при вводе даты! Используйте формат (дд-мм-гггг)')
            issue_date_ = input('Введите дату дедлайна (дд-мм-гггг): ').strip()

        # перевод строки в формат даты
        issue_date = datetime.strptime(issue_date_,'%d-%m-%Y').date()

        # добавление заметки в словарь
        note_dict.update({title: [username, title, content, status, created_date, issue_date]})

        # вывод новой заметки
        print(f'\n {n} Имя: {username} \n Заголовок: {title} \n Описание: {content}')
        print(f' Статус:{status}\n Дата создания {created_date}\n Дедлайн: {issue_date}')

