# Проверка и обновление словаря статусов

status_ = {'1': 'ВЫПОЛНЕНО', '2': 'В ПРОЦЕССЕ', '3': 'ОТЛОЖЕНО'}
# Инвертирование словаря для поиска ключа по значению (когда вводят текст, а не число)
inv_status_= {v: k for k, v in status_.items()}
# словарь для текущего статуса заметки и для обновления
status1 = {'2':'В ПРОЦЕССЕ'}
for k , v in status1.items():
    # вывод на экран текущего статуса
    print('\nТекущий статус заметки: ' +v )

# Вывод на экран справочной информации
print('\nДля изменения статуса введите цифру или текст, как показано ниже ')

# Цикл для вывода всех статусов из словаря на экран
n = 1
while str(n) in status_.keys():
    print( str(n)+ " или "+ status_.get(str(n)))
    n = n+1
# Ввод нового статуса
# и обработка ошибочного ввода
status2 = '' # переменная для ввода статуса
while status2 == '':
    status2 = input('\nВведите новый статус заметки ' ).upper()
    status1 = {}
    # Проверка корректности ввода
    if status2 in status_.keys(): # если ввели цифру
            print('Новый статус заметки: '+ status_.get(status2) )
            status1.update({status2: status_.get(status2)})
            #status2[status1] = status_.get(status1) # добавление нового статуса в словарь
    elif status2 in status_.values(): # если ввели текст
            print('Новый статус заметки: '+ status2 )
            status1.update({inv_status_.get(status2):status2})
            #status2[inv_status_.get(status1)] = status1 # добавление нового статуса в словарь
    else:
            print('Ошибка ввода')
            status2 = '' # условие для повторного ввода

# вывод на экран словаря с новым статусом
#print(status1)
