'''
File for Bob
'''

'''
def hey(sentence):
	import re
	sentence=sentence.rstrip()

	if sentence == "":
		return "Fine. Be that way!"
	elif sentence == sentence.upper() and re.search("[A-Z]", sentence):
		return "Whoa, chill out!"
	elif sentence.endswith("?"):
		return "Sure."
	else:
		return "Whatever."
'''
def hey(sentence):
    #Yell check (all caps)
    if(sentence.isupper()):
        return "Whoa, chill out!"
    #Question check (ends in question mark?)
    elif(sentence.endswith('?')):
        return "Sure."
    #Null check (Is nothing said?)
    elif(sentence.strip() == ''):
        return "Fine. Be that way!"
    else:
        return "Whatever."