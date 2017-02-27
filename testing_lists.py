weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(weekdays[4])

small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]
print(all_birds)
print(all_birds[0])
small_birds[1] = 'Pisya'
print(small_birds)
small_birds.append('Popa')
print(small_birds)

head = ['mouth', 'eyes']
body = ['legs', 'arms']
head.extend(body)
#head += body
head.insert(2, 'ears')
#del head[-1]
head.remove('legs')
print(head)

marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes)
print(sorted_marxes)

