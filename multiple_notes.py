#Импорт необходимых модулей
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU')

#Функция обработки ошибки при вводе даты
def err_date(date_str):
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False
# Функция ввода заметок
#def new_note():
date_now = datetime.now().date() # Текущая дата
print('\nСегодня ', date_now.strftime('%B,%d'))
print('Добро пожаловать в "менеджер заметок"!')
while True:
    note_dict = [] # Список словарей для хранения заметок
    note = {}  # словарь из списка для сравнения введенных имени и названия
    n = 0 # переменная для вывода номера заметки
    new = ''   # Ввод или выход (Да/Нет)

    # Основной блок ввода заметок и проверки ввода
    while True:
        new = input('\nХотите ввести новую заметку? (да/нет) ').lower()
        if not new or new == 'нет': # если ввод пустой или 'нет', выход
            break
        else:
            while new != 'да': # если введено еще что-то кроме 'да'
                print('Это не похоже на "да" или "нет", попробуйте еще раз')
                new = input('\nХотите ввести новую заметку? (да/нет) ').lower()
            #print(new)
            username = input('\nВведите ваше имя: ').strip()
            while not username: # обработка пустого ввода
                print('Имя пользователя не может быть пустым')
                username = input('\nВведите ваше имя: ').strip()

            title = input('Введите название заметки: ').strip()
            while not title:  # обработка пустого ввода
                print('Название заметки не может быть пустым')
                title = input('\nВведите название заметки: ').strip()

            # Перебираем список словарей
            for i in range(len(note_dict)):
                note = note_dict[i-1]  # загружаем словарь в список note
                # Если введенное имя и заголовок заметки уже есть словаре, предупреждение
                if username == note.get('username') and title == note.get('title'):
                    print('ВНИМАНИЕ! Такое название уже существует')
                    title = input('\nВведите название заметки: ').strip()

            # Продолжаем ввод
            content = input('Введите текст заметки: ').strip()
            while not content: # обработка пустого ввода
                print('Содержание заметки не может быть пустым')
                content = input('\nВведите текст заметки: ').strip()
            # продолжаем ввод
            status_ = ['новая', 'в процессе', 'выполнено'] # определяем список со статусами
            status = input(f'Введите статус заметки ({','.join(status_)}): ').strip().lower()
            while status not in status_: # обработка ошибки ввода
                print(f'Ошибка! Возможные варианты: {', '.join(status_)}')
                status = input(f'\nВведите статус заметки ({','.join(status_)}): ').strip().lower()

            # Дата создания заметки -текущая дата
            created_date = date_now.strftime('%d-%m-%Y')
            print('Дата начала работы: сегодня ' +str(created_date) ) # вывод текущей даты
            # Продолжаем ввод
            issue_date = input( 'Введите дату дедлайна (дд-мм-гггг): ').strip()
            while not err_date(issue_date): # обработка ошибки ввода при помощи функции
                print('Ошибка при вводе даты! Используйте формат (дд-мм-гггг)')
                issue_date = input('Введите дату дедлайна (дд-мм-гггг): ').strip()

            # добавление заметки в словарь
            note_dict.append({
                "username": username,
                "title": title,
                "content": content,
                "status": status,
                "created_date": created_date,
                "issue_date": issue_date
            })
            # вывод новой заметки
            print(f'\n {n} Имя: {username} \n Заголовок: {title} \n Описание: {content}')
            print(f' Статус: {status}\n Дата создания: {created_date}\n Дедлайн: {issue_date}')
            #return note_dict

            print('Ввод закончен! ')

#if __name__=="__main__":
     #note = new_note()
     #print('\nЗаметка создана')
       
