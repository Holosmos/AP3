# Ex 1

class Rectangle(object):
	
	nom = 'rectangle'
	
	def __init__(self, long, larg):
		self.long = float(long)
		self.larg = float(larg)
			
			
	def __str__(self):
		return "Rectangle de longueur %s et de largeur %s. Type : %s" %(str(self.larg),str(self.long),self.nom)
		
	def surface(self):
		return self.larg*self.long	
		
class Carre(Rectangle):
	
	def __init__(self,long):
		super(Carre,self).__init__(long,long)
		self.nom = "carre"

# a = Rectangle(2,3)
# print a				
# b = Carre(3)
# print b


class Point(object):

	def __init__(self, x = 0., y = 0.):
		self.x = float(x)
		self.y = float(y)
		
	def __str__(self):
		return "(%s,%s)" %(str(self.x),str(self.y))	
	
class Segment(object):
	
	def __init__(self, xA, yA, xB, yB):
		self.orig = Point(xA,yA)
		self.extrem = Point(xB,yB)
	
	def __str__(self):
		return "Segment entre %s et %s." %(self.orig.__str__(), self.extrem.__str__())

# a = Point(1,2.5)
# print a
# 
# b = Segment(0,1,2,3)
# print b		
		

# Ex 2

class Vecteur(object):
	
	def __init__(self, *valeur):
		self.__val = []
		try:
			for a in valeur:
				assert type(a) is float or type(a) is int
				self.__val.append(a)
		except:
			assert len(valeur)==1
			a = valeur[0]
			assert isinstance(a,Vecteur)
			for i in range(a.len()):
				self.__val.append(a.__val[i])
	
	def __str__(self):
		return "%s" %str(self.__val)		
		
	@staticmethod
	def zeros(a):
		b = int(a)
		c = [0 for i in range(b)]
		return Vecteur(*c)
		
	def __getitem__(self,i):
		j = int(i)
		try:
			assert j < len(self.__val) and j >= 0
			return self.__val[j]
		except:
			True	
	def __setitem__(self,i,a):
		j = int(i)
		b = float(a)
		try:
			assert j < len(self.__val) and j >=0
			self.__val[j] = b
		except:
			True			
			
	def len(self):
		return len(self.__val)
			
	def __neg__(self):
		return Vecteur(*[-self[i] for i in range(len(self.__val))])						
			
	def __add__(self, other):
		try:
			assert isinstance(other, Vecteur)
			assert other.len() == self.len()
			return Vecteur(*[self[i]+other[i] for i in range(self.len())])
		except:
			True	
	def __sub__(self, other):
		try:
			assert isinstance(other, Vecteur)
			assert other.len() == self.len()
			return self + (-other)		
		except:
			True
			
	def __mul__(self,other):
		a = float(other)
		return Vecteur(*[self[i]*a for i in range(self.len())])
	def __rmul__(self,other):
		return self*other
		
	def __cmp__(self, other):
		try:
			assert isinstance(other,Vecteur)
			assert other.len() == self.len()
			for i in range(self.len()):
				if self[i]!= other[i]:
					return 1
			return 0
		except:
			return 1						
			
# a = Vecteur(1,2)
# print a	
# 
# b = Vecteur.zeros(2)
# print b[1]
# b[1] = 2
# print b
# 
# print 2*a
# 
# print a == 2*a
# print a != 2*a
# print a == a
		
		
class Matrice(object):
	
	def __init__(self, *list):
		self.__val = []
		if len(list)!=0:
			self.li = len(list)
			if isinstance(list[0],Vecteur):
				self.col = list[0].len()
				self.__val.append(list[0])
				for i in range(1,len(list)):
					if isinstance(list[i],Vecteur):
						self.__val.append(list[i])	
			elif isinstance(list[0],Matrice):
				mat = list[0]
				self.li = mat.li
				self.col = mat.col
				self.__val = []
				for i in range(0,self.li):
					self.__val.append(Vecteur(*[mat[i,j] for j in range(self.col)]))			
		else:
			raise ValueError("Mauvaise entree")		
	def __getitem__(self, i):
		try:
			assert type(i) is tuple
			assert len(i) == 2
			assert type(i[0]) is int
			assert type(i[1]) is int
			a = self.__val[i[0]]
			
			return a[i[1]]
		except:
			try:
				assert i >= 0 and i < self.li
				return self.__val[i]
			except:
				True	
	def __setitem__(self, i , a):	
		try :	
 			assert type(i) is tuple
 			assert len(i) == 2
 			assert type(i[0]) is int
 			assert type(i[1]) is int
			v = self.__val[i[0]]
			v[i[1]] = float(a)
			self.__val[i[0]] = v
		except:	
			 try:
	 			assert type(i) is int
	 			assert i >= 0 and i < self.li
	 			assert isinstance(a,Vecteur)
	 			self.__val[i] = a
			 except:
				True
	
	def __str__(self):
		st = ""
		for i in range(self.li):
			for j in range(self.col):
				st += str(self[i,j]) + "\t"
			st += "\n"				
		return st
	
	@staticmethod
	def zeros(*args):
		try:
			assert len(args) >= 2
			n = int(args[0])
			m = int(args[1])
			v = Vecteur.zeros(m)
			return Matrice(*[Vecteur(v) for i in range(n)])
		except:
			try:
				assert len(args) == 1
				n = int(args[0])
				v = Vecteur.zeros(n)		
				return Matrice(*[Vecteur(v) for i in range(n)])
			except:
				True
	@staticmethod
	def identite(i):
		n = int(i)
		m = Matrice.zeros(n)
		for j in range(n):
			m[j,j] = 1
		return m			
		
	def __mul__(self, other):
		try:
			assert isinstance(other,Matrice)
			assert other.li == self.col
			
			res = Matrice.zeros(self.li,other.col)
			for i in range(self.li):
				for j in range(other.col):
					for k in range(self.col):
						res[i,j] += self[i,k]*other[k,j]
			return res
		except:
			try:
				a = float(other)
				return Matrice(*[a*self[i] for i in range(self.li)]) 
			except:	
				True		
	def __rmul__(self,other):
		other.__mul(self)
		
	def __add__(self,other):
		try:
			assert isinstance(other,Matrice)
			assert other.li == self.li
			assert other.col == self.col
			return Matrice(*[self[i]+other[i] for i in range(self.li)])
		except:
			True	
	def __radd__(self,other):
		return self+other	
	
	def __sub__(self,other):
		try:
			assert isinstance(other,Matrice)
			assert other.li == self.li
			assert other.col == self.col
			return Matrice(*[self[i]-other[i] for i in range(self.li)])	
		except:
			True		
			
	def __cmp__(self,other):
		try:
			assert isinstance(other,Matrice)
			assert other.li == self.li
			assert other.col == self.col
			for i in range(self.li):
				for j in range(self.col):
					assert self[i,j] == other[i,j]
			return 0
		except:
			return 1		

	
	# Gauss
	
	def __multLigne(self,i,a):
		e = Matrice.identite(self.col)
		e[i,i] = a
		return e
	def __permLignes(self,i,j):
		e = Matrice.identite(self.col)
		e[i,i] = 0
		e[j,j] = 0
		e[j,i] = 1
		e[i,j] = 1
		return e
	def __addLigne(self,i,j,a):
		e = Matrice.identite(self.col)
		e[j,i] = a
		return e
		
	def gauss(self):
		cop = Matrice(self)
		ans = Matrice.identite(self.li)
		for j in range(self.col):
			for i in range(j,self.li):
				if cop[i,j]!= 0:
					t = cop.__permLignes(i,j)
					cop = t*cop
					ans = t*ans
					
					t = cop.__multLigne(j,1./cop[j,j])
					cop = t*cop
					ans = t*ans
					
					break
					
			for i in range(self.li):
				if i!= j:
					t = cop.__addLigne(j,i,-cop[i,j])	
					cop = t*cop
					ans = t*ans	
				
		return ans
	def det(self):
		cop = Matrice(self)
		ans = Matrice.identite(self.li)
		det = 1.
		for j in range(self.col):
			c = det
			det = 0
			for i in range(j,self.li):
				if cop[i,j]!= 0:
					t = cop.__permLignes(i,j)
					cop = t*cop
					ans = t*ans
					
					det = c
					det *= (-1)**(i-j)
					det *= cop[j,j]
					
					t = cop.__multLigne(j,1./cop[j,j])
					cop = t*cop
					ans = t*ans
					
					break
					
			for i in range(self.li):
				if i!= j:
					t = cop.__addLigne(j,i,-cop[i,j])	
					cop = t*cop
					ans = t*ans	
				
		return det
		

a = Vecteur(1,2)
b = Vecteur(3,4)
c = Matrice(a,b)
print c
print c.det()	

		
		
		
		
		
		
				
				
				
				
					