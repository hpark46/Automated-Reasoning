from CNF_Converter import *
import itertools
import copy



def pl_resolution(background, query):

	background.append(Negation(query))
	kb = simplifier(to_cnf(background))
	new = []



	for i in range(0,len(kb)):
		for clause in kb[i+1:]:
			resolvent = pl_resolve(kb[i], clause)

			if (resolvent == []):
				return True

			new = new + resolvent

	if ()



















def pl_resolve(ci, cj):

	if (len(ci) == len(cj) == 1):
		if (ci[0] == cj[0] and ci[1] != cj[1]):
			return []



	result = []
	together = []

	for i in ci:
		together.append(i)

	for j in cj:
		together.append(j)

	together.sort()
	together = set(together)

	contrary = [] 						
	for i in range(1,len(together)-1):
		if (together[i][0] == together[i-1][0] or together[i][0] == together[i+1][0]):
			contrary.append(together[i][0])


	contrary = set(contrary) # set of 'opposing sign of literals'

	subsets = []
	for i in range(1, len(contrary)+1):
		subset = subset + list(itertools.combinations(contrary, i))


	for subset in subset:
		temp = copy.deepcopy(list(together))
		for symbols in subset:
			temp.remove((symbols, 1))
			temp.remove((symbols, -1))
		result.append(temp)

	return result























# convert pl to simplified form (Literal, 1/0) (1: positive 0: negative)

def simplifier(CNF):
	cnf = []

	for element in CNF:
		clause = []
		dfs(element, 1, clause)
		cnf.append(clause)

	return cnf





def dfs(element, neg, clause):

	if (element.__class__.__name__ == "Literal"):
		clause.append((element.symbol, neg))

	elif (element.__class__.__name__ == "Disjunction"):

		dfs(element.sentence_f, 1, clause)
		dfs(element.sentence_b, 1, clause)

	elif (element.__class__.__name__ == "Negation"):
		dfs(element.sentence_f, -1, clause)

























if __name__ == "__main__":
	KB = []
	s1 = Literal("P1,1")
	s2 = Literal("P1,2")
	s3 = Literal("P2,1")
	s4 = Literal("P2,2")
	s5 = Literal("P3,1")
	s6 = Literal("B1,1")
	s7 = Literal("B2,1")



	# KB.append(Negation(s1))												#r1
	KB.append(Biconditional(s6, Disjunction(s2, s3)))					#r2
	# KB.append(Biconditional(s7, Disjunction(s1, Disjunction(s4, s5))))	#r3
	# KB.append(Negation(s6))												#r4
	# KB.append(s7)														#r5


	# temp = to_cnf(KB)
	# print(temp)
	# print("**********")
	# temp_two = simplifier(temp)




	# temp_two = (temp[2].sentence_b.symbol, 0)
	# print(temp_two)
	# print(temp_two)





















