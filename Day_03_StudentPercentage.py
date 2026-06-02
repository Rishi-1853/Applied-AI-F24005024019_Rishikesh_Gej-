print("Student Marks Calculator")

Sub1= float(input("Enter Marks of Subject 1: "))
Sub2= float(input("Enter Marks of Subject 2: "))
Sub3= float(input("Enter Marks of Subject 3: "))
Sub4= float(input("Enter Marks of Subject 4: "))
Sub5= float(input("Enter Marks of Subject 5: "))

Total= Sub1 + Sub2 + Sub3 + Sub4 + Sub5

Percentage= (Total/500)*100

print("\n----- Result -----")
print("Total Marks= ", Total)
print("Percentage= ", Percentage, "%")
