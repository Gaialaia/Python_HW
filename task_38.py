
def read_csv(filename): 
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(','))) 
            phone_book.append(record)	
    return phone_book

def write_csv(filename, phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s='' 
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')

        
def find_by_lastname(phone_book, last_name):
    filtered = list(filter(lambda x: x['Фамилия'] == last_name, phone_book))
    return list(map(lambda x : x['Телефон'], filtered))


def change_number(phone_book,last_name,new_number):
    for i in range(len(phone_book)):
        if last_name == phone_book[i]['Фамилия']:
            k, v = 'Телефон', new_number
            phone_book[i].update({k: v})
    return phone_book


def delete_by_lastname(phone_book,lastname):
    return list(filter(lambda x: x['Фамилия'] != lastname, phone_book))

def find_by_number(phone_book,number):
    if number == ['Телефон']:
        return list(map(lambda x : x['Фамилия'] + ['Телефон'] + x['Имя']))

        
def add_user(phone_book):
    
    newuser = {}

    enter_lastname = input('Фамилия: ')
    k, v = 'Фамилия', enter_lastname
    newuser.update({k: v})

    firstname = input('Имя: ')
    k, v = 'Имя', firstname
    newuser.update({k: v})

    phone = input('Телефон: ')
    k, v = 'Телефон', phone
    newuser.update({k: v})

    description =  input('Описание: ')
    k, v = 'Описание', description
    newuser.update({k: v})
    phone_book.append(newuser)
    return phone_book
     

def show_menu():
    print('1. Распечатать справочник',
          '2. Найти телефон по фамилии',
          '3. Изменить номер телефона',
          '4. Удалить запись',
          '5. Найти абонента по номеру телефона',
          '6. Добавить абонента в справочник',
          '7. Закончить работу', sep = '\n')
    
    choice = int(input('Введите номер команды: '))
    return choice

def work_with_phonebook():

    choice = show_menu()
    phone_book = read_csv('phonebook.csv')

    while (choice !=7):
        if choice == 1:
            print(phone_book)

        elif choice == 2:
            last_name = input('Введите фамилию: ')
            print(find_by_lastname(phone_book,last_name))

        elif choice == 3:
            last_name = input('Введите фамилию: ')
            new_number = input('Введите номер:  ')
            phone_book = change_number(phone_book,last_name,new_number)

            print(phone_book)
            write_csv('phonebook.csv',phone_book)

        elif choice == 4:
            lastname = input('Введите фамилию:  ')
            phone_book = delete_by_lastname(phone_book,lastname)
            print(phone_book)
            write_csv('phonebook.csv',phone_book)

        elif choice == 5:
            number = input('Введите номер: ')
            print(find_by_number(phone_book, number))

        elif choice == 6:
            phone_book = add_user(phone_book)
            print(phone_book)
            write_csv('phonebook.csv',phone_book)
        

        choice = show_menu()

work_with_phonebook()
