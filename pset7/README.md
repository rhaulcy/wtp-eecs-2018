# WTP CS Problem Set 7

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

We  are  going  to  create  our  own  version  of  the  basic  Tetris  game  for  the  final  project.  The  goal  of  this exercise  is  to  get  familiar  with  the  game  and  to  create  the  shapes  (also  called  tetrominoes)  used  in  the  game. If  you’ve  never  played  it  before,  try: http://www.freetetris.org/ or http://vadim.oversigma.com/games/gbt.html (the  second  uses  MIT’s  green  building  as  a  screen  for  playing  the  game).  Just  remember you  need  to  stop  playing  at  some  point :-).There  are  seven  tetris  shapes  (tetrominoes),  which  you  can  see  below:
![alt text](screenshots/tetris.png "")


### Submitting your PSET
After you’ve finished your PSET, type into the terminal:
```
$ git add -A
$ git commit -m "Submitting pset 7"
$ git push
```
You can do this as many times as you'd like to. You can also write whatever you'd like in the quotations (instead of just "Submitting pset 7"), but the instructors will be able to see it!
