# Exercise-22-Sept-2026
# 1. Store your weight (kg) in a variable `weight` and height (m) in a variable
# `height`. Calculate BMI using `bmi = weight / (height ** 2)` and print it.

weight = 70
height_cm = 160
height = height_cm/ 100
bmi = weight / (height ** 2) 
bmi = round(bmi,2)
# print(bmi)

#2. Using the BMI value from Q1, write if/elif/else logic to print:
#    - "Underweight" if bmi < 18.5
#    - "Normal weight" if 18.5 <= bmi < 25
#    - "Overweight" if 25 <= bmi < 30
#    - "Obese" if bmi >= 30

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal weight")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obese")        

# 3. A variable `speed` holds a car's speed in km/h. Write a program that prints:
#    - "Slow" if speed < 60
#    - "Normal" if 60 <= speed <= 120
#    - "Fast" if speed > 120

car_speed = 60
if car_speed < 60:
    print("Slow")
if car_speed <= 60:
    print("Normal")
if car_speed > 120:
    print("Fast")    
    
#4. Given a variable `year`, write an if/else statement to check whether it's
#a leap year (divisible by 4, but not by 100 unless also divisible by 400).
   
year = 365

       
# 5. A variable `password` holds a string. Write an if/elif/else chain that
#    prints:
#    - "Too short" if length is less than 8
#    - "Weak" if length is 8-11
#    - "Strong" if length is 12 or more      

password = "Linda12345"
if len(password) < 8:
    print("Too short")
elif len(password) < 11:
    print("Weak")
else:
    print("Strong")         
   
#6. Store three exam scores in variables `math`, `science`, and `english`.
#    Calculate the average and use if/elif/else to print "Pass" if average
#    >= 50, else "Fail".  

math = 90
science = 60
english = 50
exam_score = (math + science + english / 300) * 100
if exam_score <= 50:
    print("Fail")  
else: print("Pass")  



#7. A variable `time` holds an hour in 24-hour format (0-23). Write
#    if/elif/else logic to print "Morning", "Afternoon", "Evening", or
#    "Night" based on the hour.

time = -17

# Morning (6 AM to 11 AM)
# Afternoon (12 PM to 17 PM)
# Evening (18 PM to 20 PM)
# Night (21 PM to 5 AM)

if time >= 6.00 and time <= 11.00:
    print("Morning")
elif time >= 11.00 and time <= 17.00:
    print("Afternoon")
elif time >=17.00 and time <= 21.00:
    print("Evening")    
elif time >= 5.00 and time <= 21.00:
    print("Night") 
else:
    print("Time format is incorrect")

#8. What will this print, and why?

#        a = 7
#        b = a
#        a = a + 1
#        print(a, b) - final answer is 8, 7 or 8 7 

a = 7
b = a
a  = a + 1
print(a, b)


#9. A variable `stock_qty` holds the number of items in stock. Write an
#    if/elif/else to print "Restock urgently" if less than 10, "Restock soon"
#    if 10-49, else "Stock OK". 

stock_qty = 49.99999
print(stock_qty)
stock_qyt = round(stock_qty, 0)
print(stock_qty)

if stock_qty < 10:
    print(f"Restock urgently: Your stock quantity is {stock_qty}")
elif stock_qty >= 10 and stock_qty <= 49:
    print(f"Restock soon: Your stock quantity is {stock_qty}")
else:
    print(f"Stock OK: Your stock quantity is {stock_qty}")    
    
# 10. Given two variables `x` and `y`, write an if/elif/else that prints
#     whether x is greater than, less than, or equal to y.        

x =2
y =6

if x > y:
    print(f"x is greater than y:x={x} and y={y}")
elif x < y:
    print(f"x is less than y:x ={x} and y={y}")
else:
    print(f"x and y are equal:x={x} and y={y}")   
    
    
    
    
    
    
    















         