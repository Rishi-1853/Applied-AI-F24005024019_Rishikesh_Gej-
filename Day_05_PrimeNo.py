#Finding the Prime Number.
Num= int(input("Enter a Number: "))
Check= 0
if(Num == 1 or Num <= 0):
    print("Enter Correct Value.")
    exit()
for i in range(Num-1,1,-1):
    if Num%i == 0:
        Check= 1
        break
if Check == 0:
    print("The Number is Prime.")
else:
    print("The Number is NOT Prime.")  
