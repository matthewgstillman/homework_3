#Homework 2 (7 points)
#1. Computers process data under the control of sets of instructions called computer _________.
# - programs
#2. Python can incorporate new ______, which can be written by any Python developer.
#3. Which Python statement instructs the computer to display information on the screen?
# - the print statement, which needs to be followed by two parenthesis. Example: print("This is an example")
#4. Which Python statement loads pre-defined functions, classes or variables to be used in your
#program?
#True or False
#1. An algorithm is a description of process in a step-by-step manner. It is best implemented in a high
#level language such as Python
# True
#2. Computers represent all data types such as pictures, text, numbers using a series of 1s and 0s.
# True
#Short questions:
#1. Is Python a compiled or interpreted language? Please explain
# - Python is an interpreted language because an interpreted language is any programming language that isn't already in the machine code prior to run time. Pyton is 'byte-code interpreted', and all python files ending in .py will be interpreted into a .pyc file with the same name
#2. What are the 3 types of languages? Please give an example of each.
# - 1.) Machine Languages - Only Understood by computers - Incomprehensible to humans
# - 2.) Assembly Languages - English-like abbreviations that represent elementary operations of the computer - More clear to human readers. Examples: Java, Objective-C
# - 3.) High-Level Languages - Single statements accomplish substantial tasks, which will in turn be translated to machine language. Examples: C, C++

#Short Programs

#Write a program that asks the user to enter 2 numbers. The program will take the first number,
#multiply by the second number and output the product.
first_number = input("type in a number")
print("First Number is: " + str(first_number))
second_number = input("type in a second number")
print("Second Number is: " + str(second_number))
number_product = int(first_number) * int(second_number)
print("Number Product: " + str(number_product))

#Write a program that asks the user to enter 3 numbers. The program will add them all together and
output the sum
sum = 0
first_num = input("Type in a number")
print("First Number: " + str(first_num))
sum += int(first_num)
print("Sum = " + str(sum))
second_num = input("Type in a second number")
print("Second Number: " + str(second_num))
sum += int(second_num)
print("Sum = " + str(sum))
third_num = input("Type in a third number")
print("Third Number: " + str(third_num))
sum += int(third_num)
print("Sum = " + str(sum))

