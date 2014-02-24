#!/usr/bin/env python

actor_hints = {}
actor_hints[0]   = ( 5, 7 )
actor_hints[1]   = ( 6, 10 )
actor_hints[2]   = ( 7, 8 )
actor_hints[3]   = ( 8, 11 )
actor_hints[4]   = ( 7, 10 )
actor_hints[5]   = ( 5, 9 )
actor_hints[6]   = ( 5, 5 )
actor_hints[7]   = ( 4, 8 )
actor_hints[8]   = ( 6, 4 )
actor_hints[9]   = ( 4, 3 )
actor_hints[10]  = ( 4, 5 )
actor_hints[11]  = ( 8, 9 )
actor_hints[12]  = ( 9, 4 )
actor_hints[13]  = ( 8, 8 )
actor_hints[14]  = ( 8, 6 )
actor_hints[15]  = ( 5, 9 )

movie_hints = {}
movie_hints[0]  = ( 4, 4, 4, 8 )
movie_hints[1]  = ( 6, 6 )
movie_hints[2]  = ( 4, 6 )
movie_hints[3]  = ( 9, )
movie_hints[4]  = ( 1, 9, 6 )
movie_hints[5]  = ( 7, 8 )
movie_hints[6]  = ( 3, 10 )
movie_hints[7]  = ( 7, )
movie_hints[8]  = ( 4, 7 )
movie_hints[9]  = ( 9, )
movie_hints[10] = ( 2, 6, 1, 3 )
movie_hints[11] = ( 3, )
movie_hints[12] = ( 8, 6 )
movie_hints[13] = ( 3, 7, 5 )
movie_hints[14] = ( 12, )
movie_hints[15] = ( 3, 2, 3, 7 )

class Actor:
   """ Class for the holding the actor's name and what movies he or she has been in """
   possibilities = {}
   name = ""
   movies = {}
   links = ()
   regex = ""
   imdb_id =  False
   node = False

class Movie:
   """ Class for storing movie info """
   imdb_id = False
   possibilities = {}
   node = False

def setup_actors():
    actors = []
    for n in range(len(actor_hints)):
        actor = Actor()
        actor_hint = actor_hints[n]
        #The example diagram they give is first, last but the imdb data is last,first
        actor.regex = '^[^- ,]{' + str(actor_hint[1]) + '}, [^- ,]{' + str(actor_hint[0]) +  '}( |$)'
        actor.node = n
        actors.append(actor)
    return actors

def setup_movies():
    movies = []
    for n in range(len(movie_hints)):
       print "working on movie " + str(n)
       movie = Movie() 
       regex = '^'
       for hint in movie_hints[n]:
           regex += '}, [^- ,]{' + str(hint) + '}'
       regex += '$'
       print "Regex for it: " + regex
       movie.regex = regex
       movie.node = n
       movies.append(movie)
    return movies

def filter_results(cursor, actors):
    # list comprehension to return a list of those actors who have been in 2 movies or more
    filtred1 = tuple([i for i in actors if imdb_lib.howmanymoviestheyhavebeenin(cursor, i) >= 2])
    print " - who have been in at least 2 movies in the last century: " + str(len(filtered1))
    actors2 = []
    for act in actors1:
            #No no-name actors plz
            cursor.execute("SELECT * FROM `person_info` WHERE `person_id` = '%s' " % act)
            if cursor.rowcount > 0:
                    actors2.append(act)
    print " - who have person_info: " + str(len(actors2))
    return actors2
