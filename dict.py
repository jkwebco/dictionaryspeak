from PyDictionary import PyDictionary
dictionary=PyDictionary()

import pyttsx


engine = pyttsx.init()
engine.setProperty('rate', 150)
	
variable = ""
while variable != 'quit':
	variable = raw_input('Lookup a word, type something in: ')
	meaning = (dictionary.meaning(variable))
	synonym = (dictionary.synonym(variable)) 
	antonym = (dictionary.antonym(variable))
	translate = (dictionary.translate(variable,'es'))
	google = (dictionary.googlemeaning(variable))


	print ("meaning :",meaning)
	print('\n')
	print ("synonym :",synonym)
	print('\n')
	print ("antonym :", antonym)
	print('\n')
	print("translated to spanish :",translate)
	print('\n')
	print("google meaning: ", google)
	engine.say('google meaning is ')
	engine.say(google)
	engine.runAndWait()
