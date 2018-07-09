# put your code here.

def count_words(file):
	"""Count word occurrences."""

	word_count = {}

	with open(file) as test_file:
		for line in test_file:
			line = line.rstrip()
			words = line.split()
			for word in words:
				word_count[word] = word_count.get(word, 0) + 1
				print(word, ": ", word_count[word])
		return word_count
		

count_words("test.txt")




