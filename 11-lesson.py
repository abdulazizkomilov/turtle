a = int(input('Juft son kiriting:  '))
m = a % 2
if m == 0:
	print('Raxmat!')
else:
	print('Bu son juft emas!')
print(' ')
bilet = int(input('Yoshingiz nachada? __ '))
if bilet < 4 or bilet > 60:
	print('Kirish bepul')
if bilet > 4 and bilet < 18:
	print("Kirish 1000 so'm")
if bilet > 18 and bilet < 60:
	print("Kirish 2000 so'm")
print(' ')
