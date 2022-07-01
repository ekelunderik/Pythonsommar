from math import *

# from https://www.youtube.com/watch?v=rfscVS0vtbw&t=1951s, Finished at 3:57:51

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

def input1():
    name = input("enter your name please:")
    age = input("enter your age please:")
    print("Hello " + str(name) + "! You are " + str(age) + ".")

def input2():
    num1 = input("Enter a number, please: ")
    num2 = input("What do you want to add it by? ")
    result = float(num1) + float(num2)
    print("Great, you wanted to add " + num1 + " to " + num2 + ".")
    print("That is " + str(result))

def mad_libs():

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

def tuple_fun():

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

def max_num(num1, num2, num3):

    #comparisons with if statements, which input is largest? Possible with str as well
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

def calculator():

    #calculator that can add, subtract, multiply and divide two numbers.
    print("Hej och välkommen till Erkans miniräknare. Den kan plus, minus, multiplikation och division av två tal. ")
    num1 = float(input("Skriv in det första talet."))
    num2 = float(input("Skriv in det andra talet. "))
    operator = input("Vilken typ av operation vill du göra?")

    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    else:
        return "Ojdå! Det blev något fel, försök igen!"

def dictionaries():
    #monthconversion, key - value, kan användas med siffror också

    month_conversions = {
        "Jan": "January",
        "Feb": "February",
        "Mar": "March",
        "Apr": "April",
        "May": "May",
        "Jun": "June",
        "Jul": "July",
        "Aug": "August",
        "Sept": "September",
        "Okt": "Oktober",
        "Nov": "November",
        "Dec": "December",
    }
    print(month_conversions["Nov"])
    print(month_conversions.get("Deg", "Not a valid key. ")) #Efter komma är det "fallback" svar

def while_loops():

    i = 1
    while i <= 10: #looping condition/looping guard
        while i <= 9:
            print(i, "inte än!")
            i += 1
        print(i, "men nu!")
        i += 1
        print("Loopen är färdig!")

def guessing_game():

    secret_word = "giraffe"
    guess = ""
    guess_max = 5

    while guess != secret_word and guess_max > 1:
        guess = input("Enter guess: ")
        if guess != secret_word:
            guess_max -= 1
            print("Wrong. Try again! You have " + str(guess_max) + " guesses left." )
            if guess_max == 3:
                print("Hint: It's an animal which lives in Africa.")
            elif guess_max == 2:
                print("Hint: It is really tall!")

    if guess == secret_word:
        print("Nice, you win!")
    else:
        print("Sadly, you ran out of guesses. You lose!")

def for_loops():

    for letter in "Giraffe Academy":
        print(letter)

    friends = ["Jim", "James", "Jones"]
    print(len(friends))
    for name in friends:
        print (name)


    for index in range(10):
        print(index)

def exponent_function():

    print(2**3)
    num1 = int(input("Berätta vilket tal du vill upphöja. "))
    num2 = int(input("Hur mycket vill du upphöja det till? "))
    result = 1

    for index in range(num2):
        result = result*num1

    print(result)

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

def num_play():
    num_grid = [

        [1,2,3],
        [2,3,4],
        [3,4,5],
        [0]
    ]

    #print(num_grid[0][0])
    for row in num_grid:
        for col in row:
            print(col)

def translate(phrase):
    #"Giraffe Language"
    #vowels -> g

    translation = ""

    for letter in phrase:
        if letter.lower() in "aeiouåäö":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter

    return translation

def try_except_block():

# Catching errors in python
# skydda programmet genom att bygga in failsafes



    try:
        number = int(input("Enter a number: "))
        print(number)
    except ValueError:
        print("Invalid input")
    except ZeroDivisionError as err: # spara fel som variabel så kan man printa det direkt
        print(err)

def reader():

    employee_file = open("pyt.txt", "r") # modes: r = read, r+ = read and write, w = write, a = append
    print(employee_file.readable())
    for employee in employee_file.readlines():
            print(employee)
    # print(employee_file.readline())
    # print(employee_file.readlines()[1])

    employee_file.close()

def writer():

    # employee_file = open("pyt.txt", "a") # add text to the end of the file
    employee_file = open("pyt.txt", "w") # "w" overridear allt i gamla filen

    employee_file.write("Toby - Human Resources") #"\n" ger ny linje, "escape character"
    employee_file.write("\nKelly - Customer Service")
    employee_file.close()

def mods_pips():

    # moduler är bara gamla program som kan importeras
    import useful_tools
    print(useful_tools.roll_dice(10))
    # list of python modules, bara att importera fritt därifrån,
    # python docs


class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    Student1 = Student("Louise", "Marketing", "4.3", False)
    Student2 = Student("Erik", "Accounting", "4.02", False)



