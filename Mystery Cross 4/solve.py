#!/usr/bin/env python
import sys
import pprint
import re

intersecting_letters = list("AAACEGHIMRRSSUUVZ")
intersecting_spaces = [ \
    (14,4), (1,6), (3,6), (10,6), (12,6), (14,6), (14,8), (12,8), (10,8), (3,8), \
    (1,8), (1,10), (6,12), (10,12), (12,12), (9,17), (6,17) ]
non_intersecting_letters = \
    list("AAAAAAAAAAABBBCCDEEEEEEEEEEFGGGIIIIIIILLLLLMNNNNNNOOOOOOOPPRRRRRSTTTTUUUUUUVYYY")

slots = { 
     '1': { 'direction': 'down',   'x':14, 'y':0,  'length':9  },
     '2': { 'direction': 'across', 'x':11, 'y':4,  'length':6  },
     '3': { 'direction': 'down',   'x':10, 'y':6,  'length':8  },
     '4': { 'direction': 'down',   'x':12, 'y':6,  'length':9  },
     '5': { 'direction': 'across', 'x':8,  'y':8,  'length':8  },
     '6': { 'direction': 'down',   'x':6,  'y':11, 'length':7  },
     '7': { 'direction': 'across', 'x':6,  'y':12, 'length':8  },
     '8': { 'direction': 'down',   'x':9,  'y':14, 'length':4  },
     '9': { 'direction': 'across', 'x':5,  'y':17, 'length':7  },
    '10': { 'direction': 'down',   'x':3,  'y':2,  'length':7  },
    '11': { 'direction': 'across', 'x':0,  'y':8,  'length':6  },
    '12': { 'direction': 'across', 'x':0,  'y':10, 'length':5  },
    '13': { 'direction': 'across', 'x':1,  'y':6,  'length':17 },
    '14': { 'direction': 'down',   'x':1,  'y':6,  'length':12 },
    }

def read_wordlist(words_file='/usr/share/dict/words'):
    wordlist=[]
    valid_re=re.compile('^[a-z]+$')
    for word in open(words_file):
        if valid_re.match(word):
            wordlist.append(word.strip())
    return wordlist

def print_board(board):
    for x in range(0,len(board)):
        for y in range(0,len(board[x])):
            sys.stdout.write(board[x][y])
        print

if __name__ == '__main__':
    wordlist = read_wordlist()

    board = [ list(" " * 18) for _ in range(18) ]
    #print_board(board)
    #pprint.pprint(board)
