# WTP CS Problem Set 3

To get started, click the green "Clone or download" button and copy the link given. Then, in a terminal, navigate to the location you want to put your new pset folder and type:
```
$ git clone {your-link-here}
```
 
### 1. Write a Mad Lib - `mad_lib.py`

Mad  Libs  are  word  games  where  one  player  fills  in  the  blanks  of  another  player’s  story  by  providing  words of  certain  types.  When  the  words  are  substituted  in  for  the  blanks,  the  result  is  a  complete,  grammatically correct  but  often  nonsensical  story.

In `madlib.py` we  are  going  to  write  a  program  that  lets  the  user  make  a  Mad  Lib!

(a)First,  you  will  need  a  Mad  Lib:  we  have  provided  a  (terrible!)  personal  ad  Mad  Lib  in  the  file `personal_ad.txt`,  but  feel  free  to  write  your  own  or  choose  one  from http://www.madglibs.com/

(b)Now,  as  we  did  for  Evil  Pierre  in  class,  some  words  need  to  be  replaced  with  variables.  In  this  case, replace  any  “blanks”  in  the  story  with  variables. 

(c)Now,  using  the `raw_input` command  we  learned  in  class,  prompt  the  user  for  words  to  fill  in  the blanks.  Ask the  user  for  at  least  4  inputs.

(d)Finally,  print  out  the  story  for  the  user!

### 2.  Mouse Input - `mousepoint.py`
In  this  exercise,  we’ll  experiment  with  a  different  type  of  user  input:  the  mouse  pointer.  You  can  find all  the  documentation  for  the  graphics  module  on  the  website http://tinyurl.com/graphics-py (or http://mcsp.wartburg.edu/zelle/python/graphics/graphics/graphics.html). 

The  code  in  `mousepoint.py`  shows  you  how  to  retrieve  the  coordinates  of  the  mouse  pointer  when  the  user  clicks. Run  the  program  and  make  sure  you  can  get  the  mouse  coordinates.  You  should  only  draw  the  window once,  but  you  should  get  new  mouse  coordinates  every  time  the  user  clicks  the  window. 

Draw  a  blue  rectangle  on  the  screen.  Modify  the  code  so  that  when  the  user  clicks  inside  the  rectangle, then  the  rectangle  changes  to  green,  and  when  the  user  clicks  outside  the  rectangle, it  becomes  red.

### 3. Guess My Number - `guessnum.py`
Write  a  Guess  My  Number!  game.  In  this  game,  your  program  will  choose  a  number,  and  the  user  tries to  guess  that  number.  Here  is  an  example  of  how  the  program  will  work:

```
Ready  to  guess?  My  number  is  between  0  and  30.
Enter  your  guess  now:
?  5
Too  low!
?  20
Too  high!
?  13
Too  low!
?  17
Correct!  You  win!
```

For  this  game,  we  will  need  to  generate  a  random  number  for  the  user  to  guess.  For  this,  we  need a  new  module,  the `random` module.  At  the  top  of  your  code,  add  the  line `import  random`.  We’ll use  this  module  to  generate  a  random  integer  using  the  function `randint`,  which  works  as  follows: `random.randint(lo, hi)`,  where `lo` and `hi` are  integers  that  tell  the  code  the  range  in  which  to  generate a  random  integer  (this  range  is  inclusive).  Let’s  use  0  to  30  for  now.

Write  a  function `guess_compare` that  asks  the  user  for  a  guess,  then  compares  that  guess  with  the  correct number  and  prints  out  “Too  low!”,  “Too  high!”,  or  “Correct!” 

Give  the  user  five  guesses.  If  the  user  has  not  yet  guessed  the  number,  print  out  the  correct  answer. *(Hint:  Your  function `guess_compare` will  need  to  return  whether  the  guess  was  correct.)*  Test  your  game.

**Optional:** If  the  user  gets `n` guesses,  what  is  the  largest  range  of  numbers  the  program  can  choose  from and  still  guarantee  that  the  user  can  win?  What  is  the  strategy  that  the  user  should  use?  You’ll  talk more  about  this  in  Discrete  Math  next  week!

