Num= int(input("Enter a Number: "))

Original_Num= Num
Reverse_Num= 0

while Num > 0:
    Digit= Num % 10
    Reverse_Num= Reverse_Num * 10 + Digit
    Num= Num // 10

if Original_Num == Reverse_Num:
    print(Original_Num, "is a Palindrome Number")
else:
    print(Original_Num, "is NOT a Palindrome Number")