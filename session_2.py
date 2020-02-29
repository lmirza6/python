#Ask for the user's name, if they are called "Bob", print "Welcome Bob!"
name = input("Whats your name?")
if name == "Bob":
    print("Welcome Bob!")

#Ask for the user's name, if they are not called "Alice", print "Youre not Alice"
name = input("Whats your name?")
if name != "Alice":
    print("Youre not Alice")

#Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". If they get it wrong, print "Password failure"
password = "qwerty123"
users_input = input("What is your password")
if password == users_input: 
    print("You have successfully logged in")
else:
    print("Password failure")

#Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd"
number = int(input("What is your number?\n"))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "safe".

number_1 = int(input("Input a number:\n"))
number_2 = int(input("Input another number:\n"))

if number_1 + number_2 > 21:
    print("Bust.")
else:
    print("Safe.")

#Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob", print "What's up Bob!", else print "You must be Charlie"
name = input("Whats your name?")
if name == "Bob":
    print("What's up Bob!")
elif name == "Alice":
    print("Hello, Alice")
else: 
        print("You must be Charlie")

#Ask the user to enter their age: if they are younger than 11 print "Youre too young to go to this school". ii. If they are between 11 and 16, print "You can come to this school". iii. If they are over 16, print "Youre too old for school". iiii they are 0, print, "Youre not born yet!".
age = int(input("How old are you?\n"))

if age < 11:
    print("You're too young to go to this school")
elif age >= 11 and age <= 16:
    print("You can come to this school")
elif age > 16:
    print("You're too old for school")
elif age == 0:
    print("You're not born yet")
else:
    print("You didn't pick a number")

#Ask the user to enter the name of a month. If the user enters March/April/May" print "<month> is in spring", otherwise print "I dont know". i. Expand for the rest of the year, given that Summer is June/July/August. Autumn is September/October/November. Winter is December/Janaury/February. ii.Ensure that when an unknown month is given it prints "I dont know"
month = input("What month is it?")
if month == "March" or month == "April" or month == "May":
    print(month + " is in Spring ")
elif month == "July" or month == "June" or month == "August":
    print(month + " is in Summer ")
elif month == "December" or month == "January" or month == "February":
    print(month + " is in Winter ")
elif month == "September" or month == "Otcober" or month == "November":
    print(month + " is in Autumn ")
else: 
    print("I dont know")

#Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers.
number_1 = int(input("Input a number:\n"))
number_2 = int(input("Input another number:\n"))

if number_1 % 2 == 0 and number_2 % 2 == 0:
    print("Even")
elif number_1 % 2 == 1 and number_2 % 2 == 1:
    print("Odd")
else:
    print(number_1 * number_2)

#Create the following list of items: apples, cherries, pears, pineapples, peaches, mango.
fruit = ["apples", "cherries" , "pears" , "pinapples" , "peaches" , "mango"]
print(fruit)

#Add "Grapes" to the list
fruit.append("grapes")
print(fruit)
fruit[3] = "strawberries"
print(fruit)
del(fruit[0])
print(fruit)
print(len(fruit))
fruit.sort()
print(fruit)

#Loop through the list you created in Section C and print each item out.
fruits = ["apples", "cherries" , "pears" , "pinapples" , "peaches" , "mango"]

for fruit in fruits:
    print(fruit)


#Loop through the list you created in section C and print each item out.  
for number in range(101):
    print(number)

 #Print all the odd numbers from 1 to 100   
for number in range(1, 100, 2):
    print(number)


#The modern olympics started in 1896, print all the years they have been held.
for number in range(1896, 2020, 4):
    print(number)






