#!/usr/bin/env python
import os.path
import pickle
import imdb_lib
import puzzle_lib
import sqlite3
import re
import sys

def regexp(expr, item):
    reg = re.compile(expr)
    return reg.search(item) is not None

def get_actor_list(cursor):
    if os.path.isfile('actor_possibilities.p'):
        print "Using cached actor possibitilties file."
        actors = pickle.load( open('actor_possibilities.p', 'r') )
    else:
        actors = puzzle_lib.setup_actors()
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
        movies = puzzle_lib.setup_movies()
        for movie in movies:
            print "Finding possible movies for node " + str(movie.node)
            print "   regex: " + movie.regex
            results = imdb_lib.search_movies(cursor, movie.regex)
            movie.possibilities = results
        print "Dumping movies into a file"
        pickle.dump( movies, open('movie_possibilities.p', 'wb') )

def main():
    conn = sqlite3.connect('imdb.db')
    conn.create_function("REGEXP", 2, regexp)
    cursor = conn.cursor()
    
    actors = get_actor_list(cursor)
    movies = get_movie_list(cursor)

if __name__ == '__main__':
    main()
