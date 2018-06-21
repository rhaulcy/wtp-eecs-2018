# WTP CS Problem Set 9.4 - Tetris: Day 4

To get started, log into your Edmodo student account, find the post for problem set 9.4, and download the files. You will also need your `tetrominoes.py` code from yesterday. Copy your `tetrominoes.py` code into the folder for problem set 9.4.

### 1. Rotaytoe, Rotahtoe
When  you  press  the  up  arrow  key,  your  shapes  should  rotate  around  the  "center  coordinate"  block  (defined  in  an earlier  tetris  assignment).  This  should  only  require  a  small  change  to  your  `handle_keypress`  function  and  the  addition of  a  `rotate`  method  inside  the  `Shape` class,  as  long  as  you  use  some  clever  math.  Try  writing  out  initial  block locations  and  after‑rotation  block  locations  for  various  shapes  using  pen  and  paper.  Do  you  see  a  pattern? 

It's  ok  if  it  doesn't  work  exactly  correctly  for  all  edge  cases,  but  if  you've  finished  basic  rotation  and  part  2,  consider handling  the  following  scenarios:

  * squares  don't  rotate  at  all
  * once  you  rotate  one  direction,  the  next  rotate  should  be  in  the  opposite  direction  (so  that  the  I  shape  doesn't move  up  one  block  if  you  rotate  it  twice  before  dropping,  for  example);  this  really  only  applies  to  the  I,  S,  and  Z shapes,  though.
  * you  don't  want  to  rotate  if  rotating  will  cause  blocks  to  go  off  the  edge  of  the  screen  or  hit  another  shape  (maybe write  a  `can_rotate`  function,  similar  to  `can_move`)
 
### 2. The End
If  the  shapes  stack  up  to  the  very  top  of  the  board  such  that  no  new  shape  can  be  added,  the  game  should  end. Implement  this  functionality.
 
### 3. Bonus: The Fancy Stuff
If  you've  finished  your  Tetris  and  helped  at  least  5  others  (or  you  want  to  keep  working  on  this  when  you  go  home), try  out  these  challenges:

  * Add  scorekeeping  and  tell  the  user  what  their  score  is  for  the  game
  * Add  levels:  if  a  player  scores  high  enough,  start  a  new  game  that  is  more  challenging  (faster?  fewer  I  pieces?)
  * Piece  preview:  add  a  window  that  shows  what  the  upcoming  shapes  are
  * Pause  game:  add  code  so  that  hitting  the  p  key  on  the  keyboard  pauses  the  game
  
### 4. Testing
You  should  write  your  own  tests  as  you  do  each  problem  to  make  sure  each  step  of  your  solution  works.  Once everything  works,  you  should  be  able  to  run  one  function  and  play  tetris!

### Submitting your PSET
After you’ve finished your PSET, log into your Edmodo account, find the post for Problem Set 9.4, click "Open Assignment", attach all of the files that you created or edited for Problem Set 9.4, and then click "Turn in Assignment". You can resubmit the assignment as many times as you'd like. After you turn in your assignment, you're all done!
