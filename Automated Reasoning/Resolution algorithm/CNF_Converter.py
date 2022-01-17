from Literal import *
from Biconditional import *
from Conjunction import *
from Disjunction import *
from Implication import *
from Negation import *


def to_cnf(KB):

	cnf = [] #clauses

	for clause in KB:
		result = [] 
		result.append(clause)

		while(len(result) != 0):
			# print(str(result) + "result")
			# print(str(cnf) + "cnf")

			temp = result.pop(0)

			if (check_clean(temp)):
				cnf.append(temp)

			else:

				if (temp.__class__.__name__ == "Negation"):
					n = break_negation(temp)
					result.append(n)

				elif (temp.__class__.__name__ == "Conjunction"):
					a, b = break_conjunction(temp)
					result.append(a)
					result.append(b)

				elif (temp.__class__.__name__ == "Disjunction"):
					c = break_disjunction(temp)
					result.append(c)

				elif (temp.__class__.__name__ == "Implication"):
					d = break_implication(temp)
					result.append(d)

				elif (temp.__class__.__name__ == "Biconditional"):
					e = break_biconditional(temp)
					result.append(e)

				else:
					print(3)
					print(temp.__class__.__name__)

	return cnf








# iterate throguh clause and check if its all disjunction or negative
# append all literals of the clause into an array + get rid of negative

# Negation: contains sentence_f (lhs) only

def check_clean(clause):
	

	if (clause.__class__.__name__ == "Literal"):
		return True

	elif (clause.__class__.__name__ == "Negation"):
		if (clause.sentence_f.__class__.__name__ != "Literal"):
			return False
		else:
			return True

	elif (clause.__class__.__name__ == "Disjunction"):
		return check_clean(clause.sentence_f) and check_clean(clause.sentence_b)

	else:
		return False





def break_biconditional(clause):
	return Conjunction(Implication(clause.sentence_f, clause.sentence_b), Implication(clause.sentence_b, clause.sentence_f))

def break_implication(clause):
	return Disjunction(break_negation(Negation(clause.sentence_f)), clause.sentence_b)

# does not work for clause containing implication/biconditional
def break_negation(clause):

	child = clause.sentence_f

	if (child.__class__.__name__ == "Conjunction"): #de morgan
		return Disjunction(break_negation(Negation(child.sentence_f)), break_negation(Negation(child.sentence_b)))#, 1 # change made

	elif (child.__class__.__name__ == "Disjunction"): #de morgan
		return Conjunction(break_negation(Negation(child.sentence_f)), break_negation(Negation(child.sentence_b)))#, 1 # change made

	elif (child.__class__.__name__ == "Negation"): #double negation 
		return child.sentence_f#, 1 #change made

	else:
		# print(4)
		return clause#, 0 #no change made


def break_conjunction(clause):
	return clause.sentence_f, clause.sentence_b

def break_disjunction(clause):
	if (clause.sentence_f.__class__.__name__ == "Conjunction" and clause.sentence_b.__class__.__name__ != "Conjunction"):
		return Conjunction(Disjunction(clause.sentence_f.sentence_f, clause.sentence_b), Disjunction(clause.sentence_f.sentence_b, clause.sentence_b))#, 1

	elif (clause.sentence_b.__class__.__name__ == "Conjunction"):
		return Conjunction(Disjunction(clause.sentence_f, clause.sentence_b.sentence_f), Disjunction(clause.sentence_f, clause.sentence_b.sentence_b))#, 1

	else:
		# print(str(clause.sentence_f.__class__.__name__) + str(clause.sentence_b.__class__.__name__) + "5")
		print(5)

		return clause#, 0 #no change








if __name__ == "__main__":
	KB = []
	s1 = Literal("P1,1")
	s2 = Literal("P1,2")
	s3 = Literal("P2,1")
	s4 = Literal("P2,2")
	s5 = Literal("P3,1")
	s6 = Literal("B1,1")
	s7 = Literal("B2,1")



	KB.append(Negation(s1))												#r1
	KB.append(Biconditional(s6, Disjunction(s2, s3)))					#r2
	KB.append(Biconditional(s7, Disjunction(s1, Disjunction(s4, s5))))	#r3
	KB.append(Negation(s6))												#r4
	KB.append(s7)														#r5


	temp = to_cnf(KB)
	# print(temp)
	# print("**********")


	temp_two = (temp[2].sentence_b.symbol, 0)
	print(temp_two)

	


