import datetime
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU') # это я срисовала из инета чтобы было по-русски

created_date= datetime.datetime.strptime('05-01-2025', '%d-%m-%Y')
print('Дата создания заметки:', created_date.strftime('%B'), ',', created_date.strftime('%d'))