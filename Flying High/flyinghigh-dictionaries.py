#!/usr/bin/env python
#
# Flying High 
# Game Copyright Games Magazine, Issue May 2011
# Code by Kyle Anderson <kyle@xkyle.com>
# Under the GPL v2
# Get the Code:
# svn co https://dev.xkyle.com/gamesmagazine
# Wiki:  https://wiki.xkyle.com/Games_Magazine_-_Flying_High
#    
# Location Layout:
# 
#       1
# 2  3  4  5
# 6  7  8  9 
# 10 11 12 13
# 14 15 16 17
#    18

animalsdict = { 1:'chipmunk', 2:'monkey', 3:'bear', 4:'fox', 5:'bear', 6:'fox', 7:'chipmunk', 8:'bear', 9:'fox', 10:'fox', 11:'monkey', 12:'chipmunk', 13:'chipmunk', 14:'monkey', 15:'chipmunk', 16:'monkey', 17:'bear', 18:'fox' }
colorsdict = { 1:'blue', 2:'brown', 3:'blue', 4:'brown', 5:'pink', 6:'grey', 7:'brown', 8:'grey', 9:'brown', 10:'brown', 11:'grey', 12:'pink', 13:'grey', 14:'blue', 15:'grey', 16:'brown', 17:'blue', 18:'blue' }
rowdict = { 1:'row1', 2:'row2', 3:'row2', 4:'row2', 5:'row2', 6:'row3', 7:'row3', 8:'row3', 9:'row3', 10:'row4', 11:'row4', 12:'row4', 13:'row4', 14:'row5', 15:'row5', 16:'row5', 17:'row5', 18:'row6' }
coldict = { 1:'col3', 2:'col1', 3:'col2', 4:'col3', 5:'col4', 6:'col1', 7:'col2', 8:'col3', 9:'col4', 10:'col1', 11:'col2', 12:'col3', 13:'col4', 14:'col1', 15:'col2', 16:'col3', 17:'col4', 18:'col2' }


def Recurse(Position,PathTaken):
   if Position == 1:
      print PathTaken
      return
   # We should never end up on the same square twice, so if our path has more than 18 moves....
   elif len(PathTaken) > 18:
      return
   else: 
      # Lets go through our sets and see what our attributes are
      mycolor = colorsdict[Position]
      myanimal = animalsdict[Position]
      myrow = rowdict[Position]
      mycol = coldict[Position]
      #For possible spaces in my row
      for Possibility in [(k) for k, v in rowdict.items() if v==myrow and k not in PathTaken]:
         #We are allowed to move if it is the same color or same animal
         if mycolor == colorsdict[Possibility] or myanimal == animalsdict[Possibility]:
            Recurse(Possibility, PathTaken + (Possibility,))
      #For Possible spaces in our same column
      for Possibility in [(k) for k, v in coldict.items() if v==mycol and k not in PathTaken]:
         #We are allowed to move if it is the same color or same animal
         if mycolor == colorsdict[Possibility] or myanimal == animalsdict[Possibility]:
            Recurse(Possibility, PathTaken + (Possibility,))

#Starting Position 18, go!
Recurse(18,(18,)) 
