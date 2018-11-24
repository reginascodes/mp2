import random

def gettemplate(file):
	'''gets file and outputs a list of templates'''
	templates = open(file, 'r').readlines()
	return templates

def getfills(file):
	'''gets file and outputs a list of what to fill in the blanks'''
	fills = open(file, 'r').readlines()
	return fills

fills = getfills('fill.txt') #list ng lahat ng fills
randomfill = random.choice(fills) #outputs string ng isang fill
position = fills.index(randomfill) #index ng fill (para makuha yung sa same index galing sa template)
rfill = randomfill.split(',') #outputs list ng mga noun,adjective, etc. to be displayed na

templates = gettemplate('templates.txt') #list ng lahat ng templates
temp_to_use = templates[position] #outputs a string ng mga templates
maintemp = temp_to_use.split('_') #outputs a list ng mga parts ng template (template _ template)

inputs = []
for word in rfill:
	if 'entered' in word: #minsan nagapainput ng something na nainput na before, pangit tignan pag naka-"input a/an"
		print('Input' + word + ':')
	else:
		print('Input a/an ' + word + ':')
	inputs.append(input()) #Gawa tayo ng error statement pag walang ininput? 
	print('Inputs:', str(inputs))

print('Story:')
maximum = len(maintemp)

for i in range(maximum):
	print(maintemp[i], end='')
	try:
		print(inputs[i], end='')
	except IndexError:
		pass


