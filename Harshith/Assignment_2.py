"""
Author: Harshith MohanKumar
Date: 26/01/2020
ChatBot Assignment 2
"""

import nltk
from nltk.corpus import treebank
from textblob import TextBlob

def nltk_parse(s):
	tokens=nltk.word_tokenize(s)
	print(tokens)
	tagged=nltk.pos_tag(tokens)
	print(tagged[0:6])
	entities=nltk.chunk.ne_chunk(tagged)
	print(entities)
	t=treebank.parsed_sents('wsj_0001.mrg')[0]
	t.draw()

def textblog_parse(s):
	blob=TextBlob(s)
	print(blob.tags)
	print(blob.noun_phrases)

	for sentence in blob.sentences:
		print(sentence)
		print(sentence.sentiment.polarity)

	print(blob.translate(to='es'))

if __name__ =='__main__':
	sentence = input("Enter a sentence to parse: ")
	print()
	nltk_parse(sentence)
	textblog_parse(sentence)
