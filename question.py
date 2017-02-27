name = input("Укажите, пожалуйста, Ваше имя: ")
while True:
    value = input('{}, укажи, пожалуйста, целое нечетное число [или нажми q для выхода]: '.format(name))
    if value == 'q': # выход
        break
    number = int(value)
    if number % 2 == 0: # нечетное число
        print(number, "НЕ является нечетным числом!")
        continue
    print(number, "в квадрате будет", number*number)