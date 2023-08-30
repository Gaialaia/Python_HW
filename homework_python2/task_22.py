#task 22

#
# s = set()
#
# s.add(input())
#
# print(s)
# print(type(s))
#
# # for i in s:
# #     s.add(input())
# #     len(s)


s = {2,3,6,6,9}
z = {1,1,7,6,9}
print(type(z))

r = int(input('enter length  '))
f = {input (i) for i in range(r)} # генератор множеств
print(f)
print(s.symmetric_difference(z))
print(s.difference(z))
print(s.symmetric_difference(z))
print(f"set ", s.intersection(z))  #111



s1 = list(s)


z1 = list(z)

s1z1 = s1 + z1
s2z2 = s1z1[:]

print(s1z1)

duplicates = []

for item in s2z2:
    if s2z2.count(item) > 1 and item not in duplicates:
        duplicates.append(item)
        print(sorted(duplicates))

my_list = [1, 2, 3, 2, 4, 1, 5, 2]
duplicates = []

for item in my_list:
    if my_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

print("Повторяющиеся элементы в списке:", duplicates)
