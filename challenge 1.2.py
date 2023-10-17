# 1.2 write a program that determines whether a year entered by user is a leap year or not using ifelif-else statements



def isleapyear(year):
  if(year % 4 == 0 and year %100 !=0) or year %400 == 0:
    return True
  else:
    return False

year = int(input("Enter the year : "))

if isleapyear(year):
  print('{} is a leap year.'.format(year))
else:
  print('{} is not a leap year.'.format(year))