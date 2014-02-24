#!/usr/bin/env python
import os.path
import pickle
import imdb_lib
import puzzle_lib
import sqlite3


db = sqlite3.connect('imdb.db')
cursor = db.cursor()

#if os.path.exists('movie_possibilities.py'):
#    print "movie_possibilities.py already exisits. Delete it and rerun this program if you need fresh data"
#    exit(0)

movies = puzzle_lib.setup_movies()

for movie in movies:
        print "Finding possible movies for node " + str(movie.node)
        print "   regex: " + movie.regex
        results = imdb_lib.search_movies(cursor, movie.regex)
        movie.possibilities = results
print movies

#Populate the file to make it faster
#f = open('movie_possibilities.py','w')
#for x in range(len(movies)):
#	f.write("movie[" + str(x)  +  "].possibilities = " + str(movie[x].possibilities) )
#	f.write("\n")
#f.close()
#print "movie_possibilties.py has been populated with this data."
#
