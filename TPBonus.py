def cut(A):
	C = [[A[i][j] for i in range(0,len(A)/2)] for j in range(0,len(A)/2)]
	D = [[A[i][j] for i in range(0,len(A)/2)] for j in range(len(A)/2,len(A))]
	E = [[A[i][j] for i in range(len(A)/2,len(A))] for j in range(0,len(A)/2)]
	F = [[A[i][j] for i in range(len(A)/2,len(A))] for j in range(len(A)/2,len(A))]	
	
	return [C,D,E,F]
	
def add(A,B):
	return [[ A[i][j] + B[i][j] for i in range(len(A))] for j in range(len(A))]
def sou(A,B):
	return [[ A[i][j] - B[i][j] for i in range(len(A))] for j in range(len(A))]

def mult(A,B):
	if len(A) == 1:
		return [[A[0][0]*B[0][0]]]
		
	AC = cut(A)
	BC = cut(B)

	
	A0B0 = mult(AC[0],BC[0])
	A0B1 = mult(AC[0],BC[1])
	A1B2 = mult(AC[1],BC[2])
	A1B3 = mult(AC[1],BC[3])
	
	A2B0 = mult(AC[2],BC[0])
	A2B1 = mult(AC[2],BC[1])
	A3B2 = mult(AC[3],BC[2])
	A3B3 = mult(AC[3],BC[3])
	
	bloc1 = add(A0B0,A1B2)
	bloc2 = add(A0B1,A1B3)
	bloc3 = add(A2B0,A3B2)
	bloc4 = add(A2B1,A3B3)
	
	bloc = [bloc1,bloc2,bloc3,bloc4]
	ret = []
	for i in range(4*len(bloc1)):	
		lis = []
		for b in bloc:
			lis = lis + bloc
		ret = ret + lis
	return ret		
	
	
print mult([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],[[2,3,4,5],[6,7,8,9],[2,3,4,5],[6,7,8,9]])	

def multStrassen(A,B):

	if len(A) == 1:
		return [[A[0][0]*B[0][0]]]
			
	AC = cut(A)
	BC = cut(B)

	P1 = multStrassen(AC[0],sou(BC[1],BC[3]))
	P2 = multStrassen(add(AC[0],AC[1]),BC[3])
	P3 = multStrassen(add(AC[2],AC[3]),BC[0])
	P4 = multStrassen(AC[3],sou(BC[2],BC[0]))
	P5 = multStrassen(add(AC[0],AC[3]),add(BC[0],BC[3]))
	P6 = multStrassen(sou(AC[1],AC[3]),add(BC[2],BC[3]))
	P7 = multStrassen(sou(AC[0],AC[2]),add(BC[0],BC[1]))
	
	bloc1 = add(P5,add(P6,sou(P4,P2)))
	bloc2 = add(P1,P2)
	bloc3 = add(P3,P4)
	bloc4 = add(sou(P5,P7),sou(P1,P3))
	
	return [[bloc1[0][0],bloc2[0][0]],[bloc3[0][0],bloc4[0][0]]]	
	
#print multStrassen([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],[[2,3,4,5],[6,7,8,9],[2,3,4,5],[6,7,8,9]])	