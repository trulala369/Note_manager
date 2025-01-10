# Ввод данных
username = input('Введите ваше имя ')
# Ввод заголовков в список
title1= input('Введите Заголовок1 ' )
title2= input('Введите Заголовок2 ' )
title3= input('Введите Заголовок3 ' )
title = [title1, title2, title3 ]

content = input( 'Введите текст заметки ' )
status = 'Не завершено'
created_date = input( 'Дата начала работы (дд-мм-гггг) ' )
issue_date = input('Дата окончания работы (дд.мм.гггг) ')

# Вывод на экран
print( username, ',', title, ',', content, ',', status, ',', created_date, ',', issue_date )
