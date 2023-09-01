#task_24

bushesqty = int(input('enter bush quantity  '))
berries = [int(input(i)) for i in range(bushesqty)]

i = len(berries)
if bushesqty > 3:
    j = len(berries) - 4
    bush = (berries[i:j:-1])
    print(f'максимальное количество ягод за один проход: ', sum(bush))

elif bushesqty == 3:
        i = len(berries) - len(berries)
        j = len(berries)
bush = (berries[i:j])
print(f'максимальное количество ягод c трёх кустов :  ', sum(bush))