import random
while True:
	a=(input("press r to roll"))
	if(a=='r'):
		r=random.randint(1,6)
		print(r)
	else:
		break