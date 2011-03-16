#!/bin/bash
for EACHWORD in `cat col1` 
do
#EACHWORD=recent
	LETTERCOUNTER=0
	WORDLENGTH=`echo -n $EACHWORD | wc -c`
	for EACHLETTER in `echo -n $EACHWORD | sed 's/./&\n/g'`
	do
		for NEWLETTER in `cat thealphabet`
		do	
			#replace that letter with a differeint one
			NEWWORD="${EACHWORD:0:$LETTERCOUNTER}$NEWLETTER${EACHWORD:$LETTERCOUNTER+1:$WORDLENGTH}"
			OLDLETTER="${EACHWORD:$LETTERCOUNTER:1}"
			if [ "$NEWWORD" != "$EACHWORD" ]; then   #WE cannot have the same word again
				grep -x $NEWWORD /usr/share/dict/words > /dev/null
				if [ $? -eq 0 ]; then #Our new word is legit
					
				echo A new word is $NEWWORD
							


					

				for CANDIDATE in `grep $NEWLETTER col2`
				do
				NEWWORD2=`echo $CANDIDATE | sed "s/$NEWLETTER/$OLDLETTER/" `
				grep -x $NEWWORD2 /usr/share/dict/words > /dev/null
                                if [ $? -eq 0 ]; then #Our new word is legit
				#echo "Our new word is $NEWWORD (exchanged $OLDLETTER for $NEWLETTER on space $LETTERCOUNTER)  "
				echo -n "$OLDLETTER $EACHWORD ($NEWWORD)"
				echo -e  "\t $NEWLETTER $CANDIDATE ($NEWWORD2)"
				fi
				
				done
										





				fi
			fi 
		done
	let LETTERCOUNTER=$LETTERCOUNTER+1
	done
		


done
