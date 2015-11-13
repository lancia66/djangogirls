print ('ahoj')
if 5<2:
	print('ahoj')
elif 'nazdar' == 'piatok':
	print('servus')
else:
	print('koniec')
volume = 30
if volume < 20:
	print ('It is kinda quiet')
elif 20 <= volume < 40:
	print ('It is nice for background music')
else:
	print('mam rada hudbu')


def hi():
	print('hi there')
	print('How are you')
hi()

def hi2(name,surname): 
    print ('hi '+name+' '+surname) 
hi2('Lucia','Stefanakova')    
hi2('Ondrej','Sika')


boys = [ 'Marek', 'Ondrej', 'Juraj']
for name in boys:
	hi2(name, '') 
for i in range(3):
	print ('pekny den')
	