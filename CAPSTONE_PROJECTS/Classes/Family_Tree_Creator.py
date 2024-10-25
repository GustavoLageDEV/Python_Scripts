#**Family Tree Creator** - Create a class called Person which will have a name, when they were born and when (and if) they died. 
#Allow the user to create these Person classes and put them into a family tree structure. Print out the tree to the screen. 

# PRIORITY FOR PRINTING (LEFT TO RIGHT):
# 1 - ORDER OF PARENTS 
# 2 - GENERATION
# 3 - MARRIED THEN SINGLES 
# 4 - AGE (OLDER TO YOUNGER) 

# FEATURES TO BE IMPLEMENTED: 
# - CHILDREN RIGHT BELOW PARENTS 

from datetime import datetime

class Person:

	def __init__(self,name,birth_date,parents=(),spouse=""):

		self.name = name
		self.birth_date = birth_date
		self.death_date = None
		self.spouse = spouse
		self.parents = parents 
		self.children = []
		self.age = datetime.today().year - datetime.strptime(birth_date, "%d-%m-%Y").year
		self.family_gen = 1
		

		if parents != ():
			p_gen = max(parents[0].family_gen,parents[1].family_gen)
			self.parents[0].spouse = self.parents[1]
			self.parents[1].spouse = self.parents[0]
			for p in parents:
				p.children.append(self)
				p.family_gen = p_gen
			self.family_gen = parents[0].family_gen + 1

		family_list.append(self)

def sort_older_to_younger(family_list): 
	if family_list == []:
		return family_list
	else:
		ages_list = []
		age_sorted_list = []
		for person in family_list:
			ages_list.append(person.age)
		ages_list.sort()
		ages_list.reverse()
		for age in ages_list:
			for person in family_list:
				if age == person.age and person not in age_sorted_list:
					age_sorted_list.append(person)

		return age_sorted_list
	
def sort_marriage(family_list): # 
	if family_list == []:
		return family_list
	else:
		for person in family_list[:][::-1]:
			if person.spouse != '':
				family_list.remove(person)
				family_list.insert(0,person)
	return family_list

def id_parents(person):
	letters_parents = ""
	for parent in person.parents:
		letters_parents += parent.name[0] + "+"
	return f"({letters_parents[:3]}) "

def check_gen(family_list,gen): 

	for p in family_list:
		if p.family_gen == gen:
			return gen
	print(f"\n\nGeneration {gen+1}:", end="")
	return gen + 1

def display_tree(family_list,children_list):
	gen = 1
	print(30*" " + "This is our Family Tree!")
	print(f"\nGeneration {gen}:", end="")
	while family_list != []:
		gen = check_gen(family_list,gen)
		singles_childs_list = []
		children_list = sort_older_to_younger(children_list)
		if children_list != []:
			for child in children_list[:]:
				if child.children != []:
					print(f"\t{id_parents(child)}{child.name} S2 {child.spouse.name} ", end="")
					family_list.remove(child)
					family_list.remove(child.spouse)
					children_list.remove(child)
					children_list.extend(child.children)
				else:
					singles_childs_list.append(child)
			singles_childs_list = sort_older_to_younger(singles_childs_list)
			for single in singles_childs_list:
				print("\t" + id_parents(single) + single.name, end="")
				print("\t", end="")
				family_list.remove(single)
				children_list.remove(single)
		else:
			family_list = sort_older_to_younger(family_list)
			for person in family_list:
				if person.family_gen == gen: # Generation order
					if person.children != []:
						couple = person.children[0].parents
						print(f"\t{couple[0].name} S2 {couple[1].name}\t", end="")
						family_list.remove(couple[0])
						family_list.remove(couple[1])
						children_list.extend(person.children)

def print_children(family_list,children_list=[]): # WORK IN PROGRESS
	gen = 1
	print(30*" " + "This is our Family Tree!")
	print(f"\nGeneration {gen}:", end="")
	while family_list != []:
		gen = check_gen(family_list,gen)
		children_list = sort_older_to_younger(children_list)
		children_list = sort_marriage(children_list)
		if children_list != []:
			for child in children_list[:]:
				if child.spouse != []:
					print(f"\t{id_parents(child)}{child.name} S2 {child.spouse.name} ", end="")
					family_list.remove(child)
					family_list.remove(child.spouse)
					if child.children_list != []:
						children_list.remove(child)
						children_list.extend(child.children)
				else:
					print("\t" + id_parents(child) + child.name, end="")
					family_list.remove(child)
					children_list.remove(child)
		else:
			family_list = sort_older_to_younger(family_list)
			for person in family_list:
				if person.family_gen == gen: # Generation order
					if person.children != []:
						print(f"\t{person.name} S2 {person.spouse.name}\t", end="")
						family_list.remove(person)
						family_list.remove(person.spouse)
						children_list.append(person.children)

if __name__ == "__main__":

	family_list = []

	odin = Person("Odin","1-1-1900")
	frigga = Person("Frigga","2-2-1900")
	rafael = Person("Rafael","22-10-1980",(odin,frigga))
	laura = Person("Laura","8-9-1982")
	wesley = Person("Wesley","7-7-1981")
	alana = Person("Alana","20-4-1972",(odin,frigga))
	lionel = Person("Lionel","22-12-2014",(rafael,laura))
	selena = Person("Selena","15-3-2010",(rafael,laura))
	cristiano = Person("Cristiano","12-2-2021",(wesley,alana))
	ronaldo = Person("Ronaldo","12-11-2022",(rafael,laura))
	thor = Person("Thor","3-3-1915",(odin,frigga))
	hela = Person("Hela","12-12-1910",(odin,frigga))
	
	display_tree(family_list,children_list)
