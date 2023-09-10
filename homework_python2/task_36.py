# task 36
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 



def print_operation_table (table, m=7, n=7):
    c = [[table(i,j) for j in range(1, m+1)] for i in range(1, n+1)]
    for i in c:
        print(*[])
        print(*[x for x in i])

print_operation_table(lambda i,j: i*j)