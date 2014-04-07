__author = 'Daniel'

'''
' Class to help deal with word frequancy
' @property image String representing word
' @property occurance Number of times word is found
'''
class Word:

	'''
	' Constructor
	' @param image Word string value
	'''
	def __init__(self, image):
		self.image = image
		self.occurance = 1

	'''
	' Increments the occurance of a word by 1
	'''
	def inc_occurance(self):
		self.occurance += 1

	'''
	' @param other Other object
	'''
	def __lt__(self, other):
		return self.occurance < other.occurance

	'''
	' @param other Other object
	'''
	def __gt__(self, other):
		return self.occurance > other.occurance

	'''
	' @param other Other object
	'''
	def __eq__(self, other):
		return self.image == other.image

'''
' Looks for a given word in a list
' @param words_captured List holding words to search through
' @param needle Word string literal to search for
' @return Word object if word found or False otherwise
'''
def word_found(words_captured, needle):
	for word in words_captured:
		if needle in word.image:
			return word
	return False

'''
' Strips away any of the given occurances found in a given string
' @param list List of strings to be striped
' @param text String to process
' @return String with all occurances stripped away
'''
def strip_matches(list, text):
	for x in list:
		text = text.replace(x, '')
	return text

'''
' Split a string into a list of words
' @param text String to split
' @return List of strings representing words
'''
def get_words(text):
	text = text.replace('\n', ' ')
	return text.split(' ')

'''
' Diagnoses a piece of text and gives back the 5 most common keywords
' @param text Text to process
' @return List of 5 Word objects representing the most common keywords
'''
def generate_keywords(text):
	punctuation = ['.', ',', '?', ':', ';', '!', '"', '\'', '(', ')']
	simple_words = ['huwa', 'hija', 'bin', 'imma', 'u', 'ghal', 'illi', 'dan', 'dina', 'sobordinament', 'preliminarjament', 'li', 'il-']
	
	text = strip_matches(punctuation, text)
	text = strip_matches(simple_words, text)

	words = get_words(text)

	words_captured = []
	for word in words:
		word_captured = word_found(words_captured, word)
		if not word_captured:
			words_captured.append(Word(word))
		else:
			word_captured.inc_occurance()

	top_five_words = []
	for x in range(5):
		most_common = max(words_captured)
		top_five_words.append(most_common)
		words_captured.remove(most_common)

	return top_five_words