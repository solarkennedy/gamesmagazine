Getting Started
---------------

## Sql Setup

```
CREATE USER 'imdb'@'localhost' IDENTIFIED BY 'imdb';
GRANT USAGE ON * . * TO 'imdb'@'localhost' IDENTIFIED BY 'imdb';
CREATE DATABASE IF NOT EXISTS `imdb` ;
GRANT ALL PRIVILEGES ON `imdb` . * TO 'imdb'@'localhost';
```

### Commands to import the imdb into sql
```
apt-get install python-imdbpy python-sqlalchemy python-mysqldb python-sqlobject
mkdir imdb
cd imdb
#Download everything, takes a while
wget -r ftp://ftp.fu-berlin.de/pub/misc/movies/database/ -l 1 -nd
cd ..
cp /usr/share/doc/python-imdbpy/examples/imdbpy2sql.py.gz .
gunzip imdbpy2sql.py.gz
python imdbpy2sql.py -d imdb -u "mysql://imdb:imdb@localhost/imdb"
```

## Initial Pass

Now that you have the database, you can run the run the program:
