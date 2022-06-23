from math import *

#from https://www.youtube.com/watch?v=rfscVS0vtbw&t=1951s
#47 min

def count(x):
    my_num = -4

    print(-2.0987)

    print(3 + 4.5)
    print(3*4.5+9)
    print(10 % 3) # "10 mod 3", gets remainde
    print(str(my_num)+ ", my favourite number") # make number to string

    print(abs(my_num))
    print(pow(3,10)) # "to the power of"
    print(max(4,6)) # print largest number (min)
    print(round(3.7))

    print(floor(3.7))
    print(ceil(3.7))

def read(a):

    phrase = "Giraffe Academy"

    if a>0:
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

#count(5)

# Finished at 38.40

read(0)


