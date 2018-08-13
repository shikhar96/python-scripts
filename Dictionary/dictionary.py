#Importing essential libraries
import json
from difflib import get_close_matches

#Importing data from json file
data = json.load(open('data.json'))

#Code for translate function
def translate(w):
	w = w.lower()
	if w in data:
		return data[w]
	elif len(get_close_matches(w, data.keys())) > 0:
		ans = input("Did you mean %s instead? Enter Y for Yes and N for No: " % get_close_matches(w, data.keys())[0])
		if ans == 'Y':
			return data[get_close_matches(w, data.keys())[0]]
		elif ans == 'N':
			return "The word does not exist."
		else:
			return "Entry not understood."
	else:
		return "The word does not exist."

#Taking user input
word = input("Enter word: ")

#Displaying output
output = translate(word)
if type(output) == list:
	for item in output:
		print(item)
else:
	print(output)