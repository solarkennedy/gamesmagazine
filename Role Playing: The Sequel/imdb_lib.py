#!/usr/bin/env python

import copy
import os
import sqlite3
import re

def re_fn(expr, item):
    reg = re.compile(expr, re.I)
    return reg.search(item) is not None
    
def connect():
    conn = sqlite3.connect('imdb.db')
    conn.create_function("REGEXP", 2, re_fn)
    cursor = conn.cursor()
    return cursor

def blacklist(cursor):
    # Generate the blacklist of awards shows, they come up as TV movies:
    cursor.execute("SELECT id FROM `title` WHERE `title` LIKE '%Awards%'")
    SqlResults = cursor.fetchall()
    blacklist = list(set([mov[0] for mov in SqlResults]))
    return blacklist

def movie_has_description(cursor, id):
    SQL = "select id from movie_info where movie_id = " + str(id) + ' and info_type_id = 98;'
    cursor.execute(SQL)
    results = cursor.fetchall()
    if len(results) >= 1:
        return True
    else:
        return False

def search_actors(cursor, regex):
    SQL = "SELECT id FROM `name` WHERE `name` REGEXP '%s'" % regex 
    cursor.execute(SQL)
    results = [ x[0] for x in cursor.fetchall() ]
    good_results = []
    for result in results:
        if len(movies_actor_has_been_in(cursor, result)) >= 4: 
            good_results.append(result)
    return tuple(good_results)

def search_movies(cursor, regex):
    SQL = "SELECT id FROM `title` WHERE `title` REGEXP '%s'" % regex 
    cursor.execute(SQL)
    results = [ x[0] for x in cursor.fetchall() ]
    good_results = []
    for result in results:
        if movie_has_description(cursor, result): 
            good_results.append(result)
    return tuple(good_results)

def actor_id_to_name(cursor, id):
    cursor.execute("SELECT `name` FROM `name` WHERE `id` = '%s'" % (id))
    Results = cursor.fetchall()
    return Results[0]

def movie_id_to_name(cursor, id):
    cursor.execute("SELECT `imdb_id`, `title`, `production_year` FROM `title` WHERE `id` = '%s'" % (id))
    Result = cursor.fetchall()
    return Result[0]

def movies_actor_has_been_in(cursor, id):
    cursor.execute("SELECT `movie_id` FROM `cast_info`, `title` WHERE `person_id` = '%s' AND title.id = cast_info.movie_id AND title.production_year >= 2000 AND title.production_year <= 2010 AND title.kind_id = '1' AND (role_id = 1 OR role_id = 2 AND (cast_info.note != '(uncredited)'  OR cast_info.note IS NULL))" % (id) )
    SqlResults = cursor.fetchall()
    return list(set([mov[0] for mov in SqlResults]))

def moviesincommon(actor1, actor2):
    movielist1 = movielist(actor1)
    movielist2 = movielist(actor2)
    commonmovies = list(set(movielist1).intersection(set(movielist2)) )
    return [i for i in commonmovies if i not in blacklist ]

def moviesincommon3(actor1, actor2, actor3):
    movielist1 = movielist(actor1)
    movielist2 = movielist(actor2)
    movielist3 = movielist(actor3)
    commonmovies = list(  set(movielist1).intersection(  set(movielist2).intersection(set(movielist3))         ) )
    return [i for i in commonmovies if i not in blacklist ]

def moviesincommon4(actor1, actor2, actor3, actor4):
    movielist1 = movielist(actor1)
    movielist2 = movielist(actor2)
    movielist3 = movielist(actor3)
    movielist4 = movielist(actor4)
    commonmovies = list(  set(movielist1).intersection(  set(movielist2).intersection( set(movielist3).intersection(set(movielist4))   )         ) )
    return [i for i in commonmovies if i not in blacklist ]

def moviestheyhavebeenin(cursor, actor_id):
    cursor.execute("SELECT `movie_id` FROM `cast_info`, `title` WHERE `person_id` = '%s' AND title.id = cast_info.movie_id AND title.production_year >= 2000 AND title.production_year <= 2010 AND title.kind_id = 1 AND (role_id = 1 OR role_id = 2) AND (cast_info.note != '(uncredited)'  OR cast_info.note IS NULL)" % (actor_id))
    SqlResults = cursor.fetchall()
    # We have a tuple of dictionaries from our mysql, but we just want a big tuple:
    return list(set([mov['movie_id'] for mov in SqlResults]))

def howmanymoviestheyhavebeenin(cursor, actor_id):
    return len(moviestheyhavebeenin(cursor, actor_id))

def actor_search(cursor, regex):
    cursor.execute("SELECT id FROM `name` WHERE `name` REGEXP '%s'" % regex )
    results = cursor.fetchall()
    #Turn this dictionary into a tuple
    actors = [persons['id'] for persons in results]
    return actors

def has_info(cursor, actor_id):
    cursor.execute("SELECT * FROM `person_info` WHERE `person_id` = '%s' " % actor_id)
    if cursor.rowcount > 0:
        return True
    else:
        return False
