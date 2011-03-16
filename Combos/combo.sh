#!/bin/bash
for LETTER in `echo $1 | sed 's/./&\n/g'`
do
COMMAND="$COMMAND ?$LETTER"
done
exec egrep -e "$COMMAND" list
