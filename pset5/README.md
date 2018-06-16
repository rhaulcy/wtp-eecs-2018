# WTP CS Problem Set 5

To get started, log into your Edmodo student account, find the post for Problem Set 5, and download the files.

### 1. Translation - `translator.py`
Sometimes  people  have  to  talk  to  automated  systems  over  the  phone.  They  might  ask  you  to  read  out some  sort  of  number  for  identification  –  for  example,  your  confirmation  number,  bank  account  number, or  social  security  number.  If  the  number  is  1234,  you  might  read  it  out  as  “one-two-three-four.”

Now  imagine  you  have  to  speak  to  a  Spanish  company,  but  you  don’t  know  Spanish!  We  are  going  to write  a  really  simple  translator  that  will  help  you  translate  English  numbers  to  Spanish  numbers.

Open `translator.py`. Your  code  should  ask  for  one  or  more  numbers,  spelled  out  in  English.  Then,  it  should  print  out  the Spanish  numbers.  Please  use  a  dictionary  for  this!  Your  program  should  work  as  follows:

```python
Enter  one  (or  more)  numbers  spelled  out  in  English:  two  three
The  Spanish  translation  is:  dos  tres
```

Note:  You  can  assume  your  user  correctly  inputs  one  (or  more)  English  numbers  separated  by  a  space. You  don’t  have  to  handle  other  cases.  (But  of  course  you  can  if  you  like!)

### 2. Binary Conversion - `binary.py`
(a) Consider  the  problem  of  converting  an  integer  number  into  a  binary  number.  There  are  many  ways  to do  this  binary  conversion,  but  in  this  problem  we  are  going  to  use  something  similar  to  the  following procedure:

While  the  number  is  greater  than  zero, 

  i. Find  the  remainder  after  dividing  the  number  by  2.  (The  remainder  would  be  0  or  1.)
  
  ii. Print  the  remainder.
  
  iii. Divide  the  number  by  2,  using  floor  division.  Set  the  number  to  this  new  result,  and  repeat  (if the  number  is  still  greater  than  zero).
  
Open `binary.py` and write  code  that  takes  a  decimal  number  and  prints  out  1’s  and  0’s  based  on  the  procedure  above. The  program  should  work  as  follows:

```python
Enter  a  number:  23
The  result  of  our  procedure  is:  11101
```

(b) It  turns  out  that  there  is  one  problem  with  this  procedure,  which  is  that  it  prints  the  binary  number in  reverse.  For  example,  suppose  we  want  to  find  the  binary  form  of  23.  Using  this  procedure,  we get  the  result  as  11101  instead  of  the  correct  binary  number  10111. 

To  fix  this  “bug”,  we  are  going  to  use  a  list  to  reverse  the  binary  number.  Instead  of  printing  each binary  digit  as  we  get  it,  we  add the  digit  to  a  list.  After  the  entire  number  has  been  converted into  the  binary  form,  we  pop  one  digit  at  a  time  from  the list and  print  it.  This  allows  us  to  get the  decimal  number  converted  into  its  correct  binary  form. Remember that we can use the following methods on lists (assume we have a list `s`):
  * s.append(item) can be used to add an item to the end of list `s` 
  * len(s)  ==  0 can be used to check whether list `s` is empty 
  * s.pop() can be used to remove the  last  element  from the list `s` and will return the last element. You  should  only  need  to  use  the len, append, and pop methods  of  the  lists. 
  
Write  a  program  that  allows  the  user  to  type  in  an  integer  and  outputs  the  correct  binary  representation  of  that  integer.  Your  program  should  work  as  follows:

```python
Enter  a  number:  23
The  binary  representation  is:  10111
```

Note:  You  can  assume  the  user  types  in  a  non-negative  integer.  What  should  you  do  if  the  user inputs  0?

**Optional:** If  the  user  types  in  a  negative  number,  keep  prompting  until  a  non-negative  number  is entered.

### 3. Acronyms - `acronyms.py`
This  exercise  will  allow  you  to  practice  with  the  methods  for  strings  and  lists.  An  acronym  is  a  word formed  by  taking  the  first  letters  of  the  words  in  a  phrase  and  making  a  word  from  them.  For  example, RAM  is  an  acronym  for  “random  access  memory.”  In  this  exercise,  you  are  going  to  write  a  program  in the file `acronyms.py`.  This  program  should  allow  the  user  to  type  in  a  phrase,  and  the  program  should then  output  the  acronym  for  that  phrase.  An  example  of  how  your  program  should  work  is  as  follows:

```python
Enter  a  phrase:  random  access  memory
Your  acronym  is:  RAM
```

Note:  The  acronym  should  be  all  uppercase,  even  if  the  words  in  the  phrase  are  not  capitalized!

### 4. Concentration - `concentration.py`
Concentration  is  a  card  game  in  which *n* pairs  of  cards  are  laid  face  down  in  some  random  arrangement. A  player  chooses  two  cards  to  flip  over.  If  the  cards  are  a  pair,  then  the  pair  is  removed  from  play. Otherwise,  the  cards  are  flipped  face  back  down  and  the  player  chooses  again.  The  goal  is  to  match  all the  cards. 

Let’s  write  a  program  that  allows  a  user  to  play  this  game!

We’ll  have  users  play  on  a  4×4  grid.  That  makes  8  pairs.  We  can  represent  each  card  with  an  integer value  between  0  and  7,  so  that  two  cards  are  a  pair  if  they  have  the  same  value. 

Open `concentration.py`.  We  have  already  written  code  for  you  that  shuffles  the  cards  in  a  random  order and  draws  them  in  a  grid  on  the  screen.  Each  card  is  drawn  in  a  color  representing  its  card  value.  Choose your  eight  favorite  colors! 

Add  some  code  to  store  the  grid  of  cards  in  a  dictionary.  For  the  key,  use  a  tuple `(column,  row)`,  which is  the  grid  location  of  the  card.  The  value  will  be  another  tuple `(value,  rect)`,  where `value` is  the  card value  itself  and `rect` is  the  card’s  Rectangle  object  drawn  in  the  user  interface. 

Fill  in  the  function `get_card` that  waits  for  the  user  to  click  on  a  card  and  returns  the  card  location.  Wait for  the  user  to  click  the  mouse  and  convert  the  pointer  coordinates  into  a  card  location  of  the  type  stored in  the  dictionary.  Check  if  that  location  has  a  card  in  it  *(Hint:  Use  the `in` operator  on  the  dictionary  to check  if  there  is  a  key  corresponding  to  the  location).*  Make  the  user  keep  clicking  until  she  clicks  on  an occupied  location.

Add  some  code  that  waits  for  the  user  to  click  on  two  different  cards,  then  compares  their  values.  *(What happens  if  the  user  clicks  on  the  same  card  twice?)*  If  their  values  are  the  same,  then  remove  them  from the  grid.  Remember  you  will  also  have  to  undraw  them  on  the  screen. 

The  game  is  won  when  all  the  cards  have  been  removed.  Write  a  function `is_game_over` that  checks whether  the  grid  is  empty  and  returns  a  boolean  value `True` or `False`.  Add  a  loop  to  the  main  program to  make  the  user  keep  playing  until  she  wins.

Finally,  remember  that  the  cards  are  supposed  to  start  face  down.  Change  your  drawing  so  that  all  the cards  are  the  same  color  (face  down).  Add  some  code  so  that  a  card  becomes  face  up  (showing  its  real color)  when  the  user  clicks  on  it.  If  two  cards  are  chosen  that  do  not  match,  you  flip  them  back  facedown.  Make  sure  you  wait  a  bit  so  the  user  can  see  the  cards’  colors  before  flipping  them  back  face  down!

### 5. Optional Challenge Problem: Tic-tac-toe - `tictactoe.py`
*The  next  problem  asks  you  to  combine  everything  you  have  learned  so  far.  It’s  a  difficult  challenge,  but we  feel  confident  that  you  will  learn  a  lot  by  doing  it!*

Tic-Tac-Toe  is  a  game  played  between  two  players  on  a  3x3  board.  One  player  is  X,  and  one  player  is O.  The  players  take  turns  drawing  X’s  and  O’s  on  the  board,  trying  to  make  a  horizontal,  vertical,  or diagonal  line  of  three  of  their  symbol  on  the  board.  Let’s  write  a  program  that  allows  two  players  to  play Tic-Tac-Toe  against  each  other.

To  make  this  easier,  we  will  break  the  program  into  parts  and  use  the  skeleton  provided  in `tictactoe.py`:

(a) First,  fill  in  the  function `draw_board()` to  draw  the  Tic-Tac-Toe  board.  We  can  do  this  by  using lines  from  the `graphics` module.

(b) Write  functions  to  draw  X’s  and  O’s  on  the  board  in `draw_O(i,j)` and `draw_X(i,j)`. `i` represents which  row  of  the  board  we  are  drawing  in,  and `j` represents  which  column  of  the  board  we  are  drawing in.  Therefore,  they  should  take  the  value  0,  1,  or  2,  where `draw_O(0,0)` draws  a  O  in  the  top  left corner  of  the  board.

(c) You’ll  need  to  keep  track  of  the  state  of  the  board  (which  of  the  9  squares  are  O,  X,  or  empty). There  are  many  ways  to  do  this,  but  we  suggest  the  following  approach,  and  we  have  included  the following  code  in  your  program:
```python
#  save  the  state  of  the  board  (empty  at  first)
board_state  =  ["","","","","","","","",""]
```

As  you  can  see,  we  use  a  list  of  9  items  to  represent  the  9  squares.  Each  element  in  the  list  represents the  state  of  each  tic-tac-toe  square.  The  way  we  interpret  the  board  state  is  as  follows:
  * If  the  list  element  is  the  empty  string "",  it  means  the  corresponding  square  is  empty.
  * If  the  list  element  is  the  string "X",  it  means  the  corresponding  square  has  an  X  in  it.
  * If  the  list  element  is  the  string "O",  it  means  the  corresponding  square  has  an  O  in  it. 
  
We  would  suggest  mapping  the  n-th  list  element  to  the  (i,  j)th  square  in  the  tic-tac-toe  board  as follows:
![tic tac toe grid](./tictactoe.PNG)

Think  of  a  formula  function `f` that  uses `i` and `j` to  come  up  with  the  list  index, `n`,  that  corresponds to  the  (i,  j)th  square.  For  example,  your  formula  should  take  in  the  following  (i,  j)  input  and  output the  following  n:
```python
(i,  j)  ->  n
(0,  0)  ->  0
(0,  1)  ->  1
(0,  2)  ->  2
(1,  0)  ->  3
...
```

Write  your  formula  function `f(i,j)` that  gives  the  corresponding `n` in a comment in the file.

Based  on  our  above  description,  what  would  the  following  board  states  describe?
```python
board_state_1=["","","","","","","","",""]
board_state_2=["O",  "","","","","","","",""]
board_state_3=["","",  "X",  "",  "X",  "",  "X",  "O",  "O"]
```

Draw  three  pictures  of  tic-tac-toe  boards,  and  label  which  list  each  picture  corresponds  to  (`board_state_1`, `board_state_2`,  or `board_state_3`).

(d) Fill  in  the  function `is_empty(i,  j)` which  uses `board_state` to  check  whether  the  (i,  j)th  square  of the  board  is  empty.  (You  can  assume `board_state` is  as  we  described  above,  although  we  have  not yet  written  any  code  to  update  or  change  it.)

(e) Fill  in  the  function `update_board_state(i,  j,  player)`,  which  should  update  the  board  state  to remember  that  player `player`(i.e.,  X  or  O)  played  in  the  the  (i,  j)th  square  of  the  board.

(f) Assuming  that  the `board_state` variable  works  as  we  described,  fill  in  the  function `is_board_full`, which  checks  the  board  state  and  returns `True` if  the  board  is  full,  and `False` otherwise.

(g) Assuming  that  the `board_state` variable  works  as  we  described,  fill  in `is_over()`.  The  function should  return `True` if  the  game  is  over,  and `False` otherwise.  What  are  all  the  ways  a  game  can  be over? Also,  if  the  game  is  over,  it  should  print  a  message  explaining  why  (for  example,  “Player  X  won!”). You  will  also  find `is_board_full` helpful  –  if  the  board  is  full,  is  the  game  over?

(h) Now,  we  will  fill  in  what  happens  during  one  player’s  turn  –  the  psuedocode  is  at  the  bottom  of  the file.  Have  the  players  click  the  mouse  in  the  window.  (Hint:  the  function `getMouse()` should  help.) Use  the  pointer  position  at  the  time  of  the  click  to  determine  what  square  on  the  board  the  player chose.  Try  to  place  the  player’s  symbol  in  that  square.  What  should  you  do  if  there  is  already  a symbol  there? 

As  a  programmer,  you  should  always  consider  “edge  conditions”  like  these  when  you  program!  Another  way  to  put  it  –  always  assume  that  the  users  of  your  program  will  be  trying  to  find  a  way  tobreak  it.  If  you  don’t  include  a  condition  that  checks  if  there  is  already  a  symbol  in  the  square  the user  chose,  what  will  happen? 

**Hint:** Remember  to  use  the  functions  you  have  already  written,  like `is_empty`, `update_board_state`, `draw_O`,  and `draw_X`.  Don’t  forget  that  the  board  state  and  the  drawn  board  must  both  be  updated separately!

(i) Fill  in  the  rest  of  the  section  titled ACTUAL  GAMEPLAY.  This  will  include  some  sort  of  loop  around one  player’s  turn,  so  that  players  can  play  until  one  of  them  wins  or  the  game  ends  in  a  tie.  Printout  the  result  of  the  game.

### Submitting your PSET
After you’ve finished your PSET, log into your Edmodo account, find the post for Problem Set 5, click "Open Assignment", attach all of the files that you created or edited for Problem Set 5, and then click "Turn in Assignment". You can resubmit the assignment as many times as you'd like. After you turn in your assignment, you're all done!

