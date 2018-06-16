# WTP CS Problem Set 3

To get started, log into your Edmodo student account, find the post for Problem Set 3, and download the files.
 
### 1. Write a Mad Lib - `madlib.py`

Mad  Libs  are  word  games  where  one  player  fills  in  the  blanks  of  another  player’s  story  by  providing  words of  certain  types.  When  the  words  are  substituted  in  for  the  blanks,  the  result  is  a  complete,  grammatically correct  but  often  nonsensical  story.

In `madlib.py` we  are  going  to  write  a  program  that  lets  the  user  make  a  Mad  Lib!

(a) First,  you  will  need  a  Mad  Lib:  we  have  provided  a  (terrible!)  personal  ad  Mad  Lib  in  the  file `personal_ad.txt`,  but  feel  free  to  write  your  own  or  choose  one  from http://www.madglibs.com/

(b) Now,  as  we  did  for  Evil  Pierre  in  class,  some  words  need  to  be  replaced  with  variables.  In  this  case, replace  any  “blanks”  in  the  story  with  variables. 

(c) Now,  using  the `raw_input` command  we  learned  in  class,  prompt  the  user  for  words  to  fill  in  the blanks.  Ask the  user  for  at  least  4  inputs.

(d) Finally,  print  out  the  story  for  the  user!

### 2.  Mouse Input - `mousepoint.py`
In  this  exercise,  we’ll  experiment  with  a  different  type  of  user  input:  the  mouse  pointer.  You  can  find all  the  documentation  for  the  graphics  module  in the graphics reference sheet on Edmodo. 

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

Open `guessnum.py` and write  a  function `guess_compare` that  asks  the  user  for  a  guess,  then  compares  that  guess  with  the  correct number  and  prints  out  “Too  low!”,  “Too  high!”,  or  “Correct!” 

Note: Remember that `raw_input` takes in the user's input as a string. You can use casting to convert that input into a number or you can use `input` instead of `raw_input`.

Give  the  user  five  guesses.  If  the  user  has  not  yet  guessed  the  number,  print  out  the  correct  answer. *(Hint:  Your  function `guess_compare` will  need  to  return  whether  the  guess  was  correct.)*  Test  your  game.

**Optional:** If  the  user  gets `n` guesses,  what  is  the  largest  range  of  numbers  the  program  can  choose  from and  still  guarantee  that  the  user  can  win?  What  is  the  strategy  that  the  user  should  use?

### 4. Blackjack - `blackjack.py`
Blackjack  is  a  popular  game  (feel  free  to  read  up  more  on  the  game  on  Wikipedia:https://en.wikipedia.org/wiki/Blackjack).  The  goal  of  the  game  is  to  get  to  a  score  of  21  without  going  over. Below  is  a  fragment  of  code.  Given  the  inputs in the table below,  what  does  it  output?

Open `blackjack.py` and use comments to fill in the table. Do  this *without* running  the  code.  (It  is  an  important  skill  to  be  able  to  understand  what  a  piece  of  code does  without  running  it.)

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

The table below is provided in `blackjack.py`:

| card1 | card2 | dealer_card | output |
| ----- | ----- | ----------- | ------ |
| 3     | 8     | 4           |        |
| 9     | 8     | 10          |        |
| 11    | 10    | 10          |        |
| 3     | 5     | 4           |        |
| 5     | 8     | 8           |        |

### 5. Card Counting in Blackjack
As  you  may  know  from  the  movie *21*,  there  is  a  technique  to  count  cards  while  playing  Blackjack  that can  help  the  player  determine  when  they  are  likely  to  win  or  lose!  Specifically,  when  counting  cards,  you keep  track  of  a  running  total  that  goes  up  and  down  based  on  the  cards  you  have  seen.  In  this  problem, we  will  be  building  a  program  that  will  count  cards  for  the  user.  Detailed  instructions  and  pseudocode are  in  each  file.

(a) **Using  a  list  of  cards** – `cardlist.py`
First,  fill  in  the  missing  code  in `cardlist.py`,  as  described  in  the  comments.  The  program  should prompt  the  user  for  a  card,  and  check  the  user’s  response  against  the  provided  list.  Then,  the program  should  print  whether  the  user  input  a  valid  or  invalid  card.  This  program  is  the  first  step toward  getting  our  card  counting  code  working!

(b) **Getting  card  values  for  MIT  card  counting** – `cardcountvalue.py`
Now,  build  on  the  code  you  wrote  in `cardlist.py` to  fill  in `cardcountvalue.py`.  This  program prompts  the  user  for  one  card’s  value  (assume  it  is  a  single  card,  not  part  of  a  series  of  cards)  and produces  the  corresponding  card  counting  value  for  it,  according  to  the  MIT  card  counting  approach. (If  the  user’s  response  is  invalid,  it  tells  the  user  it  was  invalid.) 

Specifically,  MIT  card  counting  approach  assigns  card  counting  values  as  follows:
  * 2  -  6  should  add  one  to  the  count,  so  their  value  is  1
  * 7  -  9  have  no  effect  on  the  count,  so  their  value  is  0
  * A,  10,  J,  Q,  and  K,  should  subtract  one  from  the  count,  so  their  value  is  -1
  
We  will  finish  the  card  counting  program  tomorrow  on  ps4,  and  you  will  re-use  the  code  you  wrote  today!
 
### 6. Guess Your Number (optional) - `guessnum2.py` 
Write  a  Guess  Your  Number!  game in `guessnum2.py`.  In  this  game,  the  program  will  try  to  guess  your  number!  Here  is  an example  of  how  the  program  will  work:

```
I'm  ready  to  guess!
What  is  the  minimum  possible  number?  0
What  is  the  maximum  possible  number?  30
Hmm...I  guess  5.  Is  that  (1)  too  low,  (2)  too  high,  or  (3)  correct?  1
I  guess  20.  Is  that  (1)  too  low,  (2)  too  high,  or  (3)  correct?  2
I  guess  13.  Is  that  (1)  too  low,  (2)  too  high,  or  (3)  correct?  1
I  guess  17.  Is  that  (1)  too  low,  (2)  too  high,  or  (3)  correct?  3
Yay!  So  your  number  was  17.  Good  game.
```

Think  about  what  strategy  the  program  should  use  to  guess  your  number.  What  does  it  need  to  remember? These  are  your  variables.  Give  the  computer  5  guesses  before  it  gives  up  and  asks  for  the  answer.

### Submitting your PSET
After you’ve finished your PSET, log into your Edmodo account, find the post for Problem Set 3, click "Open Assignment", attach all of the files that you created or edited for Problem Set 3, and then click "Turn in Assignment". You can resubmit the assignment as many times as you'd like. After you turn in your assignment, you're all done!
