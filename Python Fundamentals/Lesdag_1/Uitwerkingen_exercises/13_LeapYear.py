year = int(input("Put in a year: "))

# a year is a leapyear if the year can be divided by 4
# but (and) the year can not be divided by 100
# except (or) if the year can be divided by 400


if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print(year,"is a leap year")
       else:
           print(year, "is not a leap year")
   else:
       print(year, "is a leap year")
else:
   print(year, "is not a leap year")



