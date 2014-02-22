# Role Playing 4 
# (c) Kyle Anderson - 2010
# All code under GPL3, artwork under CC-BY-SA
# kyle@xkyle.com
#

=== Checking out the Code ===
# If you haven't already
svn co http://dev.xkyle.com/gamesmagazine
cd Role\ Playing\ 4

=== Getting Started ===
#Sql Setup
CREATE USER 'imdb'@'localhost' IDENTIFIED BY 'imdb';
GRANT USAGE ON * . * TO 'imdb'@'localhost' IDENTIFIED BY 'imdb';
CREATE DATABASE IF NOT EXISTS `imdb` ;
GRANT ALL PRIVILEGES ON `imdb` . * TO 'imdb'@'localhost';

#Commands to import the imdb into sql
apt-get install python-imdbpy python-sqlalchemy python-mysqldb python-sqlobject
mkdir imdb
cd imdb
#Download everything, takes a while
wget -r ftp://ftp.fu-berlin.de/pub/misc/movies/database/ -l 1 -nd
cd ..
cp /usr/share/doc/python-imdbpy/examples/imdbpy2sql.py.gz .
gunzip imdbpy2sql.py.gz
python imdbpy2sql.py -d imdb -u "mysql://imdb:imdb@localhost/imdb"


#Now that you have the database, you can run the run the program:
#This will take a while, hours really.
./startatthecenter.py

#This uses the actorpossibilities.py file to have the actor possibilities,
#If you need to regenerate them you can run this:
#This will take a while, 20min on my Core2 2.6ghz
./find-actorpossibilities.py

=== IMPORTANT ===
#The "answers" this thing spits out are not vigorously tested, the program
#only matches actors who have movies in common, it doesn't actually go through 
#movies and mark them in their place. 
#
#Take the results it gives you and manually check them. After looking through 
#the few answers, the right one will be a little obvious. The others are either 
#very foriegn or include documentaries.
# 
#If you use the revised hints, you will get only one answer.