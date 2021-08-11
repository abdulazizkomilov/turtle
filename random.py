from random import randint
sonlar = [7, 2, 15, 35]
son = randint(1,37)
i = 0
while son in sonlar:
	i += 1
	son = randint(1, 37)
print(son)
	