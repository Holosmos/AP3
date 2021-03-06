import math
import random

def prem(n):
	for i in range(2,int(math.sqrt(n))):
		if n%i == 0: return False
	return n>1
	
# print prem(2)
# print prem(3)
# print prem(4)	
# print prem(21)
# print prem(23)

def decomp(n):
	s = 0
	while n%2==0:
		s+=1
		n/=2
	return (s,n)

# print decomp(20)	

def temoin(n,s,d,a):
	if (a**d)%n==1: return False
	dR = d
	for r in range(s):
		k = a**dR
		if k%n == n-1: return False
		dR *= 2
	return True
	
def MillerRabin(n,k=10):
	s,d = decomp(n-1)
	for i in range(k):
		a = random.randint(1,n-1)
		if temoin(n,s,d,a): return False
	return True
	
#print MillerRabin(21)
#print MillerRabin(23)		
print MillerRabin(113,1)	
