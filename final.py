import datetime
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU')

# Ввод данных
note= []
username = input( 'Введите ваше имя ' )

title1 = input( 'Введите заголовок 1 ')
title2 = input( 'Введите заголовок 2 ')
title3 = input( 'Введите заголовок 3 ')
title = [title1, title2, title3]

content = input('Введите содержание заметки ')
status = 'Не завершено'
created_date = input('Дата начала работы (дд-мм-гггг) ')
issue_date = input('Дата окончания работы (дд.мм.гггг) ')

note = [username, content, status, created_date, issue_date, title] # список введенных данных

# Вывод на экран структуры данных
print('')
print('Имя пользователя: ', note[0] )
print('Содержание заметки: ', note[1] )
print('Статус: ', note[2])
created_date = datetime.datetime.strptime(note[3], '%d-%m-%Y')
print('Дата создания: ', created_date.strftime('%B,%d') )
issue_date = datetime.datetime.strptime(note[4], '%d-%m-%Y')
print('Дата завершения работы: ', issue_date.strftime('%B,%d') )
print('Заголовки: ', note[5])
