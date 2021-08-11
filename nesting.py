dustlar = {
'ali' : ['python', 'c++'],
'vali' : ['php', 'c++'],
'sali' : ['c', 'python']
}

for ism, tillar in dustlar.items():
	print(f"{ism.title()} tillarni biladi")
	for til in tillar:
		print(f"{til.upper()}")