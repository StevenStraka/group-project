#Importing math library
import math
#I have to get the factorial of a user inputted number.
def factorial_function():
    main_number= int(input("Enter your a number to be factorized:"))
    #Utilizing the math library to factor my number in 1 line.
    final_factorial=math.factorial(main_number)
    #Printing the final result
    print(final_factorial)

factorial_function()    
#Calling the final factorial answer.