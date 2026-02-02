'''“Python supports all standard arithmetic operations.”

“These include addition, subtraction, multiplication, division, modulus, and exponentiation.”

“Every calculation in data analysis and machine learning depends on these operations.”

'''
a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)


''' Operator Precedence
“Python does not evaluate expressions left to right blindly.”
“It follows operator precedence rules, similar to BODMAS.”
“Misunderstanding this causes silent logical errors.”

'''

#examples
'''
result1 = 10 + 5 * 2
result2 = (10 + 5) * 2
print(result1)
print(result2)

'''

'''
result = 2 * 3 ** 2
print(result)  
'''
'''
# Objective: Find the average of 80 and 90
score1 = 80
score2 = 90

# Wrong way:
average = score1 + score2 / 2 
print(average) # Output: 125.0 (Wait, 125 is not the average!)

# Right way:
correct_average = (score1 + score2) / 2
print(correct_average) # Output: 85.0
Order,Operator,Description

# Does it square -5 (Result: 25) or is it the negative of 5-squared (Result: -25)?
result = -5 ** 2
print(result)  # Output: -25
To get 25, you must write (-5) ** 2.

1 (Highest),(),Parentheses (Always happens first)
2,**,Exponentiation (Power)
3,"+x, -x",Unary Plus/Minus (Negative numbers)
4,"*, /, //, %","Multiplication, Division, Floor, Modulo"
5 (Lowest),"+, -","Addition, Subtraction"
'''
final_score = 10 + 5 * 2 ** 2  #task for you 
