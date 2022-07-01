print("Hello World!")

# Write some code that can take two dates as input,
# and then calculate the amount of time between them.
# This will be a great way to familiarize yourself with Python’s datetime module.

from datetime import *

print("Det här programmet beräknar hur lång tid det är till ett specifikt datum i dagar, timmar, minuter och sekunder.")

def time_calc():
    print("\nIdag är det den " + str(datetime.now().strftime("%Y-%m-%d och klockan är: %H:%M:%S")) + ". ")
    date1 = input("\nVilket datum vill du beräkna tiden till? \nSkriv i formatet YY-MM-DD: ")

    try:
        date2 = datetime.strptime(date1, "%y-%m-%d") - datetime.today()
        date2 = str(date2).split(".")[0]
        return("\nTid kvar till ditt datum: " + str(date2) )
    except:
        print("\nTyvärr, det datumet är inte ett riktigt datum. Försök igen! ")
        time_calc()

print(time_calc())