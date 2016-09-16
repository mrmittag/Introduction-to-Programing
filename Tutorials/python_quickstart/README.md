Python QuickStart: Interactive shell.
====

###Open terminal

* Type python
* You should see something similar to this:

Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.

\>>>  <----  type stuff when you see this thingy

###Basic Math

\>>> 8+8       

16

\>>> 8-4
        
4

\>>> 2*8       

16

\>>> 4/2        

2

\>>> 2**3      

8

###Variables/Strings
\>>> apples="bananas"

\>>> apples

'bananas'

\>>> x ='red'

\>>> y ='rum'

\>>> x+y

'redrum'

###Slicing/Indexing

\>>> x[0]

'r'

\>>> x[1]

'e'

\>>> x[2]

'd'

Each number represents an index or address for each letter in the string. It starts with 0

\>>> x[0:2]

're'

A slice tells the computer to print all of the letters from the start(0) to the end (2)

\>>> x[0:3]

'red'

\>>> x[::-1]

'der'

x[start : end : steps]

###print() input()


\>>> print("HelloWorld")

HelloWorld

\>>> print(x)

red

You can also print a slice:

\>>> print(x[0:2])

re

\>>> x= input("What do you want x to be?")

What do you want x to be? 'happy'

\>>> x

'happy'









