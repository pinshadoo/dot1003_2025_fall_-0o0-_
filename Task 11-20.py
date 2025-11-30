print("Task 11")
temperature=int(input("Enter a temperature in Fahrenheit: "))
celsius=float((temperature-32)/1.8)
print(celsius)
if celsius <= 0 :
    print("Brrr! I should've bring my jacket here..")
elif celsius > 0 and celsius <= 35 :
    print("Ow lala! It feels good!")
elif celsius > 35 and celsius <= 60 :
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!!!!!!!!! WHAT THE FUCK İS THAT TEMPERATURE!!!")
elif celsius > 60 :
    print("...(no one is alive rn)")
print("")
print("Task 12")
hourly_wage=float(input("Enter your hourly wage: "))
hours_worked=int(input("Enter hours you're working: "))
day_of_the_week=input("Enter todays day: ")
daily_wage=(hourly_wage*hours_worked)
if day_of_the_week == "Sunday" :
    daily_wage = daily_wage*1.5
print("Your daily wage is: ", daily_wage)
print("")
print("Task 13")
age=int(input("Pls enter your age: "))
if age < 18:
    print("You're too small for Dark Souls! Go play something less scarier!")
if age >= 18 and age < 44:
    print("Here's your PEAK experience sir! Have a great time with that!")
if age >= 44 and age < 80:
    print("Nah, you're too old for this shit dude.")
if age >= 80:
    print("Are you still alive? Dude! You're such a cool dude for playing Dark Souls at this age!")
print("")
print("Task 14")
first_number=int(input("Enter your first number: "))
second_number=int(input("Enter your second number: "))
if first_number > second_number:
    print("Your first number is greater than your second one.")
if first_number < second_number:
    print("Your first number isn't greater than your second one.")
if first_number == second_number:
    print("Your first number is equal to your second one.")
print("")
print("Task 15")
first_word=input("Pls enter your first word: ")
second_word=input("Pls enter your second word: ")
if first_word > second_word:
    print( first_word + " is greater than " + second_word)
if first_word < second_word:
    print( second_word + " is greater than " + first_word)
if first_word == second_word:
    print("These words are same! You cheater :D")
print("")
print("Task 16")
community=input("Pls enter your comminuty belong to: ")
if community == "New California Republic" or community == "NCR" or community == "Brotherhood of Steel" or community == "Caesar's Legion" or community == "Great Khans" or community == "Vault Dweller":
    print("Welcome to your Fallout universe!")
if community != "New California Republic" or "NCR" or "Brotherhood of Steel" or "Caesar's Legion" or "Great Khans" or "Vault Dweller":
    print("Nah, you're not from here. Maybe you just lost your way?")
print("")
print("Task 17")
point=int(input("Pls enter your point from your exam: "))
if point < 0 :
    print("HOW CAN YOU EVEN GET A POİNT LİKE THAT!?!? THAT'S A ACHİEVEMENT ACTUALLY YOU KNOW!!!")
if point >= 0 and point <=49:
    print("You failed :( ")
if point >= 50 and point <= 59:
    print ("You'r grade is 1")
if point >= 60 and point <= 69:
    print ("You'r grade is 2")
if point >= 70 and point <= 79:
    print ("You'r grade is 3")
if point >= 80 and point <= 89:
    print ("You'r grade is 4")
if point >= 90 and point <= 100:
    print ("You'r grade is 5")
if point > 100:
    print("God dayum! I'm so interested about your paper right now actually")
print("")
print("Task 18")
number=int(input("Pls enter a number: "))
if number % 3 == 0 :
    print("Fizz")
if number % 5 == 0 :
    print("Buzz")
if number == 35 or number == 53:
    print("FizzBuzz")
if number % 3 != 0 and number % 5 != 0 and number != 35 and number != 53:
    print("You're not FizzBuzzed")
print("")
print("Task 19")
number1=int(input("Enter your number: "))
if number1 > 0:
      if number1 % 2 == 0:
        print("Your number is even")
      if number1 % 2 != 0:
        print("Your number is odd")
if number1 <= 0:
    print("Your number is negative or zero")
#Task 19'da 0 veya negatif bi sayı yazınca niye hala "Your number is odd" yazıyor çözemedim hocam.
print("")
print("Task 20")
year=int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Your year is a leap year.")
        else:
            print("Your year isn't a leap year.")
    else:
        print("Your year isn't a leap year.")
else:
    print("Your year isn't a leap year.")
print("")
print("Thx for checking my homework :) )")