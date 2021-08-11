a = input("   Istalgan so'z yoki gap kiriting: ")
d = a[::-1]
print(f"   {d.capitalize()}")

a = int(input("   Parolni kiriting: "))
b = 12345
ad = True
while ad:
	if a == b:
		print("   Xush kelibsiz")
		ad = False
	else:
		print("   Parol xato")
		ad = True