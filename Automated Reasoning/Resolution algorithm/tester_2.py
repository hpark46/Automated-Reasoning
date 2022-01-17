import itertools

def powerset(KB):
	total = []
	# for i in range(0,len(KB)):
	total = total + list(itertools.combinations(KB, len(KB)))

	return total











if __name__ == "__main__":
	KB = []
	s1 = ("P1,1",1)
	s2 = ("P1,2",0)
	s3 = ("P2,1",1)
	s4 = ("P2,2",0)
	s5 = ("P3,1",1)
	s6 = ("B1,1",1)
	s7 = ("B2,1",0)


	KB.append(s1[0])
	KB.append(s5[0])
	KB.append(s2[0])
	KB.append(s3[0])
	KB.append(s6[0])
	KB.append(s7[0])
	KB.append(s4[0])

	# print(KB)
	# KB.sort()
	# print(pow(KB))
	temp = powerset(KB)
	print(temp)
	print(temp[0][0])
	print(temp[0])




