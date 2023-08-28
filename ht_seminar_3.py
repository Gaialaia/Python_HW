#task 10

import random
coins = int(input('How many coins '))

counter = 0
counter2 = 0
for el in range (coins):
    el = (random.randint(0,1))
    if el == 0:
        counter += 1
        print(el, counter)
    if el == 1:
        counter2 += 1
        print(el, counter2)

print(f'количество решек  {counter}, количество орлов {counter2}')
print(f'минимальное количество переворотов {min(counter, counter2)}')


#task 14

N = int(input('Enter N: '))
k = 1
while k < N:
    print(k, end=' ')
    k = k * 2

# task 12

s = int(input('Enter sum of numbers:  '))
p = int(input('Enter product of numbers:   '))

x = (s-int((s**2-4*p)**0.5))//2
y = s - x
if x <= 1000 and y <= 1000:
    print(f'Numbers on Petyas mind {x, y}')