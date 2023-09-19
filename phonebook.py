phone_book = []

def read_txt(filename):
    with open("phonebook.txt", "r") as file:
        for line in file:
            print(line, end="")
            
def write_txt(filename):
    with open(filename, 'w', encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s += v + ','
            phout.write(f'{s[:-1]}')






def show_menu():
    # print('\033c', end='') # Очистка экрана
    print('1. Распечатать справочник',
          '2. Найти телефон в справочнике',
          '3. Изменить запись',
          '4. Удалить запись',
          '5. Добавить абонента в справочник',
          '6. Закончить работу', "", sep='\n')
    choice = int(input('Enter digit:  '))
    return choice







def name ():
    lastname = input("enter name")
    with open("phonebook.csv", "r") as file:     
        contents = file.readlines()
    if lastname == contents[i]:
        print(str, end="")
  


# def find(phone_book):
    
#     lastname = input()
 
#     for phone_book in phone_book:
#         if phone_book['Фамилия'] == lastname:
#             print((
#                 phone_book['Фамилия'],
#                 phone_book['Телефон']
#             ))
#             break
#     else: 
#         print("Контакт не найден")


    
def work_with_phonebook():
    choice = show_menu()

    phone_book = read_txt('phonebook.csv')

    while (choice !=7 ):
        if choice == 1:
            print(phone_book)
            break
            
        elif choice==2:
            show_menu_search()
            break

# # #     #     elif choice == 3:
# # #     #         last_name = input('lastname')
# # #     #         new_number = input('new number')
# # #     #         print(change_number(phone_book,last_name,new_number))
# # #     #     elif choice == 4:
# # #     #         last_name = input('lastname')
# # #     #         print(delete_by_lastname(phone_book,last_name))
# # #     #     elif choice == 5:
# # #     #         last_name = input('lastname')
# # #     #         print(find_by_number(phone_book, number))
# # #     #     elif choice == 6:
# # #     #         user_data = input('new data')
# # #     #         add_user(phone_book, user_data)
# # #     #         write_txt('phonebook.txt', phone_book)

work_with_phonebook()

