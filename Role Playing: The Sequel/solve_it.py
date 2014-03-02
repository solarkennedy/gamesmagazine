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

def main():
    conn = sqlite3.connect('imdb.db')
    conn.create_function("REGEXP", 2, regexp)
    cursor = conn.cursor()
    
    # A little overkill, we could do this JIT, but 
    # precomputing these makes it faster for me to 
    # iterate on the development of this solver
    actors = puzzle_lib.get_actor_list(cursor)
    movies = puzzle_lib.get_movie_list(cursor)

if __name__ == '__main__':
    main()
