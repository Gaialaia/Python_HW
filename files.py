with open("phonebook.csv", "r") as f:   # построчное считывание
    for line in f.readlines():
        print(line)

with open("phonebook.csv", "r") as file:
    contents = file.readlines()
    str1 = contents[0]
    str2 = contents[1]
    str3 = contents[3]
    print(str1)
    print(type(str1))

with open("phonebook.csv", "r") as f:   # построчное считывание
    for line in f.readlines():
       line.split(",")
       print(type(line))