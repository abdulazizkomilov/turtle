names = ["Nodir", "Miraziz", "Doston", "Abdulazez", "Islom"]
for name in names:
	print("Salom", name)
print(f"Kod {len(names)} martta takrorlandi")
print('  ')
toq_son = list(range(11, 100, 2))
for kvadrat in toq_son:
	print(f"{kvadrat**3}")
print('  ')
kino = []
print("Iltimos 5 ta yaxshi ko'rgan kinongizni kiriting.")
for surash in range(5):
	kino.append(input(f"{surash + 1}-kinoni kiriting: "))
print("Kinolar ro'yxati", kino)
print("  ")
a = int(input("Bugun nechta kishi bilan suhbat qildingiz?  :_"))
conversation = []
for suxbat in range(a):
	conversation.append(str(input(f"{suxbat + 1} - suhbat qilgan kishingiz kim edi: ")))
print(conversation)