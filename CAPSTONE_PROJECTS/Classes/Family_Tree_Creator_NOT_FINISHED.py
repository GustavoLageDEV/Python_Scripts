#**Family Tree Creator** - Create a class called Person which will have a name, when they were born and when (and if) they died. 
#Allow the user to create these Person classes and put them into a family tree structure. Print out the tree to the screen. 

class Person:

	def __init__(self,name,birth_date,parents=(),spouse=""):

		self.name = name
		self.birth_date = birth_date
		self.death_date = None
		self.spouse = spouse
		self.parents = parents 
		self.children = []
		self.family_gen = 1
		

		if parents != ():
			p_gen = max(parents[0].family_gen,parents[1].family_gen)
			for p in parents:
				p.children.append(self)
				p.family_gen = p_gen
			self.family_gen = parents[0].family_gen + 1

		family_list.append(self)

	def add_child(self,*args): # Object Person is passed as a new child
		for child in args:
			self.children.append(child)
			child.parents.append(self)

			if self.family_gen == None:
				if self.parents == ():
					self.family_gen = 1
				else:
					self.family_gen = self.parents[0].family_gen + 1

			child.family_gen = self.family_gen + 1

def check_gen(family_list,gen): # Check if there isn't nobody on the actual generation

	for p in family_list:
		if p.family_gen == gen:
			return gen
	print(f"\n\nGeneration {gen+1}:", end="")
	return gen + 1

def display_tree(family_list):

	gen = 1
	print(30*" " + "This is our Family Tree!")
	print(f"\nGeneration {gen}:", end="")
	while family_list != []:
		gen = check_gen(family_list,gen)
		for person in family_list:
			if person.family_gen == gen: # Generation order
				if parents_list != []:
					if person.parents == parents_list[0]:
						for child in person.parents[0].children:
							if child.children != []:
								couple = child.children[0].parents
								print(f"\t{couple[0].name} S2 {couple[1].name}\t", end="")
								family_list.remove(couple[0])
								family_list.remove(couple[1])
								parents_list.append(couple)
							else:
								print("\t" + child.name, end="")
								family_list.remove(child)
						print("\t", end="")
						parents_list.remove(person.parents)
				elif person.children != []:
					couple = person.children[0].parents
					print(f"\t{couple[0].name} S2 {couple[1].name}\t", end="")
					family_list.remove(couple[0])
					family_list.remove(couple[1])
					parents_list.append(couple)
				else:
					print("\t" + person.name, end="")
					family_list.remove(person)


if __name__ == "__main__":

	family_list = []
	parents_list = []

	odin = Person("Odin",(1,1,1))
	freya = Person("Freya",(2,2,2))
	rafael = Person("Rafael",(12,8,1995),(odin,freya))
	laura = Person("Laura",(28,4,1993))
	wesley = Person("Wesley",(25,6,1987))
	alana = Person("Alana",(12,1,1988),(odin,freya))
	lionel = Person("Lionel",(20,2,2015),(rafael,laura))
	selena = Person("Selena",(14,8,2016),(rafael,laura))
	cristiano = Person("Cristiano",(5,4,2010),(wesley,alana))

	display_tree(family_list)
