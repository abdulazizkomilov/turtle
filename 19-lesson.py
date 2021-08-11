#from datetime import datetime

#bugun = datetime.today()

#def tuliq_malumot():
#	""" Ism va tug'ilgan yilni surab aniqlab beradi """
#	ism = input("Ismingiz nima:  ")
#	yosh = input("Nechanchi yil tug'ulgansiz:  ")
#	print(f"Salom {ism.title()}, sizning yoshingiz {bugun.year - int(yosh)} yoshda.")
#	
#tuliq_malumot()

#def kvadrat_son():
#	""" Sonning kvadratini hisoblaydi """
#	son = input("Istalgan son kiriting:  ")
#	print(f"{int(son)}ning kvadrati {int(son)**2}ga teng.")
#	
#kvadrat_son()

#def juft_toq():
#	""" Sonni toq yoki juft ekanligini aniqlaydi."""
#	son = int(input("Istalgan son kiriting:  "))
#	if son %2 == 0:
#		print(f"{son} juft son.")
#	else:
#		print(f"{son} toq son.")
#juft_toq()

#def katta_kichik_teng():
#	""" Solarni katta yoki kichik yoki tengligini hisoblaydi """
#	son1 = int(input("Istalgan son kiriting:  "))
#	son2 = int(input("Istalgan son kiriting:  "))
#	if son1 < son2:
#		print(f"{son1}dan {son2} katta.")
#	elif son1 > son2:
#		print(f"{son1}dan {son2} kichik.")
#	else:
#		print(f"{son1}   {son2}ga teng.")
#katta_kichik_teng()

#def solishtir(x,y):
#    """Ikki sonni solishtiruvchi funksiya"""
#    if x>y:
#        print(f"{x}>{y}")
#    elif x<y:
#        print(f"{y}>{x}")
#    else:
#        print(f"{x}={y}")

#solishtir(10,20)
#solishtir(-9,12)
#solishtir(1223*5,5**4)

#def baho_kam():
#	son = int(input("Baholanish alomati: "))
#	shart = 0
#	while shart <= 10:
#		if shart == 1:
#			continue
#		elif int(son %shart) == 0:
#			print(f"{son} soni {shart} ga qoldiqsiz bo'linadi.")
#		else:
#			print(" ")
#		shart += 1

#baho_kam()

def bolinish_alomatlari():
	son = int(input("Bo'lish uchun qiymat kiriting: "))
	for a in range(2, 11):
		if not son%a:
			print(f"{son} soni {a} ga qoldiqsiz bo'linadi.")
			
bolinish_alomatlari()