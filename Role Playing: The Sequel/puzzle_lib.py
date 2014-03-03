#!/usr/bin/env python
import os
import pickle
import imdb_lib

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
    actors[4].hint  = ( 5, 9 )
    actors[5].hint  = ( 5, 5 )
    actors[6].hint  = ( 4, 8 )
    actors[7].hint  = ( 7, 10 )
    actors[8].hint  = ( 4, 3 )
    actors[9].hint  = ( 4, 5 )
    actors[10].hint = ( 8, 9 )
    actors[11].hint = ( 6, 4 )
    actors[12].hint = ( 8, 8 )
    actors[13].hint = ( 8, 6 )
    actors[14].hint = ( 5, 9 )
    actors[15].hint = ( 9, 4 )
    # links represent which movies the actor is in
    actors[0].links  = ( 0, 1 )
    actors[1].links  = ( 1, 2 )
    actors[2].links  = ( 2, 3 )
    actors[3].links  = ( 0, 3 )
    actors[4].links  = ( 4, 5 )
    actors[5].links  = ( 5, 6 )
    actors[6].links  = ( 6, 7 )
    actors[7].links  = ( 4, 7 )
    actors[8].links  = ( 8, 9 )
    actors[9].links  = ( 9, 10 )
    actors[10].links = ( 10, 11 )
    actors[11].links = ( 8, 11 )
    actors[12].links = ( 12, 13 )
    actors[13].links = ( 13, 14 )
    actors[14].links = ( 14, 15 )
    actors[15].links = ( 12, 15 )
    actors[16].links = ( 3, 4 )
    actors[17].links = ( 7, 8 )
    actors[18].links = ( 11, 12 )
    actors[19].links = ( 0, 15 )
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
    movies[0].links  = ( 0, 3, 19 )
    movies[1].links  = ( 0, 1, )
    movies[2].links  = ( 1, 2, )
    movies[3].links  = ( 2, 3, 16 )
    movies[4].links  = ( 4, 7, 16 )
    movies[5].links  = ( 4, 5, )
    movies[6].links  = ( 5, 6, )
    movies[7].links  = ( 6, 7, 17 )
    movies[8].links  = ( 8, 11, 17 )
    movies[9].links  = ( 8, 9, )
    movies[10].links = ( 9, 10, )
    movies[11].links = ( 10, 11, 18 )
    movies[12].links = ( 12, 15, 18 )
    movies[13].links = ( 12, 13, )
    movies[14].links = ( 13, 14, )
    movies[15].links = ( 14, 15, 19 )
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
   def __init__(self):
       self.possibilities = []
       self.name = ""
       self.movies = []
       self.links = ()
       self.regex = ""
       self.imdb_id = False
       self.node = False
       self.hint = False

class Movie:
   """ Class for storing movie info """
   def __init__(self):
       self.imdb_id = False
       self.links = ()
       self.possibilities = []
       self.node = False

class Board:
    """ Class for storing the state of the puzzle """
    def __init__(self):
        actors = []
        movies = []
    def is_first_pass_complete(self):
        for movie in self.movies:
            if movie.imdb_id == False:
                return False
        for actor in self.actors[0:15]:
            if movie.imdb_id == False:
                return False
        # If we got this far, our first pass is complete 
        return True
    def print_progress(self,cursor):
        for movie in self.movies:
            if movie.imdb_id:
                print "Movie Node " + str(movie.node) + " (" + str(movie.imdb_id) + "): " + imdb_lib.movie_id_to_name(cursor, movie.imdb_id)
        for actor in self.actors:
            if actor.imdb_id:
                print "Actor Node " + str(actor.node) + " (" + str(actor.imdb_id) + "): " + imdb_lib.actor_id_to_name(cursor, actor.imdb_id)
    def find_possible_movies(self, cursor, slot):
        print "  Trying to find possible movies for slot " + str(slot)
        possibilities_so_far = set(self.movies[slot].possibilities)
        print "   DEBUG: Initial Possibilties: " + str(len(possibilities_so_far))
        for link in self.movies[slot].links:
            if self.actors[link].imdb_id != False:
                possibilities_so_far = possibilities_so_far.intersection(imdb_lib.movies_actor_has_been_in(cursor, self.actors[link].imdb_id))
                for n in imdb_lib.movies_actor_has_been_in(cursor, self.actors[link].imdb_id):
                    print "    DBUG: movies " + imdb_lib.actor_id_to_name(cursor,self.actors[link].imdb_id) + " have been in: " + imdb_lib.movie_id_to_name(cursor, n) + " (" + str(n) + ")"
                for n in possibilities_so_far:
                    print "    DBUG: Slot " + str(slot) + " Narrowed down to: " + imdb_lib.movie_id_to_name(cursor, n)
        return possibilities_so_far
    def find_possible_actors(self, cursor, n):
        print "  Trying to find possible actors for slot " + str(n)
        if self.actors[n].hint == False:
            # Special Case:
            # If we don't have a hint, we must behave differently to get a list of possible actors
            for n in self.actors[n].links:
                if self.movies[n].imdb_id != False:
                    possibilities_so_far = imdb_lib.actors_in(cursor, self.movies[n].imdb_id)
        else:
            possibilities_so_far = set(self.actors[n].possibilities)
            for n in self.actors[n].links:
                print "   DEBUG: There are " + str(len(possibilities_so_far)) + " poss so far" 
                if self.movies[n].imdb_id != False:
                    possibilities_so_far = possibilities_so_far.intersection(imdb_lib.actors_in(cursor, self.movies[n].imdb_id))
                    for n in possibilities_so_far:
                        print "    DBUG: possibility: " + imdb_lib.actor_id_to_name(cursor, n)
        return possibilities_so_far

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

def get_actor_list(cursor):
    if os.path.isfile('actor_possibilities.p'):
        print "Using cached actor possibitilties file."
        actors = pickle.load( open('actor_possibilities.p', 'r') )
    else:
        actors = setup_actors()
        for n in range(16):
            print "Finding possible actor for node " + str(actors[n].node)
            print "   regex: " + actors[n].regex
            results = imdb_lib.search_actors(cursor, actors[n].regex)
            actors[n].possibilities = results
            print "   Found " + str(len(results)) + " actors that matched."
        print "Dumping actors into a file"
        pickle.dump( actors, open('actor_possibilities.p', 'wb') )
    return actors

def get_movie_list(cursor):
    if os.path.isfile('movie_possibilities.p'):
        print "Using cached movie possibitilties file."
        movies = pickle.load( open('movie_possibilities.p', 'r') )
    else:
        movies = setup_movies()
        for movie in movies:
            print "Finding possible movies for node " + str(movie.node)
            print "   regex: " + movie.regex
            results = imdb_lib.search_movies(cursor, movie.regex)
            print "   Found " + str(len(results)) + " movies that matched."
            movie.possibilities = results
        print "Dumping movies into a file"
        pickle.dump( movies, open('movie_possibilities.p', 'wb') )
    return movies
