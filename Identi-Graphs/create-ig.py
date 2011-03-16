#!/usr/bin/env python
# Game idea and key copyright Games Magazine and Adam Fromm 2011
# Found in Games Magazine, May 2011 Issue, Page 34.

import sys
import Image, ImageDraw, ImageChops

Scale = 50

DirectionKey = { 'H':"North West",
		 'N':"North",
		 'O':"North East",
		 'E':"East",
		 'U':"South East",
		 'S':"South",
		 'T':"South West",
		 'W':"West" }

#List comprehension that merges the strings
print len(sys.argv)
if len(sys.argv) == 1:
	Input = "Nicolas Cage"
else:
	Input = ''.join([arg for arg in sys.argv[1:]])
Input =  filter(str.isalpha, Input).lower()

# No X or Q
Key = { 'a':(1,"H"), 'b':(1,"N"), 'c':(1,"O"), 'd':(1,"E"), 'e':(1,"U"), 'f':(1,"S"), 'g':(1,"T"), 'h':(1,"W"), 
        'i':(2,"H"), 'j':(2,"N"), 'k':(2,"O"), 'l':(2,"E"), 'm':(2,"U"), 'n':(2,"S"), 'o':(2,"T"), 'p':(2,"W"), 
        'r':(3,"H"), 's':(3,"N"), 't':(3,"O"), 'u':(3,"E"), 'v':(3,"U"), 'w':(3,"S"), 'x':(3,"T"), 'y':(3,"W") } 

def Move(Start, Letter):
	x = Start[0]
	y = Start[1]
	magnitude = Key[Letter][0] * Scale
	direction = Key[Letter][1]
	print "Starting at " + str(x) + "," + str(y)
	print "Moving in direction " + str(direction) + " with a mag of " + str(magnitude)
	
	x = {
	  'H': lambda x: x - magnitude,
	  'N': lambda x: x,
	  'O': lambda x: x + magnitude,
	  'E': lambda x: x + magnitude,
	  'U': lambda x: x + magnitude,
	  'S': lambda x: x,
	  'T': lambda x: x - magnitude,
	  'W': lambda x: x - magnitude
	}[direction](x)

	y = {
	  'H': lambda y: y + magnitude,
	  'N': lambda y: y + magnitude,
	  'O': lambda y: y + magnitude,
	  'E': lambda y: y,
	  'U': lambda y: y - magnitude,
	  'S': lambda y: y - magnitude,
	  'T': lambda y: y - magnitude,
	  'W': lambda y: y
	}[direction](y)
	print "Now at " + str(x) + "," + str(y)
	if Key[Letter][0] == 1:
		return ((x,y),)
	if Key[Letter][0] == 2:
		midx = (Start[0] + x) / 2
		midy = (Start[1] + y) / 2
		return ((midx,midy),(x,y))
	if Key[Letter][0] == 3:
		midx1 = Start[0] + ((x-Start[0])/3)
		midy1 = Start[1] + ((y-Start[1])/3)
		midx2 = Start[0] + (2*(x-Start[0])/3)
		midy2 = Start[1] + (2*(y-Start[1])/3)
		return ((midx1,midy1),(midx2,midy2),(x,y))

def autocrop(im, bgcolor):
    if im.mode != "RGB":
        im = im.convert("RGB")
    bg = Image.new("RGB", im.size, bgcolor)
    diff = ImageChops.difference(im, bg)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    return None # no contents


Position = (Scale*10,Scale*10)
StartingPosition = (Scale*10,Scale*10)
im = Image.new("L",(Scale*20,Scale*20),"White")
draw = ImageDraw.Draw(im)
for Letter in Input:
	print "I'm at " + str(Position) + "  Doing letter: " + str(Letter)
	OldPosition = Position
	print str(Move(Position,Letter))
	for Position in Move(Position,Letter):
		if Key[Letter][1] == 'N' or Key[Letter][1] == 'E' or Key[Letter][1] == 'S' or Key[Letter][1] == 'W':
			linewidth = Scale/8
		else:
			linewidth = Scale/10
		draw.line((OldPosition,Position), fill=50, width=linewidth)
		draw.ellipse(( (Position[0]-Scale/5,Position[1]-Scale/5),(Position[0]+Scale/5,Position[1]+Scale/5)    ), fill=50)
		OldPosition = Position

draw.ellipse(( (StartingPosition[0]-Scale/5,StartingPosition[1]-Scale/5),(StartingPosition[0]+Scale/5,StartingPosition[1]+Scale/5)    ), fill=200)
del draw
im = im.transpose(Image.FLIP_TOP_BOTTOM)
im = autocrop(im,"White")
im.show()
	
