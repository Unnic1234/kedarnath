a=['1','2','3','4','5','6','7','8','9']

def printboard():
	print("|",a[0],"|",a[1],"|",a[2],"|")
	print("----------")
	print("|",a[3],"|",a[4],"|",a[5],"|")
	print("----------")
	print("|",a[6],"|",a[7],"|",a[8],"|")
	print("----------")
playeroneturn = True
while True:
	printboard()
	p=input("choose an available place:")
	
	if(p in a):
		if(a[int(p)-1])=='X' or a[int(p)-1]=='0':
			print("place taken,choose another place...")
			continue
		else:
			if playeroneturn:
				print("player 1 >>")
				a[int(P)-1]='X'
				playeroneturn = not playeroneturn
			else:
				print("player 2 >>")
				a[int(P)-1]='0'
				playeroneturn = not playeroneturn
			for i in (0,3,6):
				if(a[i]==a[i+1] and a[i]==a[i+2]):
					print("game win" , "and" , "game over");
					exit()
			for i in (3):
				if(a[i]==a[i+3] and a[i]==a[i+6]):
					print("game win" , "and" , "game over....");
					exit()

	else:
		continue