# WTP CS Problem Set 7

To get started, log into your Edmodo student account, find the post for Problem Set 7, and download the files.

### 1. Understanding inheritance
Consider the following code:

```python
class  Spell(object):
  def  __init__(self,  incantation,  name):
    self.name =  name
    self.incantation =  incantation
    
  def  __str__(self):
    return self.name +  '  '  + self.incantation +  '\n'  + self.get_description()
    
  def  get_description(self):
    return  'No  description'
    
  def  execute(self):
    print self.incantation
    
class  Accio(Spell):
  def  __init__(self):
    Spell.__init__(self,  'Accio',  'Summoning  Charm')
    
class  Confundo(Spell):
  def  __init__(self):
    Spell.__init__(self,  'Confundo',  'Confundus  Charm')
    
  def  get_description(self):
    return  'Causes  the  victim  to  become  confused  and  befuddled.'
    
def  study_spell(spell):
  print  spell
  
spell  =  Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())
```

Create a file called `inheritance.py` and use comments to answer the following questions:

(a) What are the parent and child classes here?

(b) What  does  the  code  print  out?  (Try  figuring  it  out  without  running  it  in  Python.)  Please  mention which  lines  of  code  are  printing  which  lines  of  output.

(c) Which `get_description` method  is  called  when `study_spell(Confundo())` is  executed?  Why?

(d) What  do  we  need  to  do  so  that `print  Accio()` will  print  the  appropriate  description ( `'This  charm  summons  an  object  to  the  caster,  potentially  over  a  significant  distance'`)? Write  down  the  code  that  we  need  to  add  and/or  change.

### 2.  Tetris! It begins! - `tetrominoes.py` 
Tetris  is  deemed  by  some  the  most  popular  video  game  of  all  times.  It  is  a  puzzle  game  developed  by Alexey  Pajitnov  in  1984  while  he  was  working  at  the  Academy  of  Science  of  the  former  USSR  in  Moscow. There  have  been  hundreds  of  variants  of  the  game  developed  since.

We  are  going  to  create  our  own  version  of  the  basic  Tetris  game  for  the  final  project.  The  goal  of  this exercise  is  to  get  familiar  with  the  game  and  to  create  the  shapes  (also  called  tetrominoes)  used  in  the  game. If  you’ve  never  played  it  before,  try: http://www.freetetris.org/ or http://vadim.oversigma.com/games/gbt.html (the  second  uses  MIT’s  green  building  as  a  screen  for  playing  the  game).  Just  remember you  need  to  stop  playing  at  some  point :-).There  are  seven  tetris  shapes  (tetrominoes),  which  you  can  see  in tetris.png.

As  you  can  see,  each  of  the  tetrominoes  is  made  up  of  4  squares,  which  we  will  call  "blocks".  (Note: remember  that  a  square  is  a  type  of  rectangle!)

**Blocks** 

The  tetris  board  is  10  squares  wide  by  20  squares  high.  Each  block  (of  a  tetris  shape)  occupies  a  single square  at  a  time.  In  the  file `tetrominoes.py`,  create  a `Block` class  that  inherits  from  the `Rectangle` class from  the `graphics` module  and  save  it. 
**Hint:** Look  up  the  documentation  for  the `Rectangle` class  from  the `graphics` module  now!  You  can  use the graphics reference  sheet on Edmodo. Note  the  constructor  and  its  other  methods  –  you  will  find  some  of  these  useful.

Now,  make  the  constructor  for  the `Block` class.  The `block` class should take in a `Point(...)` parameter corresponding to the position of the block and a `color` parameter corresponding to the color of the block. It  should  have `x` and `y` attributes  that  correspond  to  the position  of  the  block  on  the  tetris  board (these values can be extracted from the `Point(...)` parameter).  The  “block  position”  (0,  0)  is  the  top  left  corner  of  the  board and  (9,  19)  is  the  bottom  right  corner.  Make  your  blocks  have  a  width  of  30  pixels. 
**Hint:** the  “block  position”  coordinates  are  different  from  the  window’s  pixel  coordinates! When  your `Block` constructor  is  done,  you  should  be  able  to  use  it  in  a  5  block  x  5  block  board  with  the code  below.  You  will  find  this  code  in  your  template  file  to  ensure  that  your `Block` class  works  correctly.

```python
win  =  GraphWin("Tetrominoes",  150,  150)

#  the  block  is  drawn  at  position  (1,  1)  on  the  board
block  =  Block(Point(1,  1),  'red')
block.draw(win)

win.mainloop()
```
*Hint:  Think  about  how  you  can  use  the  Rectangle  constructor  in  your  Block  constructor.*

**Moving  blocks**

Add  a `move` method  to  your `Block` class  that  will  take  as  parameters `dx` and `dy` telling  the  block  to  move
dx  squares  (not  pixels!)  in  the  x-direction  and  dy  squares  in  the  y-direction.  Again,  our  y-axis  will  be pointing  downwards. 

Here  is  how  you  should  be  able  to  move  a `Block`:
```python
win  =  GraphWin("Tetrominoes",  150,  150)

block  =  Block(Point(1,  1),  'red')  #  the  block  is  drawn  at  position  (1,  1)  on  the  board
block.draw(win)
block.move(2, 1)  #  now  the  block  is  at  position  (3,  2)

win.mainloop()
```
*Hint:  Think  about  how  to  reuse  the  Rectangle  superclass  move  method.*

**Tetris  Shape  (Tetromino)**

Now,  we  will  create  a `Shape` class,  which  we  will  use  as  a  parent  class  (superclass)  for  7  different  tetris shapes. `Shape` needs  to  have  a  list  of  4  blocks  as  an  attribute,  as  well  as  a `move` method  and  a `draw` method.  The `move` method  will  take  as  parameters `dx` and`dy` telling  the  shape  to  move  dx  squares  in the  x-direction  and  dy  squares  in  the  y-direction.  The  constructor  should  take  two  parameters  as  shown below:  a  list  of  4 `Points`,  which  should  be  the  locations  of  the  4  blocks,  and  a  color.

As  an  example,  here  is  a  code  snippet  that  uses  the `Shape` class  as  a  parent  class  for  an `I_shape` class.
```python
class  I_shape(Shape):
  def  __init__(self,  center):
    coords  =  [Point(center.x  -  1,  center.y),
                Point(center.x  ,  center.y),
                Point(center.x  +  1,  center.y),
                Point(center.x  +  2,  center.y)]
    Shape.__init__(self,  coords,  "blue")
    self.center_block = self.blocks[1]
```
As  you  can  see  in  the  example,  the  `I_shape` constructor  takes  one  parameter, `center`,  which  is  a `Point` that  holds  the  position  of  the  central  block  in  the  shape  (i.e.,  the  center  of  rotation).  It  also  creates  and saves  a `center_block` attribute  of  the `I_shape` class,  which  uses  the `blocks` attribute  that  you  will  create in  the `Shape` class.  We  have  defined  the  central  block  for  each  tetromino  as  the  blocks  colored  in  black, which can be seen in blocks.png.

*Note:  You  do  not  have  to  follow  the  color  scheme  of  the  tetrominoes  shown  in  the  picture  –  all  your  blocks can  be  blue  (or  you  can  color  them  however  you  want).*

Once  you  have  written  your `Shape` class,  verify  that  it  can  display  the `I_shape` correctly,  using  the  code below:
```python
win  =  GraphWin("Tetrominoes",  200,  150)

shape  =  I_shape(Point(1,  1))
shape.draw(win) #  Draw  an  I_shape  at  (1,  1)
shape.move(2, 1)  #  Move  the  I_shape  to  (3,  2)

win.mainloop()
```

**Many  Tetrominoes**

Now  create  a  subclass  for  each  of  the  other  6  shapes.  The  central  block  for  each  subclass  (tetromino)  is defined  in  the  figure  on  the  previous  page. 

You  can  test  all  of  your  tetromino  subclasses  using  the  example  code  below:
```python
win  =  GraphWin("Tetrominoes",  900,  150)

#  a  list  of  shape  classes
tetrominoes  =  [I_shape,  J_shape,  L_shape,  O_shape,  S_shape,  T_shape,  Z_shape]
cx  =  0
for  tetromino  in  tetrominoes:
  #  create  a  shape  centered  at  row  1,  column  3
  shape  =  tetromino(Point(3,  1))
  shape.draw(win)
  shape.move(cx, 0)
  cx  +=  4
  
win.mainloop()
```

Congratulations!  You  have  finished  the  first  step  towards  your  tetris  game:  creating  all  the  tetrominoes!

### Submitting your PSET
After you’ve finished your PSET, log into your Edmodo account, find the post for Problem Set 7, click "Open Assignment", attach all of the files that you created or edited for Problem Set 7, and then click "Turn in Assignment". You can resubmit the assignment as many times as you'd like. After you turn in your assignment, you're all done!
