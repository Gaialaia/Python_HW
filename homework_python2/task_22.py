#task 22

setonelength = int(input('enter setone length   '))
setone = {input(i ) for i in range(setonelength)}
settwolength = int(input('enter settwo length   '))
settwo = {input(i ) for i in range(settwolength)}
setthree = sorted(setone.intersection(settwo))
print(f'identical elements in the sets are :', *setthree)

