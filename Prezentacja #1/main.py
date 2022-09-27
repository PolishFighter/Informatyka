def decToP(n, p):
	ans = []
	while n > 0:
		ans = [n%p] + ans
		n = n//p
	return ans
def pToDec(n, p):
	ans = 0
	
	for i in range(len(n)):
		ans = (ans * p) + n[i]
	return ans

def printList(l):
	for i in range(len(l)):
		if l[i] > 9:
			print(chr(l[i]+55), end="")
		else:
			print(l[i], end="")
	print()
		
def getList():
	n = input()
	l = []
	for i in range(len(n)):
		if ord(n[i]) > 57:
			l.append(ord(n[i])-55)
		else:
			l.append(int(n[i]))
	return l
	
p1 = int(input())
p2 = int(input())
n = getList()


nInDec = pToDec(n, p1)
nInP2 = decToP(nInDec, p2)

printList(nInP2)

