#print("  Sizga kerak mahsulotlar ro'yxatini tuzing. \n")
#mahsulotlar = []
#ask = True
#n = 1
#while ask:
#	mahsulot = input(f"  {n} mahsulot nomini kiriting:  ")
#	mahsulotlar.append(mahsulot.capitalize())
#	print(f"  Mahsulotlar ro'yxati {mahsulotlar}")
#	quit = input('  Davom etish uchun "again" deb yozing yoki tugatish uchun "stop" \n  deb yozing:  ')
#	n += 1
#	if quit == "stop":
#		ask = False
#print(f"  {mahsulotlar}")

print("  Sizga kerak mahsulotlar ro'yxatini tuzing. \n")
mahsulotlar = []
ask = True
n = 1
while ask:
	mahsulot = input(f"  {n} mahsulot nomini kiriting:  ")
	mahsulotn = input(f"   {mahsulot.capitalize()} narxini kiriting:  ")
	mahsulotlar[mahsulot] = int(mahsulotn)
	quit = input('  Davom etish uchun "again" deb yozing yoki tugatish uchun "stop" \n  deb yozing:  ')
	n += 1
	if quit == "stop":
		ask = False
for mah, narx in mahsulotlar.items():
	print(f"  {mah.title()}ning narxi {narx} so'm')