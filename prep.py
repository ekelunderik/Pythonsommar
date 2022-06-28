from math import *

# from https://www.youtube.com/watch?v=rfscVS0vtbw&t=1951s, Finished at 1:54:08

def count(x):
    my_num = -4

    if x > 0:
        print(-2.0987)

        print(3 + 4.5)
        print(3 * 4.5 + 9)
        print(10 % 3)  # "10 mod 3", gets remainde
        print(str(my_num) + ", my favourite number")  # make number to string

        print(abs(my_num))
        print(pow(3, 10))  # "to the power of"
        print(max(4, 6))  # print largest number (min)
        print(round(3.7))

        print(floor(3.7))
        print(ceil(3.7))
    else:
        print(2.0987)

def read(a):
    phrase = "Giraffe Academy"

    if a > 0:
        print("Hello World")
        print("giraffe/academy")
        print()

        phrase = "Giraffe Academy"
        print(phrase + " is cool")
        print(phrase.upper())
        print(phrase.upper().isupper())  # gör det till upper och svarar på om det är upper
        print(len(phrase))

        print(phrase[1])

        print(phrase.index("Academy"))  # var det startar
        print(phrase.replace("Giraffe", "Elephant"))  # byter ut saker i strings

        print(len("phrase"))
    else:
        print(phrase.index("G"))
        print(phrase.replace("Giraffe", "Lion"))

def input1(k):
    name = input("enter your name please:")
    age = input("enter your age please:")
    print("Hello " + str(name) + "! You are " + str(age) + ".")

def input2(k):
    num1 = input("Enter a number, please: ")
    num2 = input("What do you want to add it by? ")
    result = float(num1) + float(num2)
    print("Great, you wanted to add " + num1 + " to " + num2 + ".")
    print("That is " + str(result))

def MadLibs():

    color = input("What is your favoorite color? ")
    plural = input("What is you favorite thing? ")
    celebrity = input("Who is your celebrity crush? ")

    print("Roses are " + str(color))
    print(str(plural) + " is blue")
    print("I love " + str(celebrity))

def lists():
    #Lists, structure for values. Check documentation standards for Py


    friends = ["Hannes", "Noak", "Malcolm"]
    print(friends[1]) #fungerar som siffror, räknar från 0. Negativa tal räknar bakifrån, -1 är sista.
    print("Min bästa vän är " + friends[0])
    friends[1] = "Louise" #justera vilka som är med i listan
    print(friends[1:]) #kolon tar alla efter talet, 1:5 tar alla mellan ett och fem.

    friends[1] = "Louise"

def list_functions():

    #data container, mutable!

    lucky_numbers = [4, 8, 15, 16, 23, 42]
    friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

    friends.sort() #som default i bokstavsordning, kan ej printas direkt eftersom funktionen returnerar "none"
    print(friends)

    friends.extend(lucky_numbers) #lägger till i slutet av listan
    friends.append("Creed") #alltid i slutet av listan
    friends.insert(1, "Kelly") #skickar in i mitten av listan
    friends.remove("Oscar") #tar bort Jim

    lucky_numbers.sort()
    lucky_numbers.reverse()
    print(lucky_numbers)

    #friends.pop() #tar bort ett element i listan
    #friends.clear()

    print(friends.index("Karen"))
    print(friends.count("Jim"))

    friends2 = friends.copy()
    print(friends2)

def tuple():

    #data container, similar to lists. IMMUTABLE! Uses standard brackets ()
    #used for data thats never going to be change. Possible to create lists of tuples, or tuples of lists

    coordinates = (4, 5)
    print(coordinates[0])

def function_hi(name, age): #funktioner och return statements
    print("Hello " + name +  ". You are " + str(age) + ".")
    return age*age*age #bryter ut direkt ur funktionen, går inte vidare

def if_statement(x, y):

    if x == "man" or x == "lång": #kan också använda "and" som används när båda måste vara sanna
        is_male = True
    else:
        is_male = False

    if x == "man" and y == "lång":
        print("Schyst king!")
        return 10


    print("Är du en man? " + str(is_male) + "!")

    if is_male:
        print("Cool! Du är antingen en man eller så är du lång eller båda! KING!")
    else:
        print("Wack! Antingen kvinna eller kortis :(")

def if_statement2():

    is_male = True
    is_tall = False

    if is_male and is_tall:
        print("You are a tall male")
    elif is_male and not is_tall:
        print("You are a short male")
    elif not is_male and is_tall:
        print("You are not a male but you are tall")
    else:
        print("You are not a male, nor are you tall")







#

def prime_checker(k): #Hittar alla primtal under talet k

    for i in range (2, k):
        if k % i == 0:
            return False
    return True

def prime_keeper(m):

    j = int(input("Hej Louise, det här är ett program som hittar primtal. Hur många vill du hitta? :)"))
    prime_list = []

    for i in range(2, m):
        if prime_checker(i) is True:
            if len(prime_list) < j:
                prime_list.append(i)

    print ("Snyggt, här är en lista med " + str(len(prime_list)) + " st primtal.")
    return prime_list


#print(prime_keeper(1000))
