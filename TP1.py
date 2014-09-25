#! /usr/bin/env python

import argparse

def maximum(n,m):
	return (n+m+abs(n-m))/2

#def milieu(n,m,p):
#	l = [n,m,p]
#	l.sort()
#	return l[1]
def milieu(n,m,p):
	a = maximum(n,maximum(m,p))
	if n==m or n == p or m == p:
		return maximum(n,maximum(m,p))
	if a == p:
		return maximum(n,m)
	return milieu(p,n,m)	
#print(milieu(1,2,3))
#print(milieu(1,3,2))
#print(milieu(3,1,3))

def croucrou(n,m,p):
	a = max(n,m)
	b = max(m,p)
	c = max(p,n)
	
	d = max(a,b)
	
	if d == n:
		return max(m,p)
	else:
		if d ==m :
			return max(n,p)
		else:
			return max(n,m)
						
#print(croucrou(1,2,3))
#print(croucrou(1,3,2))
#print(croucrou(3,1,3))		

i = 1
a= "0"
while i<= 10:
	a = a + " " + str(i*7)
	i+=1
#print a

l = [1,11,3,45,67,2,456]

for a in l:
	#if a <= 10:
		#print(a)
		

def somme_entier(n,m):
	return (n+m)*(m-n+1)/2

#print(somme_entier(1,5))
#print(somme_entier(2,5))
#print(somme_entier(100,101))

def somme_liste_entier(l,n,m):
	a = len(l)
	if n>=a or m>= a or n<0 or m<0:
		return "Erreur de portee"
	somme=0
	for i in range(n,m):
		case = l[i]
		if type(case) is int:
			somme+= l[i]
		else:
			return "Erreur de types"		
	return somme
	
print somme_liste_entier([1,2,3],0,2)
print somme_liste_entier([1,2,3],0,3)
print somme_liste_entier([1,2,3],2,2)
print somme_liste_entier([1,2,'a'],0,2)	


def sous_chaine(ch,n,m):
	li = ch.rsplit()
	la =[]
	for i in range(len(li)):
		if i >= n and i <= m:
			la.append(li[i])
	return " ".join(la)

#print(sous_chaine("Coucou tout le monde !",2,4))
#print(sous_chaine("Coucou tout le monde !",0,10))
#print(sous_chaine("Coucou tout le monde !",10,10))		

def PairsImpairs(x):
	chaine1 = "Nombres pairs :"
	chaine2 = "Nombres impairs :"
	for i in range(1,x):
		chaine1 += " " + str(2*i)
		chaine2 += " " + str(2*(x-i)-1)
	print(chaine1)
	print(chaine2)		
	

#parser = argparse.ArgumentParser()
#parser.add_argument("param", type = int)
#args = parser.parse_args()
#PairsImpairs(args.param)






	


	