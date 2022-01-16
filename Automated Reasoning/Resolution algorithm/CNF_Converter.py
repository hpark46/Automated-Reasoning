from AtomicSentence import *
from Biconditional import *
from Conjunction import *
from Disjunction import *
from Implication import *
from Negation import *


def to_cnf(KB):
	index = len(KB)
	cnf = []

	for clauses in KB:
		temp = []
		while (check_clean(temp))
		
	










def type_test(clause):
	if (clause.__class__.__name__ == "Literal"):
		return "Literal"

	elif (clause.__class__.__name__ == "Negation"):
		return "Literal"

	elif (clause.__class__.__name__ == "Conjunction"):
		return "Literal"

	elif (clause.__class__.__name__ == "Disjunction"):
		return "Literal"

	elif (clause.__class__.__name__ == "Implication"):
		return "Literal"

	elif (clause.__class__.__name__ == "Biconditional"):
		return "Literal"

	else:







# iterate throguh clause and check if its all disjunction or negative
# append all literals of the clause into an array + get rid of negative

# Negation: sentence_f only

def check_clean(clause):
	

	if (clause.__class__.__name__ == "Literal"):
		return True

	elif (clause.__class__.__name__ == "Negation"):
		return check_clean(clause.sentence_f)

	elif (clause.__class__.__name__ == "Disjunction")
		return check_clean(clause.sentence_f) and check_clean(clause.sentence_b)

	else:
		return False





def break_biconditional(clause):
	return Conjunction(Implication(clause.sentence_f, clause.sentence_b), Implication(clause.sentence_b, clause.sentence_f))

def break_implication(clause):
	return Disjunction(Negation(clause.sentence_f), clause.sentence_b)

# does not work for clause containing implication/biconditional
def break_negation(clause):

	child = clause.sentence_f

	if (child.__class__.__name__ == "Conjunction"):
		return Disjunction(Negation(child.sentence_f), Negation(child.sentence_b))

	elif (child.__class__.__name__ == "Disjunction"):
		return Conjunction(Negation(child.sentence_f), Negation(child.sentence_b))

	elif (child.__class__.__name__ == "Negation"):
		return child.sentence_f

	else:
		print(child.symbol) #will make error if its not literal (for debugging)
		if (child.value == True):
			child.value = False
		else:
			child.value = True

		return child


def break_conjunction(clause):
	return clause.sentence_f, clause.sentence_b

def break_disjunction(clause):
	if (clause.sentence_f.__class__.__name__ == "Conjunction" and clause.sentence_b.__class__.__name__ != "Conjunction"):
		return Conjunction(Disjunction(clause.sentence_f.sentence_f, clause.sentence_b), Disjunction(clause.sentence_f.sentence_b, clause.sentence_b))

	else: #(clause.sentence_b.__class__.__name__ == "Conjunction")
		return Conjunction(Disjunction(clause.sentence_f, clause.sentence_b.sentence_f), Disjunction(clause.sentence_f, clause.sentence_b.sentence_b))








if __name__ == "__main__":
	temp = [1,2,2,4,5]
	to_cnf(temp)





# cnf: array of clauses
# clause: array of literals
# literal: symbol +/-




# break biconditional
# break implication
# move negation inward
# negate
# distribute Or over And
