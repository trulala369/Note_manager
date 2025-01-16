import datetime
import locale
# Это я срисовала из инета чтобы было по-русски
locale.setlocale(locale.LC_ALL, 'ru_RU')

created_date= datetime.datetime.strptime('05-01-2025', '%d-%m-%Y')
print('Дата создания заметки:', created_date.strftime('%B,%d'))