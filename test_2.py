import re
def isCyrillic(text):
	return bool(re.search('[а-яА-Я]', text))


points_en = {1: 'aeioulnstr', 2: 'dg', 3:'bcmp', 4: 'fhvwy', 5: 'k', 8: 'jx', 10: 'qz'}

points_rus = {1: 'авеинорст', 2: 'дклмпу', 3: 'бгёья', 4: 'йы', 5: 'жзчцч', 8: 'шэю', 10: 'фщь'}
text = input()

if isCyrillic(text):
	print(sum([k for i in text for k, v in points_rus.items() if i in v]))
else:
	print(sum([k for i in text for k, v in points_en.items() if i in v]))