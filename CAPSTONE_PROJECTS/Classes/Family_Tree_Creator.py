#**Family Tree Creator** - Create a class called Person which will have a name, when they were born and when (and if) they died. 
#Allow the user to create these Person classes and put them into a family tree structure. Print out the tree to the screen. 

class Person:

	def __init__(self,name,birth_date,death_date=None):

		self.name = name
		self.birth_date = birth_date
		self.death_date = death_date
		self.parents = []
		self.children = []
		self.family_gen = None

	def add_child(self,*args):
		for child in args:
			self.children.append(child)
			child.parents.append(self)

			if self.family_gen == None:
				if self.parents == []:
					self.family_gen = 1
				else:
					self.family_gen = self.parents[0].family_gen + 1

			child.family_gen = self.family_gen + 1


def display_tree(*args):

	print("This is our Family Tree\n")
	family_list = []
	gen = 1
	
	for person in args:
		family_list.append(person)

	while family_list != []:
		print(f"Generation {gen}")
		for person in family_list:
			if person.family_gen == gen:
			print(f"{person.name}")
			family_list.pop(person)

			
		gen += 1
		

if __name__ == "__main__":

	rafael = Person("Rafael",(12,8,1995))
	laura = Person("Laura",(28,4,1993))
	lionel = Person("Lionel",(20,2,2015))
	selena = Person("Selena",(14,8,2016))

	rafael.add_child(lionel,selena)
	laura.add_child(lionel,selena)


