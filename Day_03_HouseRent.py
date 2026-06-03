House_Rent= float(input("Enter the House Rent: "))
Water_Cost= float(input("Enter the Water Cost: "))
Electricity_Cost= float(input("Enter the Number of People in the House: "))
People_In_House= int(input("Enter the Number of People in the House: "))
Total_Cost= House_Rent + Water_Cost + Electricity_Cost
Cost_Per_Person= Total_Cost / People_In_House

print("The Total Cost of the House Rent is: ", Total_Cost)
print("The Cost Per Person is: ", Cost_Per_Person)