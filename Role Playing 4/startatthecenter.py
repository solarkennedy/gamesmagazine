#!/usr/bin/env python
# Role Playing 4 Solver
# Kyle Anderson 2010
# Under the AGPL 3

import MySQLdb
import copy

#Did you import the imdb into your mysql using imdbpy ?
dbhost = 'localhost'
dbuser = 'imdb'
dbpass = 'imdb'
dbname = 'imdb'
db = MySQLdb.connect(host=dbhost, user=dbuser, passwd=dbpass,db=dbname)
cursor = db.cursor(MySQLdb.cursors.DictCursor)


class actorclass:
   """ Class for the holding the actor's name and what movies he or she has been in """
   possibilities = ()
   movies = []
   links = ()
   regex = ""
   name = ""
   coworkers = []
class movieclass:
   """ Class for storing movie info """
   possibilities = []
   name = ""

movie = []
for x in range(13):
   movie.append(movieclass())
   movie[x].name = x

actor = []
for x in range(9):
   actor.append(actorclass())


#The example diagram they give is first, last but the imdb data is last,first
#Question marks stand for 3,4,6, or 9
# Gener in the imdb, 1 is male and 2 is female
actor[0].regex = '^(([a-zA-Z]{3})|([a-zA-Z]{4})|([a-zA-Z]{6})|([a-zA-Z]{9})), [a-zA-Z]{5} '
actor[0].links = ( movie[12], movie[1] )
actor[0].gender= 2
actor[1].regex = '^(([a-zA-Z]{3})|([a-zA-Z]{4})|([a-zA-Z]{6})|([a-zA-Z]{9})), [a-zA-Z]{5} '
actor[1].links = ( movie[0], movie[1] )
actor[1].gender= 1
actor[2].regex = '^[a-zA-Z]{8}, (([a-zA-Z]{3})|([a-zA-Z]{4})|([a-zA-Z]{6})|([a-zA-Z]{9})) '
actor[2].links = ( movie[1], movie[2] )
actor[2].gender= 1
actor[3].regex = '^(([a-zA-Z]{3})|([a-zA-Z]{4})|([a-zA-Z]{6})|([a-zA-Z]{9})), [a-zA-Z]{7} '
actor[3].links = ( movie[3], movie[4] )
actor[3].gender= 2
actor[4].regex = '^[a-zA-Z]{7}, (([a-zA-Z]{3})|([a-zA-Z]{4})|([a-zA-Z]{6})|([a-zA-Z]{9})) '
actor[4].links = ( movie[5], movie[6], movie[7] )
actor[4].gender= 2
actor[5].regex = '^[a-zA-Z]{7}, [a-zA-Z]{7} '
actor[5].links = ( movie[7], movie[8] )
actor[5].gender= 2
actor[6].regex = '^(([a-zA-Z]{3})|([a-zA-Z]{4})|([a-zA-Z]{6})|([a-zA-Z]{9})), [a-zA-Z]{7} '
actor[6].links = ( movie[9], movie[10] )
actor[6].gender= 1
actor[7].regex = '^[a-zA-Z]{7}, (([a-zA-Z]{3})|([a-zA-Z]{4})|([a-zA-Z]{6})|([a-zA-Z]{9})) '
actor[7].links = ( movie[11], movie[12] )
actor[7].gender= 2

# For speed, we have the actor lists prepopulated in this file
execfile("actorpossibilities.py")

#By doing some sql, we have a list of movies for node 9
actor[8].possibilities = actresseswithmorethan12
actor[8].gender = 2
actor[8].links = ( movie[0],  movie[1], movie[2], movie[3], movie[4], movie[5], movie[6], movie[7], movie[8], movie[9], movie[10], movie[11], movie[12] )

def actorname(id):
        cursor.execute("SELECT `name` FROM `name` WHERE `id` = '%s'" % (id))
        Results = cursor.fetchall()
	return Results[0]['name']
def gender(id):
	cursor.execute("SELECT `role_id` FROM `cast_info`,`title` WHERE `person_id` = '%s' AND title.id = cast_info.movie_id AND title.production_year >= 2000 AND title.production_year <= 2010 AND title.kind_id = '1' AND (role_id = 1 OR role_id = 2)" % (id) )
        Results = cursor.fetchall()
        return Results[0]['role_id']

def isthereanactressinthislist(thelist):
	for a in thelist:
		if gender(a) == 2:
			return True
	return False
def moviesincommon(actor1, actor2):
	cursor.execute("SELECT `movie_id` FROM `cast_info`, `title` WHERE `person_id` = '%s' AND title.id = cast_info.movie_id AND title.production_year >= 2000 AND title.production_year <= 2010 AND title.kind_id = '1' AND (role_id = 1 OR role_id = 2)" % (actor1) )
        SqlResults = cursor.fetchall()
        movielist1 = list(set([mov['movie_id'] for mov in SqlResults]))
        cursor.execute("SELECT `movie_id` FROM `cast_info`, `title` WHERE `person_id` = '%s' AND title.id = cast_info.movie_id AND title.production_year >= 2000 AND title.production_year <= 2010 AND title.kind_id = '1' AND (role_id = 1 OR role_id = 2)" % (actor2) )
        SqlResults = cursor.fetchall()
        movielist2 = list(set([mov['movie_id'] for mov in SqlResults]))
	return tuple( set(movielist1).intersection(set(movielist2)) )

def moviestheyhavebeenin(actor):
        cursor.execute("SELECT `movie_id` FROM `cast_info`, `title` WHERE `person_id` = '%s' AND title.id = cast_info.movie_id AND title.production_year >= 2000 AND title.production_year <= 2010 AND title.kind_id = '1' AND (role_id = 1 OR role_id = 2)" % (actor) )
        SqlResults = cursor.fetchall()
        # We have a tuple of dictionaries from our mysql, but we just want a big tuple:
        return list(set([mov['movie_id'] for mov in SqlResults]))



def recurse(level, centeractress, placedactors):
#def recurse(level, centeractress, placedactors, placedmovies):
	if level == 8:
		print "We have reached the end:"
		print placedactors

	for possibleactor in actor[level].possibilities:
		sharedmovies = moviesincommon(centeractress, possibleactor)
		if len(sharedmovies) >= len(actor[level].links):
			#We have a move in common
			recurse(level+1, centeractress, copy.copy(placedactors.append(possibleactor)))
	

print "Going through " + str(len( actor[8].possibilities) + " actresses for the center"
for actress in actor[8].possibilities:
	#Go through each actress and try to fit it into the puzzle
	placedactors = []
	placedmovies = []
	print "We are recursing with " + actorname(actress) + " (" + str(actress) + ")"
	recurse(0, centeractress, copy.copy(placedactors) )
	#recurse(0, centeractress, copy.copy(placedactors), copy.copy(placedmovies) )

