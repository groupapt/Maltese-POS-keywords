Maltese-POS-keywords
====================

This is a Python module that makes use of the [Maltese Part-of-Speech tagger](http://metanet4u.research.um.edu.mt/POS.jsp) 
so as to extract keywords from PDFs on the Civil Cases website. However, anyone may and is able to reuse it within their 
projects, given that the license is respected and dependencies are available.

## Prerequisites

SOAPpy is required, since it is used to access the tagger's [web service](http://metanet4u.research.um.edu.mt/services/MtPOS?wsdl).

## Limitations

Due to our reliance on the POS tagger web service, the generate_keywords() function may not always return the correct 
result. The web service may not interpret a piece of text correctly if it does not form a valid sentence.

However, the POS tagger could improve and we are ready to help its reachable team in any way possible.

## Implementation

The module consists of a single function which sends a request to the service to send back the result of the 
`` tagParagraphReturn() `` method which is then parsed accordingly and a list of common nouns is created. At this stage, 
tags on the back of each are examined and removed, whilst only the words having the `` _NN `` token are retained.

The function, then checks the occurance of every word, while storing it in a dictionary. Finally, a list containing the 5 
most frequent keywords is returned.

Placeholder for list comprehension note!!!

## Usage

### generate_keywords()

#### Parameters

* text: String to be examined

#### Return value

list of the 5 most frequantly used common nouns

### Example call

``` python
from keyword import generate_keywords

# some optional code here

keywords = generate_keywords('Il-kelb tkebeb hdejn saqajn sidu.')

# some more optional code here
```
