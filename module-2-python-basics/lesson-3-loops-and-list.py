"""
Module 2 — Lesson 3: Loops & Lists
Student: Domanais, Jerald M.
Date: 09/27/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]
Lists are used to store multiple values in one variable. For example, instead of creating a separate variable for every student's name, we can put all the names inside one list.

Loops are used when we want a program to repeat something. A for loop can go through each item in a list, while a while loop keeps repeating as long as a condition is true.

============================================
KEY VOCABULARY
============================================
-list: A collection that stores multiple values in one variable.
-for loop: A loop that repeats code for each item in a sequence, such as a list.
-while loop: A loop that keeps repeating while a condition is True.
-index: The position of an item in a list. Python starts counting indexes at 0.
-iteration: One repetition of a loop.
-item: A single value stored inside a list.


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

favorite_foods = ["pizza", "chicken", "pasta", "ice cream"]

for food in favorite_foods:
print("I like", food)


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One mistake I want to avoid is forgetting that Python starts list indexes at 0 instead of 1.

For example:

favorite_foods = ["pizza", "chicken", "pasta"]

The index of "pizza" is 0, "chicken" is 1, and "pasta" is 2.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
