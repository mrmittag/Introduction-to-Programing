Project 1 (guess the number) 
===
This code comes from the great book Invent with python by Al Sweigart. [The book can be read here](http://inventwithpython.com)
```python 
#This code is from an example from the book Invent with Python by Al Sweigart http://inventwithpython.com/chapter4.html

import random

guessesTaken=0
print("Hello! What is your name?")
myName=input()
number=random.randint(1,20)
print("Well, " + myName + ". I am thinking of a number between 1 and 20.")

while guessesTaken < 6 :
    print("Take a guess")
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    
    if guess < number:
        print("Your guesss is too low")
    if guess > number:
        print("Your guess is too high")
        
    if guess == number:
        break
    
if guess == number:
    guessesTaken = str(guessesTaken)
    print("Goob job, " + myName + "!. You guessed my number in " + guessesTaken)
    
if guess!= number:
    number = str(number)
    print("Nope. The number I was thinking of was " + number)
	
```

###Assignment:
* Copy this code on your cloud 9 server.
* Modify it, customize it, make it your own.
* Create a pull request to have your code included into this repository.