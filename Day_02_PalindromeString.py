String= input("Enter a String: ")

String= String.lower()

Reverse_String= String[::-1]

if String == Reverse_String:
    print("The String is a Palindrome.")
else:
    print("The String is NOT a Palindrome.")