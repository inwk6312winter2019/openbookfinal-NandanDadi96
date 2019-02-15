fil1 = open("Book1.txt","r")
fil2 = open("Book2.txt","r")
fil3 = open("Book3.txt","r")
fil1.readline()
fil2.readline()
fil3.readline()

n=0
def unique_words():
	for line in fil1:
		line=line.strip()
		if not line in fil1:
			fil1.append()
		return fil1
	for line in fil2:
                line=line.strip()
                if not line in fil2:
                        fil2.append()
                return fil2
	for line in fil3:
                line=line.strip()
                if not line in fil3:
                        fil3.append()
                return fil3
print unique_words(['it','s','it']);

def count_the_article():

def sorted_words(word):
	word1=list(word)
	if word1==sorted(word1):
		return True
	else:
		pass
	for line in fil1:
		line=line.strip()
		if sorted_words(line)==True:
			n=n+1
		else:
			pass
	print(n)
	word2=list(word)
        if word2==sorted(word2):
                return True
        else:
                pass
        for line in fil2:
                line=line.strip()
                if sorted_words(line)==True:
                        n=n+1
                else:
                        pass
        print(n)
	word3=list(word)
        if word3==sorted(word3):
                return True
        else:
                pass
        for line in fil3:
                line=line.strip()
                if sorted_words(line)==True:
                        n=n+1
                else:
                        pass
        print(n)

def character_word_count():
	d = {}
	for word in fil1:
		if word not in d:
			d[word] = 0
		d[word] += 1
	word_count = []
	for key,value in d.items():
		word_count.append((value,key))
	word_count.sort(reverse = True)
	for word in fil2:
                if word not in d:
                        d[word] = 0
                d[word] += 1
        word_count = []
        for key,value in d.items():
                word_count.append((value,key))
        word_count.sort(reverse = True)
	for word in fil3:
                if word not in d:
                        d[word] = 0
                d[word] += 1
        word_count = []
        for key,value in d.items():
                word_count.append((value,key))
        word_count.sort(reverse = True)
s = 0
def starts_with_vow(word,s):
	a=0
	for i in range(len(word)):
		while word[i] in s:
			a=0
		else:
			a=a+1
	if a==0:
		return True
	else:
		pass
	s=str(input("enter the letters:"))
	for line in fil:
		line=line.strip()
		if starts_with_vow(line,s)==True:
			b=b+1
		else:
			pass
	print(b)
