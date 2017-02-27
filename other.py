bierce = {
    "day": "A period of twenty-four hours, mostly misspent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses",
}
drinks = {
    'martini': {'vodka', 'vermouth'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'black russian': {'vodka', 'kahlua'},
    'screwdriver': {'orange juice', 'vodka'}
}

marxes = ['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
stooges = ['Moe', 'Curly', 'Larry']

tuple_of_lists = marxes, pythons, stooges
list_of_lists = [marxes, pythons, stooges]
dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges': stooges}

years_list = [1986, 1987, 1988, 1989, 1990, 1991]
print ( years_list[3] )
print ( years_list[5] )
print ( '\n' )

things = ['mozzarella', 'cinderella', 'salmonella']
print ( things[1].capitalize ( ) )
print ( things[0].upper ( ) )
del things[-1]
print ( 'things' )
print ( '\n' )

suprize = ['Groucho', 'Chico', 'Harpo']
print ( suprize[-1].lower ( ) )
print ( suprize[-1].capitalize ( ) )
print ( '\n' )

e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse'
}
print ( e2f )
print ( e2f.get ( 'walrus' ) )
print ( '\n' )

f2e = {}
for english, french in e2f.items ( ):
    f2e[french] = english
print ( f2e )

# Igor
# english2france ={
#     'one': 'un',
#     'two': 'deux',
#     'three': 'troi'
# }
# france2english = {}
# for eng, fra in english2france.items():
#     france2english[fra] = eng
# Igor

print ( f2e.get ( 'chien' ) )
print ( set ( f2e.keys ( ) ) )

life = {
    'animals': {
        'cats': [
            'Henri', 'Grumpy', 'Lucy'
        ],
        'octopi': {},
        'emus': {}
    },
    'plants': {},
    'other': {}
}

print ( list ( life.keys ( ) ) )
print ( life['animals'].keys ( ) )
print ( life['animals']['cats'] )
