Module 2 — Lesson 4: Function
Student: Domanais, Jerald M.
Date: 09/27/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
A function is a reusable block of code that performs a specific task. Instead of writing the same code again and again, we can put it inside a function and use the function whenever we need it.

We create a function using the def keyword. A function can also receive information called parameters and can return a result.

For example, if I need to calculate the total price several times, I can create a function that does the calculation for me.
============================================
KEY VOCABULARY
============================================
-unction: A reusable block of code that performs a specific task.
-def: A Python keyword used to create a function.
-parameter: A variable inside a function that receives information.
-argument: The actual value that we give to a function when we call it.
-return: Sends a result back from a function.
-function call: Using a function to make it run.


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

def calculate_total(price, quantity):
return price * quantity

total = calculate_total(50, 3)

print("Total price:", total)

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One mistake I want to avoid is forgetting to call the function after creating it.

Creating a function does not automatically run it. I need to call the function using its name.

For example:

def say_hello():
print("Hello!")

say_hello()

The first part creates the function, while say_hello() actually runs it.
============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""