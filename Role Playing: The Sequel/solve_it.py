#!/usr/bin/env python
import os.path
import pickle
import imdb_lib
import puzzle_lib
import sqlite3
import re
import sys
import copy

def regexp(expr, item):
    reg = re.compile(expr)
    return reg.search(item) is not None

def solve_early_game(cursor, board):
    """ early_game does the first part of the puzzle, iterating over the
        parts of the board where the hints are for actors and movies """
    board.print_progress(cursor)
    for n in range(0, 16):
        if n % 4 == 0 and board.actors[n/4 + 15].imdb_id == False and n != 0:
            # Special spot. Try to fill in our missing actor to help hint future locations
            n = n/4 + 15
            #for possibility in board.find_possible_actors(cursor, n):
            #    print "   Possible actor for special slot " + str(n) + ": " + imdb_lib.actor_id_to_name(cursor, possibility)
            for possibility in board.find_possible_actors(cursor, n):
                board.actors[n].imdb_id = possibility
                solve_early_game(cursor,copy.deepcopy(board))
            return False
        elif board.movies[n].imdb_id == False:
            # Fit the board with a movie that could work
            #for possibility in board.find_possible_movies(cursor, n):
            #    print "   Possible movie for slot " + str(n) + ": " + imdb_lib.movie_id_to_name(cursor, possibility)
            for possibility in board.find_possible_movies(cursor, n):
                board.movies[n].imdb_id = possibility
                solve_early_game(cursor,copy.deepcopy(board))
            return False
        elif board.actors[n].imdb_id == False:
            # Fit the board with a potential actor
            #for possibility in board.find_possible_actors(cursor, n):
            #    print "   Possible actor for slot " + str(n) + ": " + imdb_lib.actor_id_to_name(cursor, possibility)
            for possibility in board.find_possible_actors(cursor, n):
                board.actors[n].imdb_id = possibility
                solve_early_game(cursor,copy.deepcopy(board))
            return False
    # If we got this far, it still means we didn't get to the last actor slot
    # So lets interate through all remaining actors and make sure we got it all.
    for n in range(0,20):
        if board.actors[n].imdb_id == False:
            for possibility in board.find_possible_actors(cursor, n):
                board.actors[n].imdb_id = possibility
                solve_early_game(cursor,copy.deepcopy(board))
            return False
    print "OMG!!!!!!!!!"
    print "Found a solution. Press enter when you have copied this solution"
    pickle.dump( board, open('solution_board.p', 'wb') )
    print "solution_board.p is dumped. Use graph_it.py to graph this soultion"
    raw_input()
    return True

def main():
    conn = sqlite3.connect('imdb.db')
    conn.create_function("REGEXP", 2, regexp)
    cursor = conn.cursor()
    
    board = puzzle_lib.Board()
    # A little overkill, we could do this JIT, but 
    # precomputing these makes it faster for me to 
    # iterate on the development of this solver
    board.actors = puzzle_lib.get_actor_list(cursor)
    board.movies = puzzle_lib.get_movie_list(cursor)
    # Kick us off with an empty board
    solve_early_game(cursor, board)

if __name__ == '__main__':
    main()
