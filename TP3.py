# Exercice 1

import random
L = [random.randrange(0,50) for i in range(10)]
#	print L

def triBulle(L):
	a = len(L)
	i = 0
	while i < (a-1):
		if L[i] > L[i+1]:
			L[i],L[i+1] = L[i+1],L[i]
			i = -1
		i += 1		 
	return L
	
# print triBulle(L)		

def triBulleOpt(L):
	a = len(L)
	i = 0
	mem = a-1
	test = True
	while test:
		test = False
		while i < mem:
			if L[i] > L[i+1]:
				L[i],L[i+1] = L[i+1],L[i]
				test = True
				if mem < i :
					mem = i
			i += 1		
		i = 0
	return L	

# print triBulleOpt(L)	

# Exercice 2

def rechercheMax(L,d = 0,f = len(L) - 1):
	max = d
	for i in range(d+1,f+1):
		if L[i] > L[max]:
			max = i
	return max
			
# print rechercheMax(L)			

def triSelection(L):
	for i in range(len(L)-1):
		max = rechercheMax(L,0,len(L) - 1 - i)
		L[len(L) - 1 -i],L[max] = L[max],L[len(L) - 1-i]
	return L

# print triSelection(L)	

# Exercice 3	

def rechercheDicho(L,x,d=0,f=len(L)-1):
	for i in range(d,f+1):
		if L[i] == x:
			return i
	return None

# print rechercheDicho(L,23)			

# Exercice 4

def triInsertion(L):
	if len(L) > 0:
		if L[0] > L[1]:
			L[0],L[1] = L[1],L[0]
	for i in range(2,len(L)):
		test = False
		for j in range(i):
			if L[j]>L[i]:
				test = True
				break
		if test:
			if j == 0:
				L1 = [L[i]]
			else :				
				L1 = [L[k] for k in range(j)]
				L1.append(L[i])
				
			L2 = [L[k] for k in range(j,i)]
			L3 = [L[k] for k in range(i+1,len(L))]
			L = L1
			if len(L2) > 0:
				L = L + L2
			if len(L3) > 0:
				L = L + L3	
	return L		

# print triInsertion(L)

def triInsertDich(L):
	if len(L) > 0:
		if L[0] > L[1]:
			L[0],L[1] = L[1],L[0]		
	i = 2		
	while i < len(L):
		test = False
		j = rechDich(L,i,i)
		if j != i:
			test = True
		i = i+1		
		if test:
			if j == 0:
				L1 = [L[i]]
			else :				
				L1 = [L[k] for k in range(j)]
				L1.append(L[i])
				
			L2 = [L[k] for k in range(j,i)]
			L3 = [L[k] for k in range(i+1,len(L))]
			L = L1
			if len(L2) > 0:
				L = L + L2
			if len(L3) > 0:
				L = L + L3	
			i = i-1	
	return L		
				
def max(a,b):
	if a > b:
		return a
	return b					
def rechDich(L,i, k, d = 0):
	print str([L[m] for m in range(d,k+1)]) + str(L[i])
	if k-d <= 1:
		if L[k] <= L[i]:
			return k
		if L[d] >= L[i]:
			return d
		return d+1		
		
	if L[(d+k)/2] >= L[i]:
		return rechDich(L,i,(d+k)/2,d)
	return rechDich(L,i,k,(d+k)/2+1)		
	
print triInsertDich([39, 2, 31, 31, 37, 17, 33, 11, 10, 39])

#print rechDich([2, 10, 11, 17, 31, 31, 33, 37, 39, 39],9,9)

