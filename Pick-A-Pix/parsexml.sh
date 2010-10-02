#!/bin/bash
cat img | grep '<row' | cut -f 2 -d ">" | cut -f 1 -d "<" | tr -d [:blank:] > matrix
TEMP=`cat matrix  | tail -n 1 | wc -c`
echo '<table border="0" cellpadding="0" cellspacing="0">'
let REALWIDTH=$TEMP-1
for EACHROW in `cat matrix`
	do
	echo '<tr>'
	WIDTH=1
	while [ $WIDTH -le $REALWIDTH ]
		do
		EACHCOL=`echo $EACHROW | cut -c $WIDTH`
		echo -n '<td>'
		if [ "$EACHCOL" -eq "0" ];then
		echo -n '<img src="white.gif" height=4 width=4>'
		elif [ "$EACHCOL" -eq "1" ]; then
		echo -n '<img src="black.gif" height=4 width=4>'
		elif [ "$EACHCOL" -eq "3" ]; then
		echo -n '<img src="red.gif" height=4 width=4>'
		elif [ "$EACHCOL" -eq "2" ]; then
		echo -n '<img src="blue.gif" height=4 width=4>'
		elif [ "$EACHCOL" -eq "4" ]; then
		echo -n '<img src="yellow.gif" height=4 width=4>'
		elif [ "$EACHCOL" -eq "5" ]; then
		echo -n '<img src="green.gif" height=4 width=4>'
		elif [ "$EACHCOL" -eq "6" ]; then
		echo -n '<img src="orange.gif" height=4 width=4>'
		else
		echo -n '<img src="grey.gif" height=4 width=4>'
		fi
		echo '</td>'
		let WIDTH=$WIDTH+1
		done
	echo "</tr>"
done
echo '</table><br>'
echo '<!-- end of table>'

