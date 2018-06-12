# WTP CS Problem Set 2

To get started, click the green "Clone or download" button and copy the link given. Then, in a terminal, navigate to the location you want to put your new pset folder and type:
```
$ git clone {your-link-here}
```
 
### 1. print vs return - `print_vs_return.py`

Open the template file `print_vs_return.py`. In it, these two functions are defined: 

```python
def f1(x):
    print x + 1

def f2(x):
    return x + 1
```

Run this code. We will now go through some examples using these functions. Answer all the bolded questions by commenting in `print_vs_return.py`.

**What happens when we call the functions below? (Try getting the answer on your own and use IDLE only to check your answer).**

Example 1:
```
>>> f1(3)
?
>>> f2(3)
?
```

From example 1, it looks like they behave in exactly the same way, but they really don't.

Example 2: Try this:
```
>>> a = f1(3)
>>> b = f2(3)
>>> a
?
>>> b
?
```
**What are the values of a and b? Why are they different?**

Example 3: Now run the following code:
```
>>> print f1(3)
?
?
>>> print f2(3)
?
```
**What is the output? Why are you getting this output?**

Example 4:
```
>>> f1(3) + 1
? 
?
?
?
>>> f2(3) + 1
?
```
**What is the output? Why are you getting this output? What do all of these examples tell us about when we want to return and when we want to print? (When is printing useful? When is returning useful?)**

Note: You might find it useful to explicitly `return None` when you don't want your function to return anything. This way, you'll always remember that what Python is *actually* doing is returning `None` if you don't tell it to return anything.

### 2.  Adding comments 
At the beginning, your programs will be small and easy to understand. Over time, they’ll get bigger and more complicated. Instead of having to understand what every line of code does, you can add comments to your code that explain what you were trying to do. 
 
You can add a comment using the # sign: 

``` python
# Print a message to the screen 
print("hello, wtp!") 
```
Comments are ignored by the computer – you can write anything you want there. 
Best practice, and what we would like you to do in this class, is to write code that explains 
what your program does and what you want it to do. For example, if you were writing a game 
like rock-paper-scissors, but you didn’t know where to start, you could write this: 
```python
# First player picks one of rock, paper, or scissors 
# Second player picks one of rock, paper, or scissors 
# If first player beats second player, print a winning screen for her 
# If second player beats first player, print a winning screen for her 
```

### 3. Doing math - `calculator.py`
We can also use Python as a calculator. The basic operations are: 
 
> \+ Addition 
>
> \- Subtraction 
>
> \* Multiplication 
>
>\/ Division 
>
>\** Exponentiation 
 
Let’s use Python to solve the following problem: 
 
If you run a 5K race in 20 minutes 30 seconds, what is your **average time (minutes) per mile**? What is your **average speed in miles per hour**? *Hint: There are 1.61 kilometers in a mile.* In your program, store useful values in variables, and print your final answers!


For this part of the problem set, we want to add comments to the hello.py file that we just wrote. 
Now, *edit the program from the previous exercise and add a comment at the beginning of the file with 
the filename, your name, anyone you worked with (no one if it’s no one), and a sentence about what it does*. 
You should do that for all future programs. 

### 4. String operators - `stringop.py`
String operators are less intuitive than those on numbers. Given the following variables, what are the values of these expressions? (Try getting the answer on your own and use Sublime only to check your answer.)

```
# Variables
look = "Look at me!" 
now = " NOW"

# Expressions
look[:4] 
 
look[-1] 
 
look*2 
 
look[:-1] + now + look[-1]
 
now[1]
 
now[4]
 
look*2 + look[:-1] + now + look[-1] 
```

### 5. Greetings - `greetings.py`
Print  a  greeting  saying  **“Hello,  Michelle"** and  **“Goodbye,  Obama"**  using  only  the  variables  provided  in `greetings.py`.  Complete instructions are in the file.
 
### 6. Optional Challenge:
Revisit Question 1, and write a program that prints **“Hello \<name>!!!”** in a box of stars for ANY name.

*Hint: Find the length of a string with  len(a_string)*

### Submitting your PSET
After you’ve finished your PSET, type into the terminal:
```
$ git add -A
$ git commit -m "Submitting pset 1"
$ git push
```
You can do this as many times as you'd like to. You can also write whatever you'd like in the quotations (instead of just "Submitting pset 1"), but the instructors will be able to see it!
