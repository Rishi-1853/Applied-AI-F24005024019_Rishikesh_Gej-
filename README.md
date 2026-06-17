# PYTHON TRAINING REPORT

# Day 01 – Python Fundamentals

A collection of beginner-level Python scripts covering core language fundamentals: variables and data types, and `for` loops applied to multiplication tables.

## 📁 Files in this Set

| File | Topic | Status |
| `Day_01_Datatype.py` | Variables & Data Types 
| `Day_01_Loop.py` | `for` Loops 
| `Day_01_5_Table.py` | 5 Times Table | ✅ Working |
| `Day_01_11_Table.py` | 11 Times Table | ✅ Working |

---

## 1. `Day_01_Datatype.py`

Demonstrates Python's built-in data types by assigning values of different types to variables and printing each one alongside its type using the `type()` function.

**Data types covered:**
- `int` — whole numbers
- `str` — text/strings
- `float` — decimal numbers
- `bool` — boolean (True/False)

  
## 2. `Day_01_Loop.py`

Reserved for `for` loop fundamentals (e.g., `range()`, iteration over sequences, `while` vs `for`). The file is currently empty and serves as a placeholder for upcoming loop exercises.


## 3. `Day_01_5_Table.py`

Prints the multiplication table of **5** from 1 to 10 using a `for` loop and `range()`.


## 4. `Day_01_11_Table.py`

Prints the multiplication table of **11** from 1 to 10 using the same loop pattern.


# Day 02 – Python Practice: Loops, Strings & User Input

A set of beginner-level Python scripts demonstrating `while` loops, string operations, conditional logic, and basic arithmetic — all driven by interactive user input.

## 📁 Files in this Set

| File | Topic | Status |
| `Day_02_PalindromeNumber.py` | Palindrome Check (Number) | ✅ Working |
| `Day_02_PalindromeString.py` | Palindrome Check (String) | ✅ Working |
| `Day_02_SimpleInterest.py` | Simple Interest Calculator | ✅ Working |
| `Day_02_StringLength.py` | String Length | ✅ Working |
| `Day_02_Swapping.py` | Swapping Two Numbers | ✅ Working |


## 1. `Day_02_PalindromeNumber.py`

Checks whether a number reads the same forwards and backwards by reversing its digits using a `while` loop and comparing the result to the original.


## 2. `Day_02_PalindromeString.py`

Checks whether a string is a palindrome by lowercasing it and comparing it to its reverse using Python's slice notation (`[::-1]`).



## 3. `Day_02_SimpleInterest.py`

Calculates Simple Interest given the principal amount, rate of interest, and time period, using the standard formula:



## 4. `Day_02_StringLength.py`

Takes a string from the user and prints its length using the built-in `len()` function.


## 5. `Day_02_Swapping.py`

Swaps the values of two user-input numbers using Python's tuple-unpacking assignment (`a, b = b, a`), avoiding the need for a temporary variable.



# Day 03 – Python Practice: Conditionals & Real-World Calculators

A set of beginner-to-intermediate Python scripts applying `if`/`elif`/`else` logic and arithmetic to practical, real-world scenarios — ATM withdrawals, billing systems, fee calculators, and academic result processing.

## 📁 Files in this Set

| File | Topic | Status |
| `Day_03_AtmWithdrawalCheck.py` | ATM Withdrawal Validation | ✅ Working |
| `Day_03_Average.py` | Average of Four Numbers |
| `Day_03_DaysToHours.py` | Days → Hours Converter | ✅ Working |
| `Day_03_DivisibleBy5and11.py` | Divisibility Check | ✅ Working |
| `Day_03_FeesCalculation.py` | Fees & Scholarship Discount | ✅ Working |
| `Day_03_HoursToMinutes.py` | Hours → Minutes Converter | ✅ Working |
| `Day_03_HouseRent.py` | House Rent Split Calculator |
| `Day_03_IncrementDecrement.py` | Increment / Decrement Operators | ✅ Working |
| `Day_03_Scholarship.py` | Scholarship Eligibility Checker | 
| `Day_03_ShoppingBillingGenerator.py` | Shopping Bill Generator | ✅ Working |
| `Day_03_StudentPercentage.py` | Student Percentage Calculator | ✅ Working |
| `Day_03_Total_marks_Percentage.py` | Total Marks & Percentage |

---

## 1. `Day_03_AtmWithdrawalCheck.py`

Validates an ATM withdrawal request by checking if the requested amount is less than or equal to the available balance.


## 2. `Day_03_Average.py`

Intended to calculate the average of four numbers entered by the user.


## 3. `Day_03_DaysToHours.py`

Converts a number of days into hours.


## 4. `Day_03_DivisibleBy5and11.py`

Checks whether a number is divisible by both 5 and 11 (i.e., divisible by 55) using the modulo operator and the `and` logical operator.



## 5. `Day_03_FeesCalculation.py`

Sums up tuition, hostel, food, and uniform fees, then applies a flat 15% scholarship discount to compute the final payable amount.



## 6. `Day_03_HoursToMinutes.py`

Converts a number of hours into minutes.


## 7. `Day_03_HouseRent.py`

Calculates the total household cost (rent + water + electricity) and splits it evenly among the number of people sharing the house.


## 8. `Day_03_IncrementDecrement.py`

Demonstrates the `+=` and `-=` compound assignment operators by incrementing then decrementing a user-entered number.



## 9. `Day_03_Scholarship.py`

Intended to check scholarship eligibility based on marks scored, using a chain of `if`/`elif`/`else` conditions.



## 10. `Day_03_ShoppingBillingGenerator.py`

The most advanced script in this set — a multi-item shopping bill generator. Collects item name, quantity, and price for `n` items, computes a formatted itemized bill, applies a 10% discount on bills over ₹5000, and prints a final total.

**Highlights:**
- Uses lists to store structured item records
- Formatted column output with f-strings and `.format()` width/precision specifiers
- Conditional bulk discount logic


## 11. `Day_03_StudentPercentage.py`

Takes marks for 5 subjects, computes the total and the percentage out of 500.
Percentage=  85.0 %


## 12. `Day_03_Total_marks_Percentage.py`

Appears to be an unfinished draft of a total-marks/percentage calculator. Currently contains a single, incomplete line.


# Day 04 – Python Practice: Nested Loops, Step Ranges & Conditionals

A set of beginner-level Python scripts exploring nested `for` loops, the step parameter of `range()`, odd-number filtering, and simple conditional password validation.

## 📁 Files in this Set

| File | Topic | Status |
| `Day_04_NumberPyramid.py` | Number Pyramid (Nested Loop) | 
| `Day_04_OnlyOdd1-10.py` | Odd Numbers 1 → 10 (step range) | ✅ Working |
| `Day_04_OnlyOdd10-1.py` | Odd Numbers 10 → 1 (reverse + modulo) | ✅ Working |
| `Day_04_RealOrFakePassword.py` | Password Validator | ✅ Working |

## 1. `Day_04_NumberPyramid.py`

Intended to print a number pyramid using a nested `for` loop, where each row prints an increasing count of numbers (e.g., `1`, `1 2`, `1 2 3`, ...).


## 2. `Day_04_OnlyOdd1-10.py`

Prints odd numbers from 1 to 10 in ascending order, using the step parameter of `range()` to jump by 2 starting from 1.


## 3. `Day_04_OnlyOdd10-1.py`

Prints odd numbers from 10 down to 1 in descending order, by iterating backward through every number and filtering with the modulo operator.


## 4. `Day_04_RealOrFakePassword.py`

A simple password validator that compares user input against a hardcoded password string.


