"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Domanais, Jerald M.
Date: 09/27/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Conditions allow a program to make decisions. The program checks whether something is true or false and then decides what code to run.

For example, a program can check someone's age and decide whether they are old enough to do something. Python uses if, elif, and else to handle these different situations.


============================================
KEY VOCABULARY
============================================
-condition: A question or rule that a program checks to see if it is true or false.
-if / elif / else: Statements used to make decisions. if checks the first condition, elif checks another condition if the first one is false, and else runs when none of the conditions are true.
-comparison operator: A symbol used to compare values, such as >, <, ==, !=, >=, or <=.
-boolean expression: An expression that results in either True or False.
-==: Checks if two values are equal.
-!=: Checks if two values are not equal.
->: Checks if the value on the left is greater than the value on the right.
-<: Checks if the value on the left is less than the value on the right.


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

score = 85

if score >= 90:
print("Excellent!")
elif score >= 75:
print("Passed!")
else:
print("Keep it up!.")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One mistake I want to avoid is using = when I want to compare two values. In Python, = is used to assign a value to a variable, while == is used to check if two values are equal.

For example:

score = 85 # assigns 85 to score
score == 85 # checks if score is 85


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
