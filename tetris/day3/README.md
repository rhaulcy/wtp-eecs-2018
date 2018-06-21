# WTP CS Problem Set 9.3 - Tetris: Day 3

To get started, log into your Edmodo student account, find the post for problem set 9.3, and download the files. You will also need your `tetrominoes.py` code from yesterday. Copy your `tetrominoes.py` code into the folder for problem set 9.3.

### 1. Do What I Tell You To
It's  time  to  take  input  to  move  the  blocks  around!  Let  a  user  press  arrow  keys  to  move  the  shapes  left  and  right.  The 'down'  arrow  key  can  either  drop  the  shape  to  the  bottom,  or  just  move  it  down  faster. 

To  do  this,  we'll  need  to  add  code  that  will  "interrupt"  our  cycle  of  picking  a  shape,  dropping  it,  then  repeating.  Inside the  `__init__`  function  for  your  `Game`  class,  add:
```python
self.key=None
self.win.bind_all('<Key>',self.key_pressed)
```

*Note:  if  you  named  your  GraphWin  object  something  other  than  win,  use  that  variable  instead.*

Then  add  a  new  method  to  your  `Game`  class,  exactly  as  below  with  no  extra  code:
```python
def key_pressed(self,event):
  self.key=event.keysym
```

Once  these  two  parts  are  set  up,  write  some  third  method  like  `handle_keypress`  for  `Game`.  It  should  check  what  the value  of  `self.key`  is  and  move  the  current  shape  if  it's  able  to  move  in  that  direction.  The  attribute  `self.key`  will  be equal  to  whatever  you  press.  For  the  arrow  keys,  that  means  "Left",  "Right", "Up",  or  "Down".

Finally,  figure  out  where  to  call  the  `handle_keypress`  function.  Remember  that  you  want  to  be  able  to  move  a  shape even  while  it's  paused  before  its  next  drop.  It  might  be  a  good  idea  to  check  for  keypress,  wait  briefly,  check  for keypress,  wait  briefly,  and  so  on  until  it's  been  the  full  .3  seconds  (or  however  long  you  pause  between  moving  the current  shape  down  each  time).

*What's  happening?  The  `bind_all('<Key>',self.key_pressed)`  line  tells  Python  that  if  a  key  is  pressed,  the  `Game` method  `key_pressed`  should  be  called.  It  automatically  calls  it  with  an  event  parameter,  which  is  a  description  of what  happened.  We  can  then  get  the  value  key  from  the  event  by  getting  the  event  attribute  `keysym`.  The `key_pressed`  function  is  called  exactly  when  a  key  is  pressed, even  if  you're  already  in  the  middle  of  another function.  (This  is  called  a  "callback"  function.)*

*For  a  more  detailed  description,  see  the Tkinter documentation at http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm.  Tkinter  is  the  package  that  `graphics.py`  is  based on.*

*Why  not  call  `can_move`  and  `move`  directly  in  `key_pressed`?  We  give  you  this  design  strategy  because  if  you moved  a  block  exactly  when  the  key  was  pressed,  you  might  be  in  the  middle  of  moving  the  same  shape somehwere  else.  For  example,  you  might  press  a  key  right  after  your  code  checks  `can_move`  to  see  if  you  can move  your  shape  down  but  before  it  actually  moves  it.  In  that  situation,  the  `key_pressed`  function  would immediately  call  `can_move`  and  move  the  shape.  Then  your  code  would  resume  running  as  before,  and  even though  the  shape  is  now  in  a  different  spot,  it  still  thinks  it  can  move  down  more  from  before  it  was  interrupted. So  if  there  is  a  shape  that  is  one  space  from  the  bottom,  what  might  happen  is:  (1)  check  if  shape  `can_move`  down 1;  it  can.  (2)  Interrupted!  Check  if  shape  `can_move`  down  one.  It  (still)  can.  Move  the  shape  down  1.  (3)  Done being  interrupted.  Before  being  interrupted,  we  were  allowed  to  move,  so  let's  continue  moving:  move  down  1. (4)  Oops!  There  was  only  room  to  move  down  once,  but  we  moved  down  twice  and  off  the  edge  of  the  board.*

*For  a  better  understanding,  see  the StackOverflow question at https://stackoverflow.com/questions/34510/what-is-a-race-condition or  google  "race  conditions  and  threading".  (Or  just ask  a  staff  member!)*
 
### 2. I Can See Clearly Now
When  a  row  fills  up  with  blocks,  the  row  should  be  cleared  and  all  blocks  above  should  shift  down.  Implement  this behavior.

You  can  do  this  any  way  you'd  like,  but  we  suggest  writing  at  least  three  different  functions: 

  * a  function  to  check  if  any  row  is  full;  if  it  is,  return  the  number  of  the  full  row
  * a  function  to  undraw  and  delete  the  blocks  on  a  row,  given  the  row  number
  * a  function  to  move  all  the  blocks  above  the  just‑deleted  row  down  into  the  newly‑cleared  space
 
### 3. Testing
You  should  write  your  own  tests  as  you  do  each  problem  to  make  sure  each  step  of  your  solution  works.  Once everything  works,  you  should  be  able  to  run  one  function  and  see  shapes  drop  to  the  bottom,  stacking  on  top  of  each other.  You  should  be  able  to  press  the  arrow  keys  to  move  the  current  shape  left  or  right.  The  down  arrow  key  should make  it  drop  faster  or  just  drop  right  to  the  bottom.  If  a  row  fills  up,  it  should  get  cleared.

### Submitting your PSET
After you’ve finished your PSET, log into your Edmodo account, find the post for Problem Set 9.3, click "Open Assignment", attach all of the files that you created or edited for Problem Set 9.3, and then click "Turn in Assignment". You can resubmit the assignment as many times as you'd like. After you turn in your assignment, you're all done!

