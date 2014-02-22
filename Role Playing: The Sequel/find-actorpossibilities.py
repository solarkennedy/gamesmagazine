#!/usr/bin/env python
import MySQLdb
import os.path

if os.path.exists('actorpossibilties.py'):
	print "actorpossibilties.py already exisits. Delete it and rerun this program if you need fresh data"
	exit(0)

#Did you import the imdb into your mysql using imdbpy ?
dbhost = 'localhost'
dbuser = 'imdb'
dbpass = 'imdb'
dbname = 'imdb'
db = MySQLdb.connect(host=dbhost, user=dbuser, passwd=dbpass,db=dbname)
cursor = db.cursor(MySQLdb.cursors.DictCursor)


class actorclass:
   """ Class for the holding the actor's name and what movies he or she has been in """
   possibilities = {}
   name = ""
   movies = {}
   links = ()
   regex = ""
class movieclass:
   """ Class for storing movie info """
   possibilities = {}

movie = []
for x in range(0,4):
   movie.append(movieclass())

actor = []
for x in range(0,4):
   actor.append(actorclass())

#The example diagram they give is first, last but the imdb data is last,first

#Original hints
actor[0].regex = '^[^- ,]{7}, [^- ,]{5}( |$)'
actor[0].links = ( movie[1], movie[0] )
actor[1].regex = '^[^- ,]{10}, [^- ,]{6}( |$)'
actor[1].links = ( movie[1], movie[2] )
actor[2].regex = '^[^- ,]{3}, [^- ,]{7}( |$)'
actor[2].links = ( movie[2], movie[3] )
actor[3].regex = '^[^- ,]{11}, [^- ,]{8}( |$)'
actor[3].links = ( movie[3], movie[0] )

def howmanymoviestheyhavebeenin(id):
        cursor.execute("SELECT `movie_id` FROM `cast_info`, `title` WHERE `person_id` = '%s' AND title.id = cast_info.movie_id AND title.production_year >= 2000 AND title.production_year <= 2010 AND title.kind_id = 1 AND (role_id = 1 OR role_id = 2) AND (cast_info.note != '(uncredited)'  OR cast_info.note IS NULL)" % (id))
        SqlResults = cursor.fetchall()
        movielist = [mov['movie_id'] for mov in SqlResults]
        return len(movielist)


# Populate all possible actor names based on regex
for x in range(len(actor)):
        print "Finding possible actors for node " + str(x)
        print "   regex: " + actor[x].regex
        cursor.execute("SELECT id FROM `name` WHERE `name` REGEXP '%s'" % actor[x].regex )
        print "Number of possible actors: %d" % cursor.rowcount
        results = cursor.fetchall()
	#Turn this dictionary into a tuple
        actors = [persons['id'] for persons in results]


	# list comprehension to return a list of those actors who have been in links movies or more
	actors1 = tuple([i for i in actors if howmanymoviestheyhavebeenin(i) >= len(actor[x].links)])
	print " - who have been in at least " +str(len(actor[x].links)) + " movies in the last century: " + str(len(actors1))
	
	actors2 = []
	for act in actors1:
		#No no-name actors plz
	        cursor.execute("SELECT * FROM `person_info` WHERE `person_id` = '%s' " % act)
		if cursor.rowcount > 0:
        		actors2.append(act)
        print " - who have person_info: " + str(len(actors2))



#Now lets go for the middle
cursor.execute("SELECT `id` FROM `name` WHERE 1")
SqlResults = cursor.fetchall()
everyactorlist = [x['id'] for x in SqlResults]
possibilities = []

print "And finally for the center - "
print "Finding possible actors for node 8"
print "Number of possible actors: %d" % cursor.rowcount

for act in everyactorlist:
        #Lets take each actor/actress and find those that fit our criterea
        cursor.execute("SELECT `movie_id` FROM `cast_info`, `title` WHERE `person_id` = '%s' AND title.id = cast_info.movie_id AND title.production_year >= 2000 AND title.production_year <= 2010 AND title.kind_id = 1 AND cast_info.role_id = '2' AND  ( cast_info.note != '(uncredited)'  OR cast_info.note IS NULL) " % act)
        results = cursor.fetchall()
        movielist = [mov['movie_id'] for mov in results]
        if len(movielist) >= 13:
		#We don't want no no-name actors with no info
        	cursor.execute("SELECT * FROM `person_info` WHERE `person_id` = '%s' " % act)
        	if cursor.rowcount > 0:
                	possibilities.append(act)

#Populate the file to make it faster
f = open('actorpossibilities.py','w')
for x in range(len(actor)):
	f.write("actor[" + str(x)  +  "].possibilities = " + str(actor[x].possibilities) )
	f.write("\n")
f.close()
print "actorpossibilities.py has been populated with this data."
