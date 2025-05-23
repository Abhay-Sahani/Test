Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import random
>>> number = random.randint(1, 100)
>>> guess = None
>>> attempts = 0
>>> while guess != number:
...     guess = int(input("Guess the number between 1 and 100: "))
...     attempts += 1
...     if guess < number:
...         print("Higher!")
...     elif guess > number:
...         print("Lower!")
... 
...         
Guess the number between 1 and 100: 5
Higher!
Guess the number between 1 and 100: 16
Higher!
Guess the number between 1 and 100: 80
Lower!
Guess the number between 1 and 100: 50
Higher!
Guess the number between 1 and 100: 
Traceback (most recent call last):
  File "<pyshell#11>", line 2, in <module>
    guess = int(input("Guess the number between 1 and 100: "))
ValueError: invalid literal for int() with base 10: ''
>>> print(f"Correct! You guessed the number in {attempts} attempts.")
Correct! You guessed the number in 4 attempts.
>>> import random
... number = random.randint(1, 100)
... guess = None
... attempts = 0
... while guess != number:
...     guess = int(input("Guess the number between 1 and 100: "))
...     attempts += 1
...     if guess < number:
...         print("Higher!")
...     elif guess > number:
...         print("Lower!")
... 
SyntaxError: multiple statements found while compiling a single statement
>>> import random
... number = random.randint(1, 100)
... guess = None
... attempts = 0
... while guess != number:
...     guess = int(input("Guess the number between 1 and 100: "))
...     attempts += 1
...     if guess < number:
...         print("Higher!")
...     elif guess > number:
