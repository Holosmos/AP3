def tern(cond, a,b):
	if cond is True:
		return a
	return b	

#Exercice 1
import time
import cmath
import math
def fib1(n):
	if n <2:
		return n
	return fib1(n-1)+fib1(n-2)

# print time.clock()
# print fib1(18)
# print time.clock()
# print fib1(30)
# print time.clock()
		
		
def fib2(n,liste = [0,1]):
	a = len(liste)
	if n < 0:
		return -1
	if n == a-1 or n == a-2:
		return liste[n]
	liste.append(liste[a-1]+liste[a-2])
	return fib2(n,liste)
	
# print time.clock()
# print fib2(18)
# print time.clock()
# print fib2(30)
# print time.clock()

def fib3(n):
	if n<2:
		return n
	fk = fib3(n/2)
	if n%2==0:
		return (2*fib3(n/2-1)+fk)*fk
	return fib3(n/2+1)**2+fk**2	

def fib3Aux(n):
	if n<=1:
		return (0,1)
	
	a = fib3Aux(n/2)
	if n%2==0:	
		return (a[0]**2+a[1]**2,(2*a[0]+a[1])*a[1])
	b = a[0]+a[1]
	return ((2*a[0]+a[1])*a[1],b**2+a[1]**2)
	
#print fib3Aux(6)
	
# print time.clock()
# print fib2(999)
# print time.clock()
# print fib3Aux(999)[1]
# print time.clock()	

def fib4(n):
	phi1 = (1+cmath.sqrt(5))/2.
	phi2 = (1-cmath.sqrt(5))/2.
	
	a = 1./cmath.sqrt(5)
	b = -1./cmath.sqrt(5)
	
	return a*(phi1**n) + b*(phi2**n)	
	
	
# Exercice 2

def fact(n):
	if n<=1:
		return 1
	return fact(n-1)*n
		
#print fact(3)

def binom1(p,n):
	nf = fact(n)
	pf = fact(p)
	df = fact(n-p)
	return nf/(pf*df)
	
# print time.clock()
# print binom1(1,2)
# print time.clock()	

def binom2(p,n):
	if p>n or n<0:
		return 0
	elif p==1 or p==n-1:
		return n
	elif p==0 or p==n:
		return 1
	
	if p>n/2:
		p = n-p
	return binom2(p-1,n-1)+binom2(p,n-1)	
		
# print time.clock()
# print binom1(10,20)
# print time.clock()
# print binom2(10,20)
# print time.clock()	

def afficher_triangle(n):
	
	nf = 1
	pf = 1
	df = 1
	for i in range(1,n+1):
		strin = "1 \t "
		nf *= i
		pf = 1
		df = nf
		for j in range(1,n+1):
			pf*= j
			df = fact(i-j)
			a = nf/(df*pf)
			if a >0:
				strin += str(nf/(df*pf)) + " \t "
		strin += "\n"
		print strin	

#afficher_triangle(1000)

#Exercice 3

def bin(a):
	strin = ""
	boo = False
	if a==0:
		print "0"
	elif a<0:
		a*=-1
		boo = True	
	while a!=0:
		strin = str(a%2) + strin
		a/=2
	if boo:
		strin = "-" + strin
	print strin

#bin(-30)

def hexa(a):
	strin = ""
	boo = False
	he = ['A','B','C','D','E','F']
	if a==0:
		print "0"
	elif a<0:
		a*=-1
		boo = True	
	while a!=0:
		r = a%16
		if r < 9:
			strin = str(r) + strin
		else:
			strin = he[r-10] + strin
				
		a/=16
	if boo:
		strin = "-" + strin
	print strin	


#hexa(42)


# Exercice 4

def pgcd(a,b):
	if a==b:
		return (a,1,0)
	if a<b:
		a,b=b,a	
	
	r1,u1,v1,r2,u2,v2 = a,1,0,b,0,1
	while r2!=0:
		q = r1/r2
		r1,u1,v1,r2,u2,v2 = r2,u2,v2,r1-q*r2,u1-q*u2,v1-q*v2
	return (r1,u1,v1)

#print pgcd(15,7)		

#Exercice 5

def sol(a,n):
	prod = 1
	for k in n:
		prod*= k
	e = [pgcd(prod/k,k)[1]*prod/k for k in n]
	x = 0
	for i in range(len(a)):
		x += a[i]*e[i]
	return x

#print sol((2,4,3),(3,5,7))

def ask(strin):
	a=0;
	while True:
		try:
			a = int(raw_input(strin))
			break
		except ValueError :
			print 'Entrez un entier'	
	return a

def askPositif(strin):
	a=0;
	while True:
		try:
			a = int(raw_input(strin))
			assert a>0
			break
		except ValueError :
			print 'Entrez un entier strictement positif'
		except AssertionError :
			print 'Entrez un entier strictement positif'
	return a		

def askEq(liste):
	strin = "Entrez une equation sous la forme  'x = a mod n'\n"
	while True:
		try:
			recep = raw_input(strin)
			ega = recep.partition("=")
			assert ega[2] != ''
			modo = ega[2].partition("mod")
			assert modo[2] != ''
			a = int(modo[0])
			n = int(modo[2])
			for k in liste:
				assert pgcd(n,k[1])[0]==1
			liste.append([a,n])	
			break
		except ValueError :	
 			print "Entrez une chaine valide, comme le modele"
		except AssertionError :
			print "Entrez une chaine valide, comme le modele et verifez que n est premier avec la liste : " + str([i[1] for i in liste])
		
# nbEq = askPositif("Entrez le nombre d'equations : ")
# liste_eq=[]
# for i in range(nbEq):
# 	askEq(liste_eq);
# 
# a = sol([i[0] for i in liste_eq],[i[1] for i in liste_eq])
# print str(a) + " est solution du systeme d'equations."


# Exercice 4

def fonc1(i,n):
	list = [n]
	for k in range(i-1):
		if n == 1:
			list.append(1)
		elif n%2 == 0:
			list.append(n/2)
			n = n/2
		else :
			list.append(3*n+1)
			n = 3*n+1
	return list

# print fonc1(20,7)				

# Exercice 5

def prim(n):
	list = [i for i in range(2,int(math.sqrt(n))+1)]
	for k in list:
		for i in range(2,(int(math.sqrt(n))+1)/k+1):
			try:
				list.remove(i*k)
			except ValueError:
				False	
	for k in list:
		if n%k == 0:
			return k
	return 0				

# for i in range(2,50):
# 	n = prim(i)
# 	if n == 0:
# 		print i

print prim(20)

# Exercice 6

def per(n,liste=[3,0,2]):
	if n <0:
		return -1
	a = len(liste)
	if n == a-1 or n == a-2 or n == a-3:
		return liste[n]
	liste.append(liste[a-3]+liste[a-2])
	return per(n,liste)

def PriPer(n):
	if per(n)%n == 0:
		return 0
	return -1			

for i in range(2,1000):
	n = prim(i)
	k = PriPer(i)
	if n == 0:
		if k == -1:
			print "fail"
	elif k==0:
		print "fail"
			


