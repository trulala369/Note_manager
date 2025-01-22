# Определяем список словарей с заметками
note_dict = [{'username': 'Алексей', 'title': 'Список покупок', 'Content': 'Купить продукты'},
             {'username': 'Мария', 'title': 'Учеба', 'Content': 'Подготовиться к экзамену'},
             {'username': 'Мария', 'title': 'Кастинг', 'Content': 'Выучить текст'}]
list_ = ['Имя:', 'Заголовок:', 'Содержание:']
#print(note_dict)
yes_no=''

# проверка на ошибку ввода заголовка (нет в списке на удаление)
def title_err(a, b):
    for i in b:
        if a == i.get('title'):
            return True

# основной блок удаления заметок списком и по одной
while True:
    yes_no  = input('\nХотите удалить заметку? (да/нет) ').lower()
    if not yes_no or yes_no == 'нет':  # если ввод пустой или 'нет', выход
        break # отказ от предложения удалить заметку - это выход
    else:
        while yes_no != 'да':  # если введено еще что-то кроме 'да'
            print('Это не похоже на "да" или "нет", попробуйте еще раз')
            yes_no = input('\nХотите удалить заметку? (да/нет) ').lower()

        # Если предложение удалить заметку принято, вводим имя
        # Ошибка в имени не обрабатывается, будет сообщение Список пуст
        username = input('Введите ваше имя: ').strip().capitalize()

        while not username:  # обработка пустого ввода
            print('Имя пользователя не может быть пустым')
            username = input('\nВведите ваше имя: ').strip().capitalize()

        #Определяем два списка для имени: все удаленные и оставшиеся
        note_del = []
        note_rest = []
        for i in note_dict:
            # сначала в список для удаления добавляем все заметки пользователя
            if username == i.get('username'):
                note_del.append(i)
            # Оставшиеся в другой список
            else:
                note_rest.append(i)

        #Если список пуст, это значит заметок нет или ошибка в имени
        if not note_del:
            print(username + ', сори, у вас нет заметок.')
            break

        # Если в списке есть заметки, выводим их на экран
        print('==== Все ваши заметки: ====')
        for i in note_del:
            n = 0
            #print('\n')
            for j, k in i.items():
                print(f'{list_[n]} {k} ')
                n = n + 1
        # Предложение удалить все заметки
        yes_no = input('\n'+username + ', хотите удалить все заметки?(да/нет) ').lower()
        while yes_no != 'да' and yes_no != 'нет':  # если введено еще что-то кроме 'да'
            print('Это не похоже на "да" или "нет", попробуйте еще раз\n')
            yes_no = input('Хотите удалить все заметки? (да/нет) ').lower()

        # Если предложение принято, предупреждение
        if yes_no == 'да':
            yes_no = input('Уверены, что хотите удалить все заметки? (да/нет) ').lower()
            while yes_no != 'да' and yes_no != 'нет':  # если введено еще что-то кроме 'да'
                print('Это не похоже на "да" или "нет", попробуйте еще раз\n')
                yes_no = input('Уверены, что хотите удалить все заметки? (да/нет) ').lower()
        # Если все же нужно удалить весь список
        if yes_no == 'да':
            note_del.clear() #Очищаем список удаленных заметок
            note_dict = note_rest # Обновляем список заметок
            print('Список очищен')
            break
        else:
            # Если не нужно удалять весь список, предложение ввести заголовок для удаления
            title = input('Тогда введите заголовок заметки: ' ).strip().capitalize()
            # обработка пустого ввода и ошибки в заголовке
            while not title or not title_err(title, note_del) :
                print('Ошибка ввода')
                title = input('Введите заголовок заметки: ').strip().capitalize()

            # Если заголовок введен верно, предупреждение
            yes_no = input('Уверены, что хотите удалить заметку? (да/нет) ').lower()
            while yes_no != 'да' and yes_no != 'нет':  # если введено еще что-то кроме 'да'
                print('Это не похоже на "да" или "нет", попробуйте еще раз')
                yes_no = input('Уверены, что хотите удалить заметку? (да/нет) ').lower()
            # Если пользователь передумал удалять заметку, выход
            if yes_no == 'нет':
                break
            # Если все же нужно удалить заметку, ищем ее по заголовку
            for i in note_del:
                if title == i.get('title'):
                    # удаление из списка заметок
                    note_dict.remove(i)
                    # удаление из списка данного пользователя для вывода оставшихся на экран
                    note_del.remove(i)
                    print('\nЗаметка удалена, а вот то, что осталось')
                    for i in note_del:
                        n = 0
                        for j, k in i.items():
                            print(f'{list_[n]} {k} ')
                            n = n + 1
                        # снова на ввод


