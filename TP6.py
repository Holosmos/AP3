class Rectangle():
	
	def __init__(self, long, larg):
		if type(long) is float :
			self.long = long
		else :
			raise ValueError('La longueur doit être un nombre')	
		if type(larg) is float :
			self.larg = larg
		else :
			raise ValueError('La largeur doit être un nombre')
			
	def __str__(self):
		return "Rectangle de longueur %d et de largeur %d" %(larg,long)
		

a = Rectangle(2,3)
print a				
