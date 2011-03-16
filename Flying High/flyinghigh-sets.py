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

from sets import Set
chipmunks = Set([1,7,12,13,15])
monkeys   = Set([2,11,14,16])
bears     = Set([3,5,8,17])
foxes     = Set([4,6,10,18])
animals = Set([chipmunks,monkeys,bears,foxes])

blues     = Set([1,3,14,17,18])
browns    = Set([2,4,7,9,10,16])
greys     = Set([6,8,11,13,15])
colors = Set([blues,browns,greys])

#There might be a better way to do this, but I'm sticking with sets:
row1 = Set([1])
row2 = Set([2,3,4,5])
row3 = Set([6,7,8,9])
row4 = Set([10,11,12,13])
row5 = Set([14,15,16,17])
row6 = Set([18])
rows = Set([row1,row2,row3,row4,row5,row6])

col1 = Set([2,6,10,14])
col2 = Set([3,7,11,15,18])
col3 = Set([1,4,8,12,16])
col4 = Set([5,9,13,17])
cols = Set([col1,col2,col3,col4])

def Recurse(Position,PathTaken):
   if Position == 1:
      print PathTaken
      return
   # We should never end up on the same square twice, so if our path has more than 18 moves....
   elif len(PathTaken) > 18:
      return
   else: 
      # Lets go through our sets and see what our attributes are
      mycolorset = [color for color in colors if Position in color]
      myrow = [animal for animal in animals if Position in animal]
      myrow = [row for row in rows if Position in row]
      mycol = [col for col in cols if Position in col]
      #For possible spaces in my row
      for Possibility in myrow:
         #We are allowed to move if it is the same color or same animal
         if Possibility mycolor or myanimal == animalsdict[Possibility] and Possibility not in PathTaekn:
            Recurse(Possibility, PathTaken + (Possibility,))
      #For Possible spaces in our same column
      for Possibility in [(k) for k, v in coldict.items() if v==mycol and k not in PathTaken]:
         #We are allowed to move if it is the same color or same animal
         if mycolor == colorsdict[Possibility] or myanimal == animalsdict[Possibility]:
            Recurse(Possibility, PathTaken + (Possibility,))

#Starting Position 18, go!
Recurse(18,(18,)) 
