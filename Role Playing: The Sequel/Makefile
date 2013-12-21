db_init: 
	mysql -u root < dbinit.sql

deps:
	sudo apt-get install python-imdbpy python-sqlalchemy python-mysqldb python-sqlobject mysql-server

imdb:
	mkdir imdb
	cd imdb && wget -r ftp://ftp.fu-berlin.de/pub/misc/movies/database/ -l 1 -nd
	cp /usr/share/doc/python-imdbpy/examples/imdbpy2sql.py.gz .
	gunzip imdbpy2sql.py.gz
	python imdbpy2sql.py -d imdb -u "mysql://imdb:imdb@localhost/imdb"
