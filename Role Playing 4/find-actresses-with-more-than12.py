#!/usr/bin/env python
import MySQLdb
import imdb

#Did you import the imdb into your mysql using imdbpy ?
dbhost = 'localhost'
dbuser = 'imdb'
dbpass = 'imdb'
dbname = 'imdb'
db = MySQLdb.connect(host=dbhost, user=dbuser, passwd=dbpass,db=dbname)
cursor = db.cursor(MySQLdb.cursors.DictCursor)


#Exhaustive list of actors
cursor.execute("SELECT `id` FROM `name` WHERE 1")
SqlResults = cursor.fetchall()
everyactorlist = [x['id'] for x in SqlResults]
possibilties = []
for actor in everyactorlist:
	#Lets take each actor/actress and find those that fit our criterea
	cursor.execute("SELECT `movie_id` FROM `cast_info`, `title` WHERE `person_id` = '%s' AND title.id = cast_info.movie_id AND title.production_year >= 2000 AND title.kind_id = 1 AND cast_info.role_id = '2'" % (actor))
	SqlResults = cursor.fetchall()
	movielist = [mov['movie_id'] for mov in SqlResults]
	if len(movielist) >= 13:
		possibilties.append(actor)
		cursor.execute("SELECT `name` FROM `name` WHERE `id` = '%s'" % (actor))
		SqlResults2 = cursor.fetchall()
		print "Actress " + SqlResults2[0]['name'] + " ("  + str(actor) + ") has 13 or more movies recently"

print "Use this list to start from."

print possibilties
f = open('actresseswithmorethan12.py','w')
f.write("actresseswithmorethan12 = " + possibilties)
f.close()
print "actresseswithmorethan12.py has been populated with this data."
