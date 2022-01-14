class Biconditional:

	def __init__(self, sentence_f, sentence_b):
		self.sentence_f = sentence_f
		self.sentence_b = sentence_b
		self.value = (not sentence_f or sentence_b) and (not sentence_b or sentence_f)



