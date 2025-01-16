#Импорт необходимых модулей
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU')

# Вновь созданные функции:
# Определение и вывод текущей даты
def date_now():
    date_now = datetime.now().date()
    print('Текущая дата: ', date_now.strftime('%B,%d'))
    return date_now
# Разница между дедлайном и текущей датой
def difference(dead_date, date_now):
    dif = dead_date - date_now
    dif = dif.days
    return dif
# Обработка пользовательского ввода
def inp():
    if dif < 0:
        print(f'ВНИМАНИЕ! Дедлайн истек {abs(dif):02d} дней назад')
    elif dif == 0:
        print('ВНИМАНИЕ! Дедлайн сегодня!')
    else:
        print(f'До дедлайна осталось {dif:02d} дней')

# Вызов функции вывода текущей даты
date_now = date_now()

# Основной блок программы
while True:
    try:
        #Ввод даты и перевод из формата строки в формат даты
        dead_date_inp = input('\nВведите дату дедлайна в формате дд-мм-гггг: ')
        dead_date = datetime.strptime(dead_date_inp, '%d-%m-%Y').date()
        # Вызов функции расчета разницы между дедлайном и текущей датой
        dif = difference(dead_date, date_now)
        # Вызов функции обработки пользовательского ввода
        inp()
        break
    # Обработка ошибок ввода
    # Неправильный формат
    except ValueError:
        print('Ошибка! Убедитесь, что ввели дату в формате дд-мм-гггг ')
        print('Пожалуйста, попробуйте ввести дату еще раз')
    # Прочие ошибки
    except Exception as e:
        print('Произошла непредвиденная ошибка {str(e)}')
        print('Пожалуйста попробуйте ввести дату еще раз ')

