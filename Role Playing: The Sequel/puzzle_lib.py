#!/usr/bin/env python

def setup_actors():
    actors = []
    for n in range(20):
        actor = Actor()
        actor.node = n
        actors.append(actor)
    # Hints are given in the puzzle, number of letters in the first name,
    # number of letters in the second name
    actors[0].hint  = ( 5, 7 )
    actors[1].hint  = ( 6, 10 )
    actors[2].hint  = ( 7, 8 )
    actors[3].hint  = ( 8, 11 )
    actors[4].hint  = ( 7, 10 )
    actors[5].hint  = ( 5, 9 )
    actors[6].hint  = ( 5, 5 )
    actors[7].hint  = ( 4, 8 )
    actors[8].hint  = ( 6, 4 )
    actors[9].hint  = ( 4, 3 )
    actors[10].hint = ( 4, 5 )
    actors[11].hint = ( 8, 9 )
    actors[12].hint = ( 9, 4 )
    actors[13].hint = ( 8, 8 )
    actors[14].hint = ( 8, 6 )
    actors[15].hint = ( 5, 9 )
    # links represent which movies the actor is in
    actors[0].links  = ( 0, 1 )
    actors[1].links  = ( 1, 2 )
    actors[2].links  = ( 2, 3 )
    actors[3].links  = ( 0, 3 )
    actors[4].links  = ( 4, 7 )
    actors[5].links  = ( 4, 5 )
    actors[6].links  = ( 5, 6 )
    actors[7].links  = ( 6, 7 )
    actors[8].links  = ( 8, 11 )
    actors[9].links  = ( 8, 9 )
    actors[10].links = ( 9, 10 )
    actors[11].links = ( 10, 11 )
    actors[12].links = ( 12, 15 )
    actors[13].links = ( 12, 13 )
    actors[14].links = ( 13, 14 )
    actors[15].links = ( 14, 15 )
    actors[16].links = ( 0, 15 )
    actors[17].links = ( 3, 4 )
    actors[18].links = ( 7, 8 )
    actors[19].links = ( 11, 2 )
    for n in range(16):
        #The example diagram they give is first, last but the imdb data is last,first
        actors[n].regex = '^[^- ,]{' + str(actors[n].hint[1]) + '}, [^- ,]{' + str(actors[n].hint[0]) +  '}( |$)'
    return actors

def setup_movies():
    movies = []
    for n in range(16):
       movie = Movie()
       movie.node = n
       movies.append(movie)
    # Hints describe the letters of each word in the title 
    # of a movie
    movies[0].hint  = ( 4, 4, 4, 8 )
    movies[1].hint  = ( 6, 6 )
    movies[2].hint  = ( 4, 6 )
    movies[3].hint  = ( 9, )
    movies[4].hint  = ( 1, 9, 6 )
    movies[5].hint  = ( 7, 8 )
    movies[6].hint  = ( 3, 10 )
    movies[7].hint  = ( 7, )
    movies[8].hint  = ( 4, 7 )
    movies[9].hint  = ( 9, )
    movies[10].hint = ( 2, 6, 1, 3 )
    movies[11].hint = ( 3, )
    movies[12].hint = ( 8, 6 )
    movies[13].hint = ( 3, 7, 5 )
    movies[14].hint = ( 12, )
    movies[15].hint = ( 3, 2, 3, 7 )
    # Links describe the actors that are in them
    movies[0].links  = ( 0, 3, 16 )
    movies[1].links  = ( 0, 1, )
    movies[2].links  = ( 1, 2, )
    movies[3].links  = ( 2, 3, 17 )
    movies[4].links  = ( 5, 4, 17 )
    movies[5].links  = ( 5, 6, )
    movies[6].links  = ( 6, 7, )
    movies[7].links  = ( 4, 7, 18 )
    movies[8].links  = ( 8, 9, 18 )
    movies[9].links  = ( 9, 10, )
    movies[10].links = ( 10, 11, )
    movies[11].links = ( 8, 11, 19 )
    movies[12].links = ( 12, 13, 19 )
    movies[13].links = ( 13, 14, )
    movies[14].links = ( 14, 15, )
    movies[15].links = ( 12, 15, 16 )
    for n in range(16):
       movie_regexes = []
       for hint in movies[n].hint:
           regex = '[^- ,]{' + str(hint) + '}'
           movie_regexes += [ regex ]
       regex = '^' + ' '.join(movie_regexes) + '$'
       movies[n].regex = regex
    return movies


class Actor:
   """ Class for the holding the actor's name and what movies he or she has been in """
   possibilities = {}
   name = ""
   movies = {}
   links = ()
   regex = ""
   imdb_id =  False
   node = False
   hint = False

class Movie:
   """ Class for storing movie info """
   imdb_id = False
   possibilities = {}
   node = False



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
