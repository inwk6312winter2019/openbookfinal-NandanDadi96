from string import punctuation
fil1 = open("Book1.txt","r")
fil2 = open("Book2.txt","r")
fil3 = open("Book3.txt","r")
fil1.readline()
fil2.readline()
fil3.readline()

def sort_items(x, y):
	return cmp(x[1], y[1]) or cmp(y[0], x[0])
	N = 10
	words = {}
	words_gen = (word.strip(punctuation).lower()
	for line in open("Book1.txt","Book2.txt","Book3.txt") 
		for word in line.split()
			for word in words_gen:
				words[word] = words.get(word, 0) + 1
				top_words = sorted(words.iteritems(), cmp=sort_items, reverse=True)[:N]
					for word, frequency in top_words:
	print "%s: %d" % (word, frequency)
