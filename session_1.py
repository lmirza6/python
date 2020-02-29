# Create two variables, one that holds the width and one that holds the height of a rectange, then, work out and store the area in a third variable.
width = 28
height = 4
area = width * height
print ("Rectangle of " + str(width) + " and height " + str(height) + " has an area of " + str(area))

# Write code that prints the length of the string, 'python'
print(len('python'))

# Print out the first and third letter of the word 'python'
word = "python"
print(word[0])
print (word[2])

# Ask the user to enter their name, and print out "Hello, <name>"
name = input("Whats your name? ")
print("Hello " + name)

#Ask the user to enter their age, tell them holw old they will be in 15 years time
age = int(input("How old are you? "))
age_10 = age + 10
print("In 15 years you will be " + str(age_10))

#Combine the two input statements above and print out the message "Hello, , you are currently years old. In 15 years you will be
name = input("Whats your name? ") 
age = int(input("How old are you? "))
age_15 = age + 15
print("Hello " + name +" you are currently " + str(age) + " years old. In 15 years you will be " + str(age_15)+".")

#Ask the user to enter their hometown, print it out in uppercase letters.
hometown = input(" Whats your hometown? ")
print(hometown.upper())




