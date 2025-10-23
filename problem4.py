import os
os.system("clear")

fuzz = []
size = int(input("Enter array size: "))
for i in range(1,size+1):    
    if i % 3 == 0 and i % 5 == 0:
        fuzz.append("FizzBuzz")
    elif i % 3 == 0:
        fuzz.append("Fizz")
    elif i % 5 == 0:
        fuzz.append("Buzz")
    else:
        fuzz.append(i)
print(fuzz)