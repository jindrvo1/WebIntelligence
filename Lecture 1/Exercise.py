from random import shuffle

def near_duplicates(str1, str2, threshold = 0.9, n_shingle = 3):
	words1 = str1.split()
	words2 = str2.split()

	shingle1 = []
	shingle2 = []

	for i in range(len(words1) - n_shingle + 1):
		shingle1.append(tuple(words1[i:i+n_shingle]))

	for i in range(len(words2) - n_shingle + 1):
		shingle2.append(tuple(words2[i:i+n_shingle]))

	union = len(set(shingle1 + shingle2))
	overlap = len(shingle1 + shingle2) - union

	return overlap/union > threshold

	#hashed1 = [hash(shingle) for shingle in shingle1]
	#hashed2 = [hash(shingle) for shingle in shingle2]
	
	#n_iterations = 10000

	#sketch1 = []
	#sketch2 = []
	#for i in range(n_iterations):
	#	shuffle(hashed1)
	#	shuffle(hashed2)

	#	sketch1.append(hashed1[0])
	#	sketch2.append(hashed2[0])

	#match = 0
	#for i in range(n_iterations):
	#	if sketch1[i] == sketch2[i]:
	#		match += 1

	#return match/n_iterations

text1 = "do not worry about your difficulties in mathematics"
text2 = "i would not worry about your difficulties you can easily learn what is needed"

print(near_duplicates(text1, text2))

text3 = "do not worry about your difficulties in mathematics you can easily learn what is needed blah blah whatever some words to make this text longer much much longer because either i screwed up or the jaccard similarity is really strict"
text4 = "do not worry about your difficulties in physics you can easily learn what is needed blah blah whatever some words to make this text longer much much longer because either i screwed up or the jaccard similarity is really strict"

print(near_duplicates(text3, text4, threshold = 0.8))