# WTP CS Problem Set 4

### 1. Understanding Loops - `loops.py`
For the following fragments of code, create a new file called `loops.py` and write what the output would be using comments for each of the examples below. **Do this *without* running the code.**

Example 1:
```python
num1  =  10
while  num1  >  3:
  print  num1
  num1  =  num1  -  1
```

Example 2:
```python
num2  =  10
while  True:
  if  num2  <  7:
    #  break  makes  us  quit  the  loop
    break
  print  num2
  num2  =  num2  -  1
```

Example 3:
```python
divisor  =  2
for  i  in  range(0,  10,  2):
  print  i/divisor
```

You can use for loops to iterate through strings.

Example 4:
```python
my_string  =  "stressed"
for  letter  in  my_string:
  print  letter
```

Example 5:
```python
my_string  =  "stressed"
res  =  ''
for  letter  in  my_string:
  res  =  letter  +  res
print  res
```

### 2.  Exponentials - `exponential.py`
Imagine  that  the `**` operator  for  numbers  has  now  been  removed  from  the  Python  programming  language. Write  a  program  that  prompts  the  user  for  a  base  and  an  exponent  and  uses  a `for` loop  to  calculate `base**exp`.

We  will  assume  the  user  types  in  a  positive  integer.  (You  don’t  need  to  handle  other  cases.)

### 3. Card Counting in Blackjack (continued)
A  review  from  ps3:  As  you  may  know  from  the  movie *21*,  there  is  a  technique  to  count  cards  while playing  Blackjack  that  can  help  the  player  determine  when  they  are  likely  to  win  or  lose!  Specifically, when  counting  cards,  you  keep  track  of  a  running  total  that  goes  up  and  down  based  on  the  cards  you have  seen.  In  this  problem,  we  will  finish  a  program  that  will  count  cards  for  the  user.

(a) We  need  to  fill  in  the  missing  code  in `hotandcold.py`.  This  program  will  ask  for  cards  from the  user  and  keep  track  of  the  running  total  card  counting  score.  First,  copy  in  your  code  from `cardcountvalue.py` from `ps3`.

(b) **Knowing  when  to  bet** Now,  using  the  code  you  copied  in,  finish  the  program  so  that  it  uses  the total  card  counting  score  as  follows:

  * It  should  tell  the  user  when  to  bet  big  (if  the  running  total  is  5  or  greater).
  * It  should  tell  the  user  to  find  a  new  table  for  blackjack  (if  the  running  total  is  -5  or  less).
  * It  should  keep  asking  the  user  for  the  next  card  if  the  running  total  is  not  too  high  or  too  low (if  the  running  total  is  between  -5  and  5).
  
Test  out  your  program  to  make  sure  it  works  correctly,  and  if  it  does,  you  are  done!

### 4. Animations - `animate.py`
Loops  allow  us  to  make  animations.  By  drawing  the  same  object  over  and  over  again  at  different  locations on  the  screen,  we  can  give  the  illusion  of  movement.  The `graphics` module’s `move` command  makes  this really easy. `move(dx,dy)` takes  two  arguments `dx`,  the  number  of  pixels  to  shift  in  the x-direction,  and `dy`,  the  number  of  pixels  to  shift  in  the y-direction. `animate.py` gives  an  example  of  the `move` command on  a  circle.

The `sleep(ns)` command  in  the `time` module  pauses  the  program  for `ns` seconds  before  continuing execution.  Placing  a `sleep` command  before  moving  the  circle  slows  down  the  execution  so  that  you  can actually  see  the  circle  move.

(a) Let’s  make  the  circle  slide  across  the  screen.  Add  a  loop  around  the`sleep` and `move` commands. Change  the  arguments  so  that  the  circle  moves  1  pixel  to  the  right  every  10  milliseconds.  (To  avoid using  infinite  loops,  you  can  specify  a  finite  number  of  time  steps  for  the  circle  to  move,  e.g.,  30.)

(b) Cool!  If  we  let  the  animation  keep  going,  then  the  circle  will  move  off  the  right  edge  of  the  screen. Add  a  variable `x` to  keep  track  of  the  circle’s  position  and  a  variable `dx` for  its  velocity.  The  circle initially  starts  at  (100,  150),  so  by  updating `x` each  time  it  moves,  we  can  track  where  the  circle  is going.  When  the  circle  reaches  the  edge  of  the  screen,  make  it  change  direction.  Do  this  for  both directions  so  that  the  circle  bounces  back  and  forth  inside  the  screen.

(c) **(Optional)** Add  some  movement  in  the y-direction  so  that  the  circle  bounces  around  the  entire window.  Experiment  with  starting  the  circle  at  different  locations  or  changing  its  velocity.

(d) **(Optional)** Finally,  count  the  number  of  times  the  ball  hits  the  edge  of  the  screen.  Stop  the animation  once  the  ball  has  bounced  10  times.

### Submitting your PSET
After you’ve finished your PSET, type into the terminal:
```
$ git add -A
$ git commit -m "Submitting pset 3"
$ git push
```
You can do this as many times as you'd like to. You can also write whatever you'd like in the quotations (instead of just "Submitting pset 3"), but the instructors will be able to see it!

