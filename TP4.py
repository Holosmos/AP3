# Exercice 1

def merge(L1,L2):
	L = []
	j = 0
	for i in range(len(L1)):
		while j < len(L2):
			if L2[j] < L1[i]:
				L.append(L2[j])
				j += 1
			else:
				break
		L.append(L1[i])
	if j < len(L2):
		L = L + L2[j:len(L2)]				
	return L

# print merge([1,2,5,6],[2,3,4,7,8])				

def mergeSort(L):
	if len(L) <= 1:
		return L
	A = L[0:len(L)/2]
	B = L[len(L)/2:len(L)]
	A,B = mergeSort(A),mergeSort(B)	
	return merge(A,B)
	
# print mergeSort([12,3,32,8,6,9,13])	

# Exercice 2

def maxL(L,a,b):
	if L[a] > L[b]:
		return a
	return b	
	
def tasNouvelIndice(L,p,fin):
	test = False
	
	while not test:
		test = True
		l = 2*p+1
		r = 2*p+2
		m = p
		if l <= fin and L[l] > L[m]:
			m = l
		if r <= fin and L[r] > L[m]:
			m = r
		if m != p:
			L[m],L[p] = L[p],L[m]
			p = m
			test = False	
				
def miseEnTas(L):
	n = len(L)
	for i in range(n/2-1,-1,-1):
		tasNouvelIndice(L,i,n-1)
	return L	
def triParTas(L):
	n = len(L)
	miseEnTas(L)
	for i in range(n-1,0,-1):
		print " ---- " 
		L[i],L[0] = L[0],L[i]
		print L
		tasNouvelIndice(L,0,i-1)
		print L
	return L	

print triParTas([7,4,2,5,3,8,4,10])