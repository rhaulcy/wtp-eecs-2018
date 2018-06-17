# WTP CS Problem Set 9.2 - Tetris: Day 2

To get started, log into your Edmodo student account, find the post for problem set 9.2, and download the files. You will also need your `tetrominoes.py` code from yesterday. Copy your `tetrominoes.py` code into the folder for problem set 9.2.

### 1. Randomize It
Write  a  function in `tetrominoes.py`  to  get  a  random  shape  letter,  like  I  or  J. 

*Hint:  importing  the  module  random  might  be  helpful.*
 
### 2. Loopy Loop
In  Tetris,  you  don't  just  drop  one  or  two  shapes;  you  keep  adding  new  shapes  to  the  board  and  dropping  them  until the  player  loses.  Write  a  function  that:

  1.  picks  a  random  shape
  2.  draws  it  at  the  top  of  the  tetris  board
  3.  drops  the  shape  down  until  it  hits  the  bottom
  
It  should  repeat  these  three  steps  either  indefinitely  (forever,  or  until  you  close  the  window),  or  for  a  set  number  of loops  that  you  accept  as  a  parameter  to  your  loop‑drop  function.

*Hint:  You  can  use  your  function  from  step  1  and  your  `add_drop_shape`  method  from  yesterday  to  add  a  random  shape to  the  board.*
 
### 3. Stacks on Stacks on Stacks
Change  your  program  so  that  the  shapes  stack  on  each  other  instead  of  always  going  to  the  bottom.  Depending  on how  you  wrote  your  earlier  functions,  this  could  require  just  a  small  change  to  the  Block  method  can_move.

*Hint:  There  are  a  number  of  different  ways  to  do  this.  We  think  the  easiest  might  be  to  keep  track  of  a  list  of  blocks that  have  dropped  and  hit  the  bottom,  then  change  your  can_move  function  to  check  for  both  board  edges  and  other blocks  in  the  potential  location.  However,  the  best  way  to  do  this  depends  on  what  your  earlier  code  looks  like  and what  makes  sense  to  you,  so  feel  free  to  do  something  different.*
 
### 4. Testing
You  should  write  your  own  tests  as  you  do  each  problem  to  make  sure  each  step  of  your  solution  works.  Once everything  works,  you  should  be  able  to  run  one  function  and  see  shapes  drop  to  the  bottom,  stacking  on  top  of  eachother.

### Submitting your PSET
After you’ve finished your PSET, log into your Edmodo account, find the post for Problem Set 9.2, click "Open Assignment", attach all of the files that you created or edited for Problem Set 9.2, and then click "Turn in Assignment". You can resubmit the assignment as many times as you'd like. After you turn in your assignment, you're all done!
