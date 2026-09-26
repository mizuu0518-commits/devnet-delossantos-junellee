"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Delos Santos, Junelle 
Date: 09/26/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Control flow allows a program to make decisions based on
different conditions. The program checks a condition and
decides what code to run.


============================================
KEY VOCABULARY
============================================
- condition: statement that the program checks to see if it is true or false.
- if / elif / else: statements used to make decisions in a program.
- comparison operator: symbol used to compare values, such as ==, >, <, >=, or <=.
- boolean expression: expression that results in either True or False.



============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""
score = int(input("Enter Score: "))
if(score == 10):
  print("Perfect Score!")
elif(score == 5):
  print("Average Score!")
else:
  print("Failed")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
I want to avoid using braces since I'm used to using them instead of the colon.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
This connects to programs I have made before because many
programs need to make decisions based on what the user enters.
For example, the movie program we did earlier where I used if elif else conditions for the choice of the user.
"""
