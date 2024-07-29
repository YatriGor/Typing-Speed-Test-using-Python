# using time module
from time import *
import random as rd

def mistake(para, input):
    error = 0
    for i in range(len(para)):
        try:
            if para[i] != input[i]:
                error+=1
        except:
            error+=1
    return error

def timeSpeed(iTime, fTime, input):
    tTime = fTime-iTime
    tTime = round(tTime, 2)
    speed = len(input) / tTime
    return round(speed)

while True:
    chk = input("Ready to take test? (yes/no) : ")

    if chk == 'yes':
        test = ["Once upon a time in a small, bustling town, there was a quaint little bakery known for its delicious pastries and warm, inviting atmosphere.", "Every morning, the sweet aroma of freshly baked bread and pastries would waft through the air, drawing in customers from all corners of the town."," The bakery, owned by a kind and elderly couple, was a cherished spot where locals gathered to enjoy a cup of coffee and share stories."," Despite the fast pace of modern life, this little bakery remained a beloved cornerstone of the community, offering a slice of comfort and tradition in every bite."]

        #firstly we'll be importing a paragraph, dividing it into list, and then by using random module, we w'll randomly display one line from the paragraph.

        test1 = rd.choice(test)

        print("---------Typing Speed Test---------")
        print(test1)
        print()
        print()
        initial_time = time()

        testinput = input("Type Here : ")
        final_time = time()

        print("There are ", mistake(test1, testinput), " no. of mistakes in your input.")
        print("Your Typing Speed is = ", timeSpeed(initial_time, final_time, testinput), "wps")

    elif chk == 'no':
        print("No worries :) You're welcome to continue anytime!")
        break;

    else:
        print("Invalid choice!")
