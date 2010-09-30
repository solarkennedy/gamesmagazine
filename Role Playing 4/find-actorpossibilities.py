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
for x in range(13):
   movie.append(movieclass())

actor = []
for x in range(9):
   actor.append(actorclass())

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

def gender(id):
        cursor.execute("SELECT `role_id` FROM `cast_info`,`title` WHERE `person_id` = '%s' AND title.id = cast_info.movie_id AND title.production_year >= 2000 AND title.production_year <= 2010 AND (title.kind_id = '1' OR title.kind_id = '3') AND (role_id = 1 OR role_id = 2)" % (id) )
        Results = cursor.fetchall()
        return Results[0]['role_id']

def howmanymoviestheyhavebeenin(id):
        cursor.execute("SELECT `movie_id` FROM `cast_info`, `title` WHERE `person_id` = '%s' AND title.id = cast_info.movie_id AND title.production_year >= 2000 AND title.production_year <= 2010 AND (title.kind_id = 1 OR title.kind_id = '3') AND (role_id = 1 OR role_id = 2) AND cast_info.note != `(uncredited)`" % (id))
        SqlResults = cursor.fetchall()
        movielist = [mov['movie_id'] for mov in SqlResults]
        return len(movielist)


# Populate all possible actor names based on regex
for x in range(8):
        print "Finding possible actors for node " + str(x)
        print "   regex: " + actor[x].regex
        cursor.execute("SELECT id FROM `name` WHERE `name` REGEXP '%s'" % actor[x].regex )
        print "Number of possible actors: %d" % cursor.rowcount
        results = cursor.fetchall()
	#Turn this dictionary into a tuple
        actors = tuple([persons['id'] for persons in results])

	# list comprehension to return a list of those actors who have been in links movies or more
	actors1 = tuple([i for i in actors if howmanymoviestheyhavebeenin(i) >= len(actor[x].links)])
	print " - who have been in at least " +str(len(actor[x].links)) + " movies in the last century: " + str(len(actors1))

	# List comprehension to make a list only containing the gender we need
	actor[x].possibilities = [i for i in actors1 if gender(i) == actor[x].gender]
        print " - who are of gender " + str(actor[x].gender) + ": " + str(len(actor[x].possibilities))
	


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
        cursor.execute("SELECT `movie_id` FROM `cast_info`, `title` WHERE `person_id` = '%s' AND title.id = cast_info.movie_id AND title.production_year >= 2000 AND title.production_year <= 2010 AND (title.kind_id = 1 OR title.kind_id = '3') AND cast_info.role_id = '2' AND  cast_info.note != `(uncredited)`" % act)
        results = cursor.fetchall()
        movielist = [mov['movie_id'] for mov in results]
        if len(movielist) >= 13:
                possibilities.append(act)
actor[8].possibilities = possibilities
print " - Number that are female with more than 12 movies: " + str(len(actor[8].possibilities))

#Populate the file to make it faster
f = open('actorpossibilities.py','w')
for x in range(9):
	f.write("actor[" + str(x)  +  "].possibilities = " + str(actor[x].possibilities) )
	f.write("\n")
f.close()
print "actorpossibilities.py has been populated with this data."

