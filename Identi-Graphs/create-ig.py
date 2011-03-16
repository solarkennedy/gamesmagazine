#!/usr/bin/env python
# Game idea and key copyright Games Magazine and Adam Fromm 2011
# Found in Games Magazine, May 2011 Issue, Page 34.

import sys

DirectionKey = { H:"North West",
		 N:"North",
		 O:"North East",
		 E:"East",
		 U:"South East",
		 S:"South",
		 T:"South West",
		 W:"West" }

#List comprehension that merges the strings
Input = ''.join([arg for arg in sys.argv[1:]]).lower()

print Input

# No X or Q
Key = { a:(1,"H"), b:(1,"N"), c:(1,"O"), d:(1,"E"), e:(1,"U"), f:(1,"S"), g:(1,"T", h:(1,"W"), 
        i:(2,"H"), j:(2,"N"), k:(2,"O"), l:(2,"E"), m:(2,"U"), n:(2,"S"), o:(2,"T", p:(2,"W"), 
        r:(3,"H"), s:(3,"N"), t:(3,"O"), u:(3,"E"), v:(3,"U"), w:(3,"S"), x:(3,"T", y:(3,"W") } 

def Move(Start, Direction):
	x = Start[0]
	y = Start[1]
	
	 Value = {
	  'H': lambda x: x + 1, y: y - 1,
	  'W': lambda x: x - 2, y: y
	}[Direction](x,y)

Position = (0,0)
for Letter in Input:
	print "Doing letter: " + str(Letter)
	
