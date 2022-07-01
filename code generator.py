# print("Hello world")

# Create a code generator. This can that take text as input,
# replaces each letter with another letter, and outputs the “encoded” message.

def code_control():

    prompt = input("Hej. Det här är ett program som förändrar textsnuttar. "
                   "\nSkriv en mening. ")

    choice = input("Vill du översätta till \n (a) kod, \n (b) rövarspråket?"
                   "\n Svara med a eller b. ")

    if "a" in choice:
        code_gen(prompt)
    else:
        rovar_gen(prompt)

def code_gen(prompt):

    result = ""
    for letter in prompt:
        if letter.lower() in "aeiouåäö":
            if letter.lower() == letter:
                result = result + "g"
            else:
                result = result + "G"
        else:
            result = result + letter

    result_handle(result, prompt)

def rovar_gen(prompt):

    result = ""
    for letter in prompt:
        if letter.lower() not in "aeiouåäö":
            if letter.lower() == letter:
                result = result + letter + "o" + letter
            else:
                result = result + letter.upper() + "o" + letter
        else:
            result = result + letter

    result_handle(result, prompt)

def result_handle(result, prompt):

    print("\nNu är det översatt. Det nya, omgjorda, meningen är: "
           "\n"
           "\n" + result)

    saver = input("\nVill du spara det kodade meddelandet och ursrungsmeddelandet? ")

    if "ja" in saver.lower():
        kodfil = open("kod.txt", "w")
        kodfil.write(str(prompt) + "\n" + str(result))
        kodfil.close()
        print("\nNu är det sparat, filen ligger i mappen MyFolder.")
    else:
        print("\nOkej. Tack för att du ville leka med mig!")

code_control()