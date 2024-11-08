# Question 1: Arithmetic and Assignment Operators

x = 100
x += 3

y = 50
y *= 2

result = x/y

result = result

print("Result =", result)



# Question 2: Comparison and Logical Operators

a = 100

b = 50

c = 25

if a > b:
    print("A is greater than B")

if b % b:
    print("B is even")

if c <= a:
    print("C is less than or equal to A")

print("Final_condition =", a > b or b % b or c <= a)



# Question 3: Conditional Statements
print("Hey user type in your test_score!")

test_score = int(input("Score: "))
score = test_score

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")



# Question 4: Combining Operators and Conditionals

print("Hey user type in two numbers.")

num1 = int(input("First number: "))
first_number = num1

num2 = int(input("Second number: "))
second_number = num2

print("Great now type in any of these operations (+, -, *, /)")

operation = (input("Operator: "))
operator = operation

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
if num2 == 0 and operation == "/":
        print("Division by zero is not allowed")
else:
    result = num1 / num2
if num2 !=0:
            print("result: ", result)
















