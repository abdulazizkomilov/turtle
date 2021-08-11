import math
cars = ["toyota", "mazda", "hyundia", "gm", "kia"]
for car in cars:
	if "gm" == car:
		print(car.upper())
	else:
		print(car.title())
print(' ')
login = input("Login parolingizni kiriting: ")
if "admin" == login:
	print("Xush kelibsiz admin foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
	print(f"Xush kelibsiz {login}")
print('  ')
a = input('1 - sonni kiriting:  ')
b = input('2 - sonni kiriting:  ')
if a == b:
	print('Sonlar bir-biriga teng!')
else:
	print('Sonlar teng emas!')
print(' ')
a = int(input('Manfiy yoki musbat son kiriting:  '))
if a < 0:
	print('Manfiy son ekan.')
if a > 0:
	print('Musbat son ekan.')
print('  ')
a = int(input('Ildiz olish kerak bulgan sonni kiriting:  '))
while True:
	if a < 0:
		print(int(input('Musbat son kiriting, manfiy son ildizi yuq:  ')))
		break
	if a > 0:
		print(math.sqrt(a))
		break