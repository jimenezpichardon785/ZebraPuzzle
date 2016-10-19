'''
Nerys Jimenez Pichardo
The College of Saint Rose
Spring 2016
Artificial Intelligence

zebra puzzle solver
'''
from itertools import permutations
from collections import namedtuple

colors = ['red', 'green', 'ivory', 'yellow', 'blue']
drinks = ['tea','coffee','milk','orange juice','water']
pets = ['dog','snails','fox','horse','zebra']
smokes = ['Old Gold', 'Kools','Chesterfield','Lucky Strike','Parliament']
nationalities = ['Englishman','Spaniard','Ukrainian','Norwegian','Japanese']
houses = range(len(colors))

PossibleSolution = namedtuple('PossibleSolution',
								['nationality','color','drink','smoke','pet'])
								
								
PossibleSolution.__new__.__defaults__ =(None,) *len(PossibleSolution._fields)


#Test solution against all hints and returns true if satisfies all hints
def does_solution_fit(hints, solution):
	return all(hint(solution) for hint in hints)

#The Englishman lives in the red house
def hint2(s):	
	if(s.nationality is None) or (s.color is None):
		return True
	
	for house in houses:
		if s.nationality[house] == 'Englishman' and s.color[house] == 'red':
			return True
	return False

#The Spaniard owns the dog
def hint3(s):
	if(s.nationality is None) or (s.pet is None):
		return True
	for house in houses:
		if s.nationality[house] == 'Spaniard' and s.pet[house] == 'dog':
			return True
	return False

#Coffee is drunk in green house
def hint4(s):
	if(s.drink is None) or (s.color is None):
		return True
	for house in houses:
		if s.drink[house] == 'coffee' and s.color[house] == 'green':
			return True
	return False

#Ukrainian drinks tea
def hint5(s):
	if(s.nationality is None) or (s.drink is None):
		return True
	for house in houses:
		if s.nationality[house] == 'Ukrainian' and s.drink[house] == 'tea':
			return True
	return False

#The green house is immediately to the right of the ivory house
def hint6(s):
	if s.color is None:
		return True
	for house in houses [:len(houses)-1]:
		if s.color[house] == 'ivory' and s.color[house+1] == 'green':
			return True
	return False

#The old gold smoker owns snails
def hint7(s):
	if (s.smoke is None) or (s.pet is None):
		return True
	for house in houses:
		if s.smoke[house] == 'Old Gold' and s.pet[house] == 'snails':
			return True
	return False
	
#Kools are smoked in the yellow house
def hint8(s):
	if(s.color is None) or (s.smoke is None):
		return True
	for house in houses:
		if s.color[house] == 'yellow' and s.smoke[house] == 'Kools':
			return True
	return False

#milk is drunk in the middle house
def hint9(s):
	if s.drink is None:
		return True
	if s.drink [2] == 'milk':
		return True
	else:
		return False

#The Norwegian lives in the first house
def hint10(s):
	if s.nationality[0] == 'Norwegian':
		return True
	else:
		return False

#The man who smokes Chesterfields live in the house next to the man with the fox
def hint11(s):
	if(s.smoke is None) or (s.pet is None):
		return True
	if abs(s.smoke.index('Chesterfield') - s.pet.index('fox')) == 1:
		return True
	return False
	
#Kools are smoked in the house next to the house where the horse is kept
def hint12(s):
	if(s.smoke is None) or (s.pet is None):
		return True
	if abs(s.smoke.index('Kools') - s.pet.index('horse')) == 1:
		return True
	return False

#The Lucky Strike smoker drinks orange juice
def hint13(s):
	if(s.smoke is None) or (s.drink is None):
		return True
	for house in houses:
		if s.smoke[house] == 'Lucky Strike' and s.drink[house] == 'orange juice':
			return True
	return False
	
#The Japanese smokes parliaments
def hint14(s):
	if(s.nationality is None) or (s.smoke is None):
		return True
	for house in houses:
		if s.smoke[house] == 'Parliament' and s.nationality[house] == 'Japanese':
			return True
	return False
	
#The Norwegian lives next to the blue house
def hint15(s):
	if(s.nationality is None) or (s.color is None):
		return True
	if abs(s.nationality.index('Norwegian') - s.color.index('blue')) == 1:
		return True
	return False

hints = [hint2, hint3, hint4, hint5, hint6, hint7, hint8, hint9,
			hint10, hint11, hint12, hint13, hint14, hint15]	

def find_solutions():
	for n in permutations(nationalities):
		if does_solution_fit(hints, PossibleSolution(n)):
			for c in permutations(colors):
				if does_solution_fit(hints, PossibleSolution(n, c)):
					for d in permutations(drinks):
						if does_solution_fit(hints, PossibleSolution(n, c, d)):
							for s in permutations(smokes):
								if does_solution_fit(hints, PossibleSolution(n, c, d, s)):
									for p in permutations(pets):
										if does_solution_fit(hints, PossibleSolution(n, c, d, s, p)):
											yield PossibleSolution(n, c, d, s, p)

#prints solution											
def show(solution):
	row_names = ('Nationality', 'Color', 'Drink', 'Smoke', 'Pet')
	row_format = '{:<18}'
	
	row = [row_format.format('House')]
	for house in houses:
		row.append(row_format.format(house+1))
	print ''.join(row)
	
	for(row_name, row_values) in zip(row_names, solution):
		row = [row_format.format(row_name)]
		for value in row_values:
			row.append(row_format.format(value))
		print ''.join(row)
		
for sol in list(find_solutions()):
	show(sol)
