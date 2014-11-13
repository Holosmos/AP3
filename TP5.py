def rechercheMotifNaif(C,M):
	a = len(M)
	b = len(C)
	S = []
	for i in range(b-a+1):
		K = C[i:i+a]
		test = True
		for j in range(a):
			if M[j] != '*' and M[j] != K[j]:
				test = False
		if test:		
			S = S+[i]	
	return S		
			
#print rechercheMotifNaif([3,4,1,5,1,2,1,2],['*'])				

def rechercheMotif2DNaif(C,M):
	a = len(M)
	b = len(M[0])
	S = []
	for i in range(len(C)-a+1):
		for j in range(len(C[0])-b+1):
			K = []
			for x in range(a):
				L = C[i+x]
				K.append(L[j:j+b])
			test = True
			for x in range(a):
				for y in range(b):
					if M[x][y] != '*' and M[x][y] != K[x][y]:
						test = False
			if test:
				S = S + [(i,j)]
	return S

C = [[1,2,3],[4,5,6],[7,4,9]]
M = [[4,'*']]
print rechercheMotif2DNaif(C,M)

def Horner(w):
	T = [int(w[i]) for i in range(len(w)-1,-1,-1)]
	res = 0
	for i in range(len(T)-1,-1,-1):
		res *= 10
		res += T[i]
	return res

#print Horner('123')	

def KarpRabin(C,M,q):
	lc = len(C)
	lm = len(M)
	m,c = 0,0
	S = []
	for i in range(lm):
		m = (10*m + int(M[i])) % q
		c = (10*c + int(C[i])) % q
	h = 10**(lm-1) % q	
	for i in range(lc-lm+1):
		if m == c:
			if M[0:lm] == C[i:i+lm]:
				S = S+[i,]
		if i < lc-lm:
			c = (10*(c-int(C[i])*h) + int(C[i+lm])) % q
	return S					
#print KarpRabin('1231564234123156','15',10)

	
def TabDyn(u,v):
	A = [[0 for i in range(len(v)+1)]for j in range(len(u)+1)]
	L = [[0 for i in range(len(v)+1)]for j in range(len(u)+1)]
	for i in range(len(u)):
		for j in range(len(v)):
			if A[i][j+1]>A[i+1][j]:
				L[i+1][j+1] = 'n'
				A[i+1][j+1] = A[i][j+1]
			else:
				L[i+1][j+1] = 'o'
				A[i+1][j+1] = A[i+1][j]
			if u[i] == v[j] and A[i+1][j+1] < 1 + A[i][j]:
				L[i+1][j+1] = 'no'
				A[i+1][j+1] = 1 + A[i][j]				
				
	return A,L		

A,L = TabDyn('abcaa','abcabc')
#print [[L[i][j] for j in range(1,len(L[i]))]for i in range(1,len(L))]

def min(a,b):
	if a < b :
		return a
	return b	

def LCS(u,v):
	A,L = TabDyn(u,v)
	k,i,j = 0,len(u),len(v)
	z = []
	while min(i,j) >= 0:
		if L[i][j] == 'no':
			k += 1
			z.append(u[i-1])
			i -= 1
			j -= 1
		elif L[i][j] == 'o':
			j -= 1
		else:
			i -= 1		
	return [z[i] for i in range(len(z)-1,-1,-1)]

#print LCS('atgcg','agcccc  ')		

def max(a,b):
	return a if a > b else b

def RuckSack(poids,val,W):
	n = len(poids)
	kp = [[0 for j in range(W+1)] for i in range(n+1)]
	for i in range(1,n+1,1):
		for c in range(1,W+1,1):
			if c >= poids[i-1]:
				kp[i][c] = max(kp[i-1][c],val[i-1]+kp[i-1][c-poids[i-1]])
			else:
				kp[i][c] = kp[i-1][c]
	x = [0 for i in range(n)]
	c = W
	for i in range(n,0,-1):
		if kp[i][c] != kp[i-1][c]:
			x[i-1] = 1
			c = c-poids[i-1]
	return x, kp		

#print RuckSack((1,2,3),(1,3,5),3)	
					


							