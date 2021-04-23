def askForInt():
    while True:
        try:
            result = int(input("Please provide a year: "))
        except:
            print("Hey, that is not a number!!")
            continue
        else:
            break
    return result

year = askForInt()
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{} is a leap year".format(year))
       else:
           print("{} is not a leap year".format(year))
   else:
       print("{} is a leap year".format(year))
else:
   print("{} is not a leap year".format(year))
