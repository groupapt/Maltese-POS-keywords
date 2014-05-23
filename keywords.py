__author = 'Daniel'

from collections import defaultdict
from SOAPpy import SOAPProxy
from operator import itemgetter

'''
' Diagnoses a piece of text and gives back the 5 most common keywords
' @param text Text to process
' @return List of 5 Word objects representing the most common keywords
'''


def generate_keywords(text):
	server = SOAPProxy('http://metanet4u.research.um.edu.mt/services/MtPOS?wsdl')
	words = [w[:w.rfind('_')] for w in server.tagParagraphReturn(text).split(' ') if w[len(w)-2:] == 'NN']

	word_dict = defaultdict(int)
	for word in words:
		word_dict[word] += 1

	return [x[0] for x in (sorted(word_dict.iteritems(), key=itemgetter(1), reverse=True)[:5])]