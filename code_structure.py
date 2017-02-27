disaster = True
if disaster:
    print ( "Woe!" )
else:
    print ( "Whee!" )

# Eugene
Eugene = True
if Eugene:
    print ( "Kysliak!" )
else:
    print ( "KTOOO??" )

# cats
furry = True
small = True
if furry:
    if small:
        print ( "It's a cat." )
    else:
        print ( "It's a bear!" )
else:
    if small:
        print ( "It's a skink!" )
    else:
        print ( "It's a human. Or a hairless bear." )

# elif
color = "puce"
if color == "red":
    print ( "It's a tomato" )
elif color == "green":
    print ( "It's a green pepper" )
elif color == "bee purple":
    print ( "I don't know what it is, but only bees can see it" )
else:
    print ( "I've never heard of the color", color )

# цикл while
count = 1
while count <= 5:
    print ( count )
    count += 1

# break
# while True:
#     stuff = input("String to capitalize [type q to quit]: ")
#     if stuff == "q":
#             break
#     print(stuff.capitalize())


while True:
    value = input("Укажите целое нечетное число, пожалуйста [q для выхода]: ")
    if value == 'q': # выход
        break
    number = int(value)
    if number % 2 == 0: # нечетное число
        continue
    print (number, "в квадрате будет", number*number)