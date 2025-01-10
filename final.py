# Ввод данных
username = input( 'Введите ваше имя ' )

title1 = input( 'Введите заголовок 1 ')
title2 = input( 'Введите заголовок 2 ')
title3 = input( 'Введите заголовок 3 ')
title = [title1, title2, title3]

content = input( 'Введите текст заметки ' )
status = 'Не завершено'
created_date = input( 'Дата начала работы (дд-мм-гггг) ' )
issue_date = input('Дата окончания работы (дд.мм.гггг) ')

note = [username, title, content, status, created_date, issue_date]

print(note)