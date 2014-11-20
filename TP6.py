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
			True
	
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
		
		
		
		
		
		
		
		
		
		
		
					