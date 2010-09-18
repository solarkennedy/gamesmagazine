#!/usr/bin/env python

class actorclass:
   """ Class for the holding the actor's name and what movies he or she has been in """
   possibilities = []
   name = ""
   movies = []
   links = ()
   regex = ""
class movieclass:
   """ Class for storing movie info """
   possibilities = []

movie = []
for x in range(13):
   movie.append(movieclass())

actor = []
for x in range(8):
   actor.append(actorclass())

actor[0].regex = '....., '
actor[0].links = ( movie[12], movie[1] )
actor[1].regex = '....., '
actor[1].links = ( movie[0], movie[1] )
actor[2].regex = '.*,........ '
actor[2].links = ( movie[1], movie[2] )
actor[3].regex = '.......,, '
actor[3].links = ( movie[3], movie[4] )
actor[4].regex = '.*,.......'
actor[4].links = ( movie[5], movie[6], movie[7] )
actor[5].regex = '.......,.......'
actor[5].links = ( movie[7], movie[8] )
actor[6].regex = '.......,'
actor[6].links = ( movie[9], movie[10] )
actor[7].regex = '.*,.......'
actor[7].links = ( movie[11], movie[12] )

# Populate all possible actor names based on regex
for x in range(8):
	print "Finding possible actors for node " + str(x)
	print "   regex: " + actor[x].regex

# Populate movie lists
for x in range(8):
   print "Populating all movies done by actor " str(x)
   for link in actor[x].links:
      #if there are movies already
          #trim the possibile actors
      #else
          #populate the movie with possibilites
   #populate movies