### 4. Blackjack - `blackjack.py`
Blackjack  is  a  popular  game  (feel  free  to  read  up  more  on  the  game  on  Wikipedia:https://en.wikipedia.org/wiki/Blackjack).  The  goal  of  the  game  is  to  get  to  a  score  of  21  without  going  over. Below  is  a  fragment  of  code.  Given  the  inputs,  what  does  it  output?

Create a python file called `blackjack.py` and use comments to write your answer. Do  this *without* running  the  code.  (It  is  an  important  skill  to  be  able  to  understand  what  a  piece  of  code does  without  running  it.)

```python
total  =  card1  +  card2
if  total  ==  21:
    print  "blackjack!"
elif  total  >=  17:
    print  "stand"
elif  total  >=  12:
    if  dealer_card  >  6:
        print  "hit"
    else:
        print  "stand"
elif  total  >  9  or  (total  ==  9  and  dealer_card  <=  6):
    print  "double,  then  hit"
else:
    print "hit"
```

Fill in the following table with the appropriate outputs (the answers can be entered into `blackjack.py` using comments):
| card1 | card2 | dealer_card | output |
| ------|:-----:| -----------:|:------:|
| 3     | 8     | 4           |        |
| 9     | 8     | 10          |        |
| 11    | 10    | 10          |        |
| 3     | 5     | 4           |        |
| 5     | 8     | 8           |        |

### 5. Simple graphics - `simple_graphics.py`
Let’s  make  a  simple  graphics  program.  Open `simple_graphics.py` in  IDLE,  but  don’t  run  it  yet!  You  can find  all  the  documentation  for  the  graphics  module  on  the  website http://tinyurl.com/graphics-py (or http://mcsp.wartburg.edu/zelle/python/graphics/graphics/graphics.html).  We  explain  the code in `simple_graphics.py` below.

***

**from  graphics  import  *

This  tells  us  that  we’re  going  to  use  graphics.  Importing  graphics  gives  us  access  to  all  sorts  of  graphics commands  that  someone  else  has  made  for  us.

**win  =  GraphWin('My  Circle',  100,  100)**
We’re  creating  a  new  graphics  window,  called `win` of  type `GraphWin` (part  of  the  graphics  module).  We’re calling  it `My  Circle` and  telling  it  to  have  dimensions  of  100 x 100  pixels.

**c  =  Circle(Point(50,  50),  10)**
We’re  creating  a  circle  called `c` with  a  center  point  at  (50,50)  and  with  a  radius  of  10.  Note  that  the center  of  the  circle  is  a  (unnamed) `Point` with  coordinates  (x,  y)  =  (50,50).

**c.setFill('red')**
We’re  coloring  the  circle  red.  This  can  take  most  normal  colors.  See  the  documentation  under *Generating Colors* for  more  information.

**c.draw(win)
win.mainloop()**
Now  that  we’ve  decided  on  attributes  for  the  circle  (position,  size,  and  color),  we’re  actually  drawing  it on  the  screen.

***

Now  run  the  code.  A  window  with  your  image  will  pop  up!

Feel  free  to  try  playing  around  with  some  of  the  values  –  see  where  things  break,  and  see  where  you  can change  things.  Then  change  the  code  to  do  the  following  things:

(a)Make  your  circle  bigger  -  specifically,  double  the  radius.

(b)Your  circle  is  currently  centered  in  your  window.  Change  your  code  so  that  the  circle  is  now  located in  the  upper  right  hand  corner  of  the  window.  Specifically,  the  center  of  the  circle  should  be  located in  the  middle  of  the  upper-right  quadrant  of  the  window.  (Hint:  coordinates  are  counted  from  the top-left  corner.  You  can  also  use  a  trial-and-error  approach  by  changing  the  numbers  for  the  circle until  you  get  what  you  want!)

(c)Make  the  circle  yellow.

(d)Make  the  outline  of  the  circle  purple.  (Hint:  you  will  need  to  look  up  how  to  do  this in the  online  graphics  documentation.  Remember  that  all  the  functions for  “Graphics  Objects”  can  be  used  for  any  shapes!)

(e)Then  submit  your  code.
 
### 6. Yummy graphics (optional) - `parfait_graphics.py` 
We  already  know  how  to  print  text  in  the  Python  shell,  but  sometimes  we  may  want  to  “draw”  text,  so that  we  can  decide  its  color,  size,  and  more.  The  code  in `parfait_graphics.py` is  an  example  of  how  to draw  text  on  the  screen.  Run  the  program  to  see  the  text  it  draws  in  the  window.

Now,  change  the  font  size,  style,  and  color  of  the  text.  (You  can  pick  whatever  you  like!)  Look  at  the `setSize`, `setStyle`, and `setTextColor` methods  in  the  documentation  under  Text  methods.  All  the `set` methods  that  change  the  attributes  of  the  graphics  object  automatically  update  its  appearance  on  the screen.

After  you’ve  played  around,  use  the  functions  you  wrote  in  exercise  2  in `desserts.py` to  “draw”  your recipe  for  ladyfinger  parfaits  on  the  screen.  (*Hint:  Change  the `print` statements  to  draw  text  on  the screen  instead.  You  will  need  to  choose  the  locations  to  “draw”  each  line  of  text!)*

Create  a  function  called `parfait_stamp` that  takes  in  an `x` and a `y` value  and  draws  a  ladyfinger  parfait centered  around  the  point  (x,  y)  on  the  screen.  (Don’t  worry:  we’re  not  grading  for  realism.)  Decorate your  recipe!

### Submitting your PSET
After you’ve finished your PSET, type into the terminal:
```
$ git add -A
$ git commit -m "Submitting pset 2"
$ git push
```
You can do this as many times as you'd like to. You can also write whatever you'd like in the quotations (instead of just "Submitting pset 2"), but the instructors will be able to see it!
