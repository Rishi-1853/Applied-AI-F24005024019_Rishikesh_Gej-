Num= int(input("Enter a Number: "))
Factorial= 1
if (Num < 0):
   print("Factorial is not defined for negative numbers.")
elif Num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,NUM + 1):
        Factorial *= 1
    print(f"Factorial of {Num} is {Factorial}")