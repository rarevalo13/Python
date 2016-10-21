minor_words = ['of', 'the', 'a' ]
def title_case(title, minor_words):
	for words in title: 
		if words.split() == minor_words:
			words.lower()
		else:
			words.title()

print(title_case('a clash of KINGS', 'a an the of'))