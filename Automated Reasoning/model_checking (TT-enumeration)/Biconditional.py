class Biconditional:

	def __init__(self, sentence_f, sentence_b):
		self.sentence_f = sentence_f
		self.sentence_b = sentence_b
		self.value = (not sentence_f.value or sentence_b.value) and (not sentence_b.value or sentence_f.value)



