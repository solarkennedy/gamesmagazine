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

chipmunks = [1,7,12,13,15]
monkeys   = [2,11,14,16]
bears     = [3,5,8,17]
foxes     = [4,6,9,10,18]
animals = [chipmunks,monkeys,bears,foxes]

blues     = [1,3,14,17,18]
browns    = [2,4,7,9,10,16]
greys     = [6,8,11,13,15]
pinks	  = [5,12]
colors = [blues,browns,greys,pinks]

#There might be a better way to do this, but I'm sticking with lists:
row1 = [1]
row2 = [2,3,4,5]
row3 = [6,7,8,9]
row4 = [10,11,12,13]
row5 = [14,15,16,17]
row6 = [18]
rows = [row1,row2,row3,row4,row5,row6]

col1 = [2,6,10,14]
col2 = [3,7,11,15,18]
col3 = [1,4,8,12,16]
col4 = [5,9,13,17]
cols = [col1,col2,col3,col4]

def Recurse(Position,PathTaken):
   if Position == 1:
      print PathTaken
      return
   # We should never end up on the same square twice, so if our path has more than 18 moves....
   elif len(PathTaken) > 18:
      return
   else: 
      # Lets go through our sets and see what our attributes are
      # This list comprehension should return the list which has the right list in it, and only one list, so we want that one, 0.
      mycolor = [color for color in colors if Position in color][0]
      myanimal = [animal for animal in animals if Position in animal][0]
      myrow = [row for row in rows if Position in row][0]
      mycol = [col for col in cols if Position in col][0]
      #For possible spaces in my row
      for Possibility in myrow:
         #We are allowed to move if it is the same color or same animal
         if (Possibility in mycolor or Possibility in myanimal) and Possibility not in PathTaken:
            Recurse(Possibility, PathTaken + (Possibility,))
      #For Possible spaces in our same column
      for Possibility in mycol:
         #We are allowed to move if it is the same color or same animal
         if (Possibility in mycolor or Possibility in myanimal) and Possibility not in PathTaken:
            Recurse(Possibility, PathTaken + (Possibility,))

#Starting Position 18, go!
Recurse(18,(18,)) 
