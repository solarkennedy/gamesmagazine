#!/usr/bin/env python

import pickle
import imdb_lib
import pygraphviz
import subprocess
import sqlite3

conn = sqlite3.connect('imdb.db')
cursor = conn.cursor()

board = pickle.load(open('solution_board.p', 'r'))

graph=pygraphviz.AGraph(overlap='false', splines='false', overlap_shrink='true')

actor_hash = {}
for actor in board.actors:
    name = imdb_lib.actor_id_to_name(cursor, actor.imdb_id)
    node = actor.node
    id   = actor.imdb_id
    hint = actor.hint
    if not hint: hint = '?'
    if node < 16:
        color = 'gold4'
    else:
        color = 'khaki'
    string = name + "\\n" + str(hint) + "\\nNode: " + str(node) + "\\nIMDB ID: " + str(id)
    actor_hash[node] = string
    graph.add_node(string, shape='square', fillcolor=color, style='filled', width=2, height=2, fixedsize=True)

movie_hash = {}
for movie in board.movies:
    id = movie.imdb_id
    name = imdb_lib.movie_id_to_name(cursor, id)
    node = movie.node
    hint = movie.hint
    string = name + "\\n" + str(hint) + "\\nNode: " + str(node) + "\\nIMDB ID: " + str(id)
    movie_hash[node] = string
    graph.add_node(string, shape='circle', fillcolor='khaki1', style='filled',  width=2, height=2, fixedsize=True)

for actor in board.actors:
    for link in actor.links:
        graph.add_edge(actor_hash[actor.node], movie_hash[link])

graph.draw('solution.png',prog='neato') 
graph.write('solution.dot') 
subprocess.call(['eog', 'solution.png'])
