#1

with open ("Test File.txt") as raw_text:
	text = raw_text.read()
	

def letter_count(text):
	letter_dictionary = {}
	text = text.upper()
	for letter in text:
		if letter in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"): #before had, if letter not in [".", "@", "$", "etc"]
			if letter not in letter_dictionary:
				letter_dictionary[letter] = 1
			else:
				letter_dictionary[letter] += 1
	return letter_dictionary

print letter_count(text)

#2
def remove_charactors(text):
	for charactors in [".", "!", ",", "?"]:
		if charactors in text:
			text = text.replace(charactors,"")
	return text

def word_count(string):
	wordcount={}
	for word in string.split(): #makes string into a list, ex. ["One", "Fish", "Blue", "Fish"]
	    if word not in wordcount:
	        wordcount[word] = 1
	    else:
	        wordcount[word] += 1
	return wordcount

with open ("Test File.txt") as text:
	text = text.read() #returns all text in a string, ex. "One Fish. Blue Fish"
	text = text.upper() #returns all text in CAPITAL LETTERS

text_no_charactors = remove_charactors(text)
print word_count(text_no_charactors)

	#OR

def remove_charactors(text):
	for charactors in [".", "!", ",", "?"]:
		if charactors in text:
			text = text.replace(charactors,"")
	return text

with open ("Test File.txt") as text:
	text = text.read() #returns all text in a string, ex. "One Fish. Blue Fish"
	text = text.upper() #returns all text in CAPITAL LETTERS

text_no_charactors = remove_charactors(text)

from collections import Counter
print Counter(text_no_charactors.split()) #Counter counts strings in a list, .split() converted the string into a list
