letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[20:])
print(letters[10:])
print(letters[12:15])
print(letters[4:20:3])
print(letters[-1::-1])
print(len(letters))

todos = 'get gloves,get mask,give cat vitamins,call ambulance'
print(todos.split(','))

crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print('Found and signing book deals:', crypto_string)

poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''
print(poem[:13])
print(len(poem))
print(poem.startswith('All'))
print(poem.endswith('That\'s all, folks!'))

word = 'the'
print(poem.find(word))
print(poem.rfind(word))
print(poem.count(word))
print(poem.isalnum())

setup = 'a duck goes into a bar...'
print(setup.strip('.'))
print(setup.capitalize())
print(setup.upper())
print(setup.center(30))
print(setup.replace('duck', 'marmoset'))
print(setup.replace('a ', 'a famous ', 100))
print(setup.replace('a', 'a famous', 100))

#DZ
seconds_per_hour = 60*60
print(seconds_per_hour)
seconds_per_day = seconds_per_hour*24
print(seconds_per_day)
my_var = seconds_per_day / seconds_per_hour
print(my_var)
my_var2 = seconds_per_day // seconds_per_hour
print(my_var2)