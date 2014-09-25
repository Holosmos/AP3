#! /usr/bin/env python

import argparse

def maximum(n,m):
	if n>= m:
		return n
	return m

def milieu(n,m,p):
	l = [n,m,p]
	l.sort()
	return l[1]
#print(milieu(1,2,3))
#print(milieu(1,3,2))
#print(milieu(3,1,3))


i = 1
a= "0"
while i<= 10:
	a = a + " " + str(i*7)
	i+=1
#print a

l = [1,11,3,45,67,2,456]

for i in range(len(l)):
	a = l[i]
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
	for i in range(a):
		case = l[i]
		if type(case) is int:
			somme+= l[i]
		else:
			return "Erreur de types"		
	return somme
	
#print somme_liste_entier([1,2,3],0,2)
#print somme_liste_entier([1,2,3],0,3)
#print somme_liste_entier([1,2,3],2,2)
#print somme_liste_entier([1,2,'a'],0,2)	


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
	chaine = "Nombres pairs :"
	for i in range(1,x):
		chaine += " " + str(2*i)
	print(chaine)
	chaine = "Nombres impairs :"
	for i in range(1,x):
		chaine += " " + str(2*(x-i)-1)
	print(chaine)		
	

parser = argparse.ArgumentParser()
parser.add_argument("param", type = int)

args = parser.parse_args()

PairsImpairs(args.param)






	


	