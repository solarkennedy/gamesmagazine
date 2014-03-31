#!/bin/bash
#
# In Other Words Solver
#
# Iterates through a list of hints and finds words that match
# per the rules.


# Echos a bash command pipleline that represents the rules
# Must be evaled
function build_filter {
  local FILTER
  for WORD in $*; do
    FILTER="${FILTER}grep  '.*"
    for LETTER in `echo $WORD | grep -o .`; do
      letter=`echo $LETTER | tr [A-Z] [a-z]`
      FILTER="${FILTER}${letter}.*"
    done
    FILTER="${FILTER}' | "
  done
  echo $FILTER cat
}

# Takes a set of words and returns words that work out of the dictionary
function solve {
  FILTER=`build_filter $*`
  # Must be more than 8 characters, and only valid characters
  grep -E '^.{8,}$' /usr/share/dict/words \
  | grep -E '^[a-z]*$' \
  | eval $FILTER \
  | grep -P '^(?:([A-Za-z])(?!.*\1))*$' \
  | grep -v '^$'
}

# Main loop. Take in the hints and try to solve each
function main {
  while read LINE; do
    WORDS=`echo $LINE | tr -d ,`
    echo "Solving for $WORDS"
    ANSWERS=`solve $WORDS`
    if [[ -z "$ANSWERS" ]]; then
      echo "  NO ANSWERS"
    else
      echo "$ANSWERS" | sed 's/^/  /g'
    fi
  done < hints.txt
}

if [ "$BASH_SOURCE" == "$0" ]; then
  # code in here only gets executed if
  # script is run directly on the commandline
  time main
fi
