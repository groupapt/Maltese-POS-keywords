__author = 'Daniel'

import re

#added dictionary as per Jurgen's advice
word_dict = {
	'a': [],
	'b': [],
	'c': [],
	'd': [],
	'e': [],
	'f': [],
	'g': [],
	'h': [],
	'i': [],
	'j': [],
	'k': [],
	'l': [],
	'm': [],
	'n': [],
	'o': [],
	'p': [],
	'q': [],
	'r': [],
	's': [],
	't': [],
	'u': [],
	'v': [],
	'w': [],
	'x': [],
	'y': [],
	'z': [],
	'other': []
}

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
def word_found(needle):
	for word in word_dict[dict_key(needle)]:
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
' Remove words starting with a digit from a list of word strings
' @param list List of word strings
' @return Resulting list
'''
def strip_digit_words(list):
	for word in list:
		if word != '' and re.match('[1-9]', word[0]):
			list.remove(word)
	return list

'''
' Returns a key depending on the first character of the word passed
' @param word String representing a word
' @return Key representing the position of the word in word_dict
'''
def dict_key(word):
	if re.match('[a-z, A-Z]', word):
		return word[0].lower()
	else:
		return 'other'

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

	words = strip_digit_words(get_words(text))

	for word in words:
		word_captured = word_found(word)
		if not word_captured:
			word_dict[dict_key(word)].append(Word(word))
		else:
			word_captured.inc_occurance()

	top_five_words = []
	for x in range(5):
		max_occurance = 0
		most_common = None
		for list in word_dict:
			if word_dict[list]:
				most_common_current = max(word_dict[list])
				if most_common_current.occurance > max_occurance:
					max_occurance = most_common_current.occurance
					most_common = most_common_current
		top_five_words.append(most_common)
		word_dict[dict_key(most_common.image)].remove(most_common)

	return top_five_words