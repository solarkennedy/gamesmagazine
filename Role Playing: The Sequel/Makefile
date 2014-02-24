db_init: 
	mysql -u root < dbinit.sql

deps:
	sudo apt-get install python-imdbpy sqlite3-pcre

imdb:
	mkdir imdb
	cd imdb && wget -c -r ftp://ftp.fu-berlin.de/pub/misc/movies/database/ -l 1 -nd

db:
	cp /usr/share/doc/python-imdbpy/examples/imdbpy2sql.py.gz .
	gunzip -f imdbpy2sql.py.gz
	python imdbpy2sql.py --sqlite-transactions -d imdb -u "sqlite:/tmp/imdb.db"
