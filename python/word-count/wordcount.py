def word_count(phrase):
	words = {}
	for word in phrase:
		if word in words:
			words[word] += 1
		else:
			words[word] = 1
	return words