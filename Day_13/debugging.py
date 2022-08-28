############# Debugging #############

#Problem
number = int(input("Which number do you want to check?"))

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

#Problem

def check_leap_year(year):
    return((year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0)))
year = int(input("Enter year: "))
is_leap_year = check_leap_year(year)
if is_leap_year:
    print(f"{year} is Leap Year")
else:
    print(f"{year} is not Leap Year")

#Problem

def fizz_buzz(num):
  for i in range(1,num+1):
    if (i % 3 == 0) and (i % 5 == 0):
      print("FizzBUzz")
    elif i % 5 == 0:
      print("Buzz")
    elif i % 3 ==0:
      print("Fizz")
    else:
      print(i)

print("Welcome to FizzBuzz game")
num = int(input("Enter number: "))
fizz_buzz(num)