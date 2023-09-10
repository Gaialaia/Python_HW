
# task 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод: Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам Парам пам-пам

a = input("enter phrase 1  ")
b = input("enter phrase 2  ")
c = input("enter phrase 3  ")
def count_vowels(phrase):
  return sum([1 for x in phrase if x in 'а, е, ё, и, о, у, ы, э, ю, я'])


print(count_vowels(a))
print(count_vowels(b))
print(count_vowels(c))


if count_vowels(a) == count_vowels(b) == count_vowels(c):
  print("Парам пам-пам")
else:
  print("Пам парам")
