#!/usr/bin/env python
# Role Playing 4 Solver
# Kyle Anderson 2010
# Under the AGPL 3

import MySQLdb
import copy
import os


#Did you import the imdb into your mysql using imdbpy ?
dbhost = 'localhost'
dbuser = 'imdb'
dbpass = 'imdb'
dbname = 'imdb'
db = MySQLdb.connect(host=dbhost, user=dbuser, passwd=dbpass,db=dbname)
cursor = db.cursor(MySQLdb.cursors.DictCursor)

# Generate the blacklist of awards shows, they come up as TV movies:
cursor.execute("SELECT id FROM `title` WHERE `title` LIKE '%Awards%'")
SqlResults = cursor.fetchall()
blacklist = list(set([mov['id'] for mov in SqlResults]))

class actorclass:
   """ Class for the holding the actor's name and what movies he or she has been in """
   possibilities = ()
   links = ()
   regex = ""
actor = []
for x in range(9):
   actor.append(actorclass())

class movieclass:
   """ Class for storing movie info """
   possibilities = []
   name = ""
movie = []
for x in range(13):
   movie.append(movieclass())
   movie[x].name = x

#The example diagram they give is first, last but the imdb data is last,first
#Question marks stand for 3,4,6, or 9
# Gener in the imdb, 1 is male and 2 is female
actor[0].regex = '^(([^- ,]{3})|([^- ,]{4})|([^- ,]{6})|([^- ,]{9})), [^- ,]{5} '
actor[0].links = ( movie[12], movie[1] )
actor[0].gender= 2
actor[1].regex = '^(([^- ,]{3})|([^- ,]{4})|([^- ,]{6})|([^- ,]{9})), [^- ,]{5} '
actor[1].links = ( movie[0], movie[1] )
actor[1].gender= 1
actor[2].regex = '^[^- ,]{8}, (([^- ,]{3})|([^- ,]{4})|([^- ,]{6})|([^- ,]{9})) '
actor[2].links = ( movie[1], movie[2] )
actor[2].gender= 1
actor[3].regex = '^(([^- ,]{3})|([^- ,]{4})|([^- ,]{6})|([^- ,]{9})), [^- ,]{7} '
actor[3].links = ( movie[3], movie[4] )
actor[3].gender= 2
actor[4].regex = '^[^- ,]{7}, (([^- ,]{3})|([^- ,]{4})|([^- ,]{6})|([^- ,]{9})) '
actor[4].links = ( movie[5], movie[6], movie[7] )
actor[4].gender= 2
actor[5].regex = '^[^- ,]{7}, [^- ,]{7} '
actor[5].links = ( movie[7], movie[8] )
actor[5].gender= 2
actor[6].regex = '^(([^- ,]{3})|([^- ,]{4})|([^- ,]{6})|([^- ,]{9})), [^- ,]{7} '
actor[6].links = ( movie[9], movie[10] )
actor[6].gender= 1
actor[7].regex = '^[^- ,]{7}, (([^- ,]{3})|([^- ,]{4})|([^- ,]{6})|([^- ,]{9})) '
actor[7].links = ( movie[11], movie[12] )
actor[7].gender= 2
actor[8].links = ( movie[0],  movie[1], movie[2], movie[3], movie[4], movie[5], movie[6], movie[7], movie[8], movie[9], movie[10], movie[11], movie[12] )
actor[8].gender = 2

# For speed, we have the actor lists prepopulated in this file
try:
	execfile("actorpossibilities.py")
except:
	print "Did you run find-actorpossibilities.py?"
	exit()

def actorname(id):
        cursor.execute("SELECT `name` FROM `name` WHERE `id` = '%s'" % (id))
        Results = cursor.fetchall()
	return Results[0]['name']
def moviename(id):
        cursor.execute("SELECT `title` FROM `title` WHERE `id` = '%s'" % (id))
        Results = cursor.fetchall()
        return Results[0]['title']
def movielist(id):
        cursor.execute("SELECT `movie_id` FROM `cast_info`, `title` WHERE `person_id` = '%s' AND title.id = cast_info.movie_id AND title.production_year >= 2000 AND title.production_year <= 2010 AND title.kind_id = '1' AND (role_id = 1 OR role_id = 2 AND (cast_info.note != '(uncredited)'  OR cast_info.note IS NULL))" % (id) )
        SqlResults = cursor.fetchall()
        return list(set([mov['movie_id'] for mov in SqlResults]))
def gender(id):
	cursor.execute("SELECT `role_id` FROM `cast_info`,`title` WHERE `person_id` = '%s' AND title.id = cast_info.movie_id AND title.production_year >= 2000 AND title.production_year <= 2010 AND title.kind_id = '1'  AND (role_id = 1 OR role_id = 2)" % (id) )
        Results = cursor.fetchall()
        return Results[0]['role_id']
def moviesincommon(actor1, actor2):
        movielist1 = movielist(actor1)
        movielist2 = movielist(actor2)
	commonmovies = list(set(movielist1).intersection(set(movielist2)) )
	return [i for i in commonmovies if i not in blacklist ]
def moviesincommon3(actor1, actor2, actor3):
        movielist1 = movielist(actor1)
        movielist2 = movielist(actor2)
        movielist3 = movielist(actor3)
        commonmovies = list(  set(movielist1).intersection(  set(movielist2).intersection(set(movielist3))         ) )
        return [i for i in commonmovies if i not in blacklist ]
def moviesincommon4(actor1, actor2, actor3, actor4):
        movielist1 = movielist(actor1)
        movielist2 = movielist(actor2)
        movielist3 = movielist(actor3)
        movielist4 = movielist(actor4)
        commonmovies = list(  set(movielist1).intersection(  set(movielist2).intersection( set(movielist3).intersection(set(movielist4))   )         ) )
        return [i for i in commonmovies if i not in blacklist ]
def moviestheyhavebeenin(actor):
        cursor.execute("SELECT `movie_id` FROM `cast_info`, `title` WHERE `person_id` = '%s' AND title.id = cast_info.movie_id AND title.production_year >= 2000 AND title.production_year <= 2010 AND title.kind_id = '1' AND (role_id = 1 OR role_id = 2)" % (actor) )
        SqlResults = cursor.fetchall()
        # We have a tuple of dictionaries from our mysql, but we just want a big tuple:
        return list(set([mov['movie_id'] for mov in SqlResults]))

# Our main recursive function, checks to see if we have common movies at junction points 2,3,6,8
def recurse(level, centeractress, placedactors):
	if level == 2:
		if len(moviesincommon3(placedactors[0], placedactors[1], centeractress)) < 1:
			return
	elif level == 3:
		if len(moviesincommon4(placedactors[0], placedactors[1], placedactors[2], centeractress)) < 1:
			return
	elif level == 6:
		if len(moviesincommon3(placedactors[4], placedactors[5], centeractress)) < 1:
			return
	elif level == 8:
                if len(moviesincommon3(placedactors[0], placedactors[7], centeractress)) < 1:
                        return
		else:
			print "I HAZ A SOLUTION:"
			print [actorname(i) for i in placedactors]
			print placedactors
			return

	for possibleactor in actor[level].possibilities:
		if possibleactor not in placedactors + [centeractress]:
			sharedmovies = moviesincommon(centeractress, possibleactor)
			if len(sharedmovies) >= len(actor[level].links):
				recurse(level+1, centeractress, copy.copy(placedactors + [possibleactor]))
	

#print "Going through " + str(len( actor[8].possibilities)) + " actresses for the center"
#for actress in actor[8].possibilities:
#	#Go through each actress and try to fit it into the puzzle
#	placedactors = []
#	placedmovies = []
#	print "We are recursing with " + actorname(actress) + " (" + str(actress) + ")"
#	recurse(0, actress, copy.copy(placedactors) )
