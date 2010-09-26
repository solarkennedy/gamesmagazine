#!/usr/bin/env python
import MySQLdb

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
for x in range(8):
   actor.append(actorclass())

#The example diagram they give is first, last but the imdb data is last,first
#Question marks stand for 3,4,6, or 9
actor[0].regex = '^(([a-zA-Z]{3})|([a-zA-Z]{4})|([a-zA-Z]{6})|([a-zA-Z]{9})), [a-zA-Z]{5} '
actor[0].links = ( movie[12], movie[1] )
actor[1].regex = '^(([a-zA-Z]{3})|([a-zA-Z]{4})|([a-zA-Z]{6})|([a-zA-Z]{9})), [a-zA-Z]{5} '
actor[1].links = ( movie[0], movie[1] )
actor[2].regex = '^[a-zA-Z]{8}, (([a-zA-Z]{3})|([a-zA-Z]{4})|([a-zA-Z]{6})|([a-zA-Z]{9})) '
actor[2].links = ( movie[1], movie[2] )
actor[3].regex = '^(([a-zA-Z]{3})|([a-zA-Z]{4})|([a-zA-Z]{6})|([a-zA-Z]{9})), [a-zA-Z]{7} '
actor[3].links = ( movie[3], movie[4] )
actor[4].regex = '^[a-zA-Z]{7}, (([a-zA-Z]{3})|([a-zA-Z]{4})|([a-zA-Z]{6})|([a-zA-Z]{9})) '
actor[4].links = ( movie[5], movie[6], movie[7] )
actor[5].regex = '^[a-zA-Z]{7}, [a-zA-Z]{7} '
actor[5].links = ( movie[7], movie[8] )
actor[6].regex = '^(([a-zA-Z]{3})|([a-zA-Z]{4})|([a-zA-Z]{6})|([a-zA-Z]{9})), [a-zA-Z]{7} '
actor[6].links = ( movie[9], movie[10] )
actor[7].regex = '^[a-zA-Z]{7}, (([a-zA-Z]{3})|([a-zA-Z]{4})|([a-zA-Z]{6})|([a-zA-Z]{9})) '
actor[7].links = ( movie[11], movie[12] )

# Populate all possible actor names based on regex
for x in range(8):
        print "Finding possible actors for node " + str(x)
        print "   regex: " + actor[x].regex
        cursor.execute("SELECT * FROM `name` WHERE `name` REGEXP '%s'" % actor[x].regex )
        print "Number of possible actors: %d" % cursor.rowcount
        actor[x].possibilities = cursor.fetchall()
       

# Populate movie lists
for x in range(8):
        print "Populating all movies done by actor " + str(x)
        for link in actor[x].links:
                for possibility in actor[x].possibilities:
                        cursor.execute("SELECT * FROM `cast_info` WHERE `person_id` = '%s'" % possibility )
                        print "This actor was in movies: %d" % cursor.rowcount
                        link.possibilities.extend(cursor.fetchall())

      #if there are movies already
          #trim the possibile actors
      #else
          #populate the movie with possibilites
   #populate movies

