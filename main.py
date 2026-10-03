# Exercise - 22 September 2026


# ============================================================
# QUESTION 1: Calculate BMI
# ============================================================

# Store weight in kilograms.
weight = 70

# Store height in centimetres.
height_cm = 160

# Convert height from centimetres to metres.
height = height_cm / 100

# Calculate BMI using the formula:
# BMI = weight / (height squared)
bmi = weight / (height ** 2)

# Round the BMI to 2 decimal places.
bmi = round(bmi, 2)

# Print the BMI.
print(f"BMI: {bmi}")


# ============================================================
# QUESTION 2: BMI Category
# ============================================================

# Check the BMI and determine the appropriate category.
if bmi < 18.5:
    print("Underweight")

elif 18.5 <= bmi < 25:
    print("Normal weight")

elif 25 <= bmi < 30:
    print("Overweight")

else:
    print("Obese")


# ============================================================
# QUESTION 3: Car Speed
# ============================================================

# Store the car's speed in kilometres per hour.
car_speed = 60

# Check the speed and print the appropriate category.
if car_speed < 60:
    print("Slow")

elif 60 <= car_speed <= 120:
    print("Normal")

else:
    print("Fast")


# ============================================================
# QUESTION 4: Leap Year
# ============================================================

# Store the year that we want to check.
year = 2024

# A year is a leap year if:
# 1. It is divisible by 4 AND not divisible by 100
# OR
# 2. It is divisible by 400.
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap year")

else:
    print("Not a leap year")


# ============================================================
# QUESTION 5: Password Strength
# ============================================================

# Store the password.
password = "Linda12345"

# Check the length of the password.
if len(password) < 8:
    print("Too short")

elif len(password) < 12:
    print("Weak")

else:
    print("Strong")


# ============================================================
# QUESTION 6: Exam Average
# ============================================================

# Store the three exam scores.
math = 90
science = 60
english = 50

# Calculate the average of the three subjects.
exam_score = (math + science + english) / 3

# Print the average.
print(f"Exam average: {exam_score}")

# Check whether the average is at least 50.
if exam_score >= 50:
    print("Pass")

else:
    print("Fail")


# ============================================================
# QUESTION 7: Time of Day
# ============================================================

# Store the time using the 24-hour format.
# Example: 8 = 8 AM, 14 = 2 PM, 19 = 7 PM.
time = 14

# Morning: 06:00 - 11:59
if 6 <= time < 12:
    print("Morning")

# Afternoon: 12:00 - 17:59
elif 12 <= time < 18:
    print("Afternoon")

# Evening: 18:00 - 20:59
elif 18 <= time < 21:
    print("Evening")

# Night: 21:00 - 05:59
elif 21 <= time <= 23 or 0 <= time < 6:
    print("Night")

# Check whether the time is outside the valid 0-23 range.
else:
    print("Time format is incorrect")


# ============================================================
# QUESTION 8: Variable Assignment
# ============================================================

# Assign 7 to variable a.
a = 7

# Assign the current value of a (7) to b.
b = a

# Increase the value of a by 1.
# a becomes 8, but b remains 7.
a = a + 1

# Print both values.
print(a, b)

# Output:
# 8 7
#
# This happens because b received a copy of the value of a
# when a was 7. Changing a afterwards does not change b.


# ============================================================
# QUESTION 9: Stock Quantity
# ============================================================

# Store the number of items currently in stock.
stock_qty = 49

# Check the stock quantity and print the appropriate message.
if stock_qty < 10:
    print(f"Restock urgently: Your stock quantity is {stock_qty}")

elif 10 <= stock_qty <= 49:
    print(f"Restock soon: Your stock quantity is {stock_qty}")

else:
    print(f"Stock OK: Your stock quantity is {stock_qty}")


# ============================================================
# QUESTION 10: Compare Two Numbers
# ============================================================

# Store two numbers.
x = 2
y = 6

# Compare x and y.
if x > y:
    print(f"x is greater than y: x = {x}, y = {y}")

elif x < y:
    print(f"x is less than y: x = {x}, y = {y}")

else:
    print(f"x and y are equal: x = {x}, y = {y}")

