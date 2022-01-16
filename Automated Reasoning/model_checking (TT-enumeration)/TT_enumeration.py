from AtomicSentence import *
from Biconditional import *
from Conjunction import *
from Disjunction import *
from Implication import *
from Negation import *



# returns if the query entails knowledge base

def tt_entails(KB, query):

	symbols = []
	for sentence in KB:
		symbol_generation(sentence, symbols)

	symbol_generation(query, symbols)


	return tt_check_all(KB, query, symbols, [])



def tt_check_all(KB, query, symbols, model):

	if (len(symbols) == 0):

		print_tt(model, KB)

		if(pl_true(KB)):

			if (query.value):
				return True

			else:
				return False



		else:
			return True






	else:

		symbols[0].value = True

		model.append(symbols[0])

		hold = tt_check_all(KB, query, symbols[1:], model)

		symbols[0].value = None
		model.pop(len(model)-1)



		symbols[0].value = False
		model.append(symbols[0])

		hold_two = tt_check_all(KB, query, symbols[1:], model)

		symbols[0].value = None
		model.pop(len(model)-1)

		return hold and hold_two



def pl_true(KB):
	flag = True
	for sentence in KB:
		flag = flag and sentence.value

	return flag






def symbol_generation(sentence, symbols):
	
	if (sentence.__class__.__name__ == "AtomicSentence"):
		if(check_exist(sentence, symbols)):
			symbols.append(sentence)


	else:
		symbol_generation(sentence.sentence_f, symbols)
		if (sentence.__class__.__name__ != "Negation"):
			symbol_generation(sentence.sentence_b, symbols)




def check_exist(atomic, symbols):

	for element in symbols:

		if (element.symbol == atomic.symbol):
			return False

	return True




def print_tt(model, KB):
	names = ""
	tf = ""
	for element in model:
		names = names + element.symbol + "   "
		tf = tf + str(element.value) + "   "

	index = 1
	for sentence in KB:
		names = names + " R" + str(index) + "    "
		tf = tf + str(sentence.value) + "  "
		index = index + 1

	names = names + "KB "
	tf = tf + str(pl_true(KB))


	print(names)
	print(tf)







if __name__ == "__main__":
	KB = []
	s1 = AtomicSentence("P1,1")
	s2 = AtomicSentence("P1,2")
	s3 = AtomicSentence("P2,1")
	s4 = AtomicSentence("P2,2")
	s5 = AtomicSentence("P3,1")
	s6 = AtomicSentence("B1,1")
	s7 = AtomicSentence("B2,1")


	KB.append(Negation(s1))												#r1
	KB.append(Biconditional(s6, Disjunction(s2, s3)))					#r2
	KB.append(Biconditional(s7, Disjunction(s1, Disjunction(s4, s5))))	#r3
	KB.append(Negation(s6))												#r4
	KB.append(s7)														#r5


	print(tt_entails(KB, s2))







# in every model where KB is true, query is true : entails
								    # else:  	   cannot conclude