#!/usr/bin/env python
import os
import sys
import pprint
import re
import copy

intersecting_letters = tuple("AAACEGHIMRRSSUUVZ".lower()[::-1])
intersecting_spaces = ( \
    (14,4), (1,6), (3,6), (10,6), (12,6), (14,6), (14,8), (12,8), (10,8), (3,8), \
    (1,8), (1,10), (6,12), (10,12), (12,12), (9,17), (6,17) )
non_intersecting_letters = \
    tuple("AAAAAAAAAAABBBCCDEEEEEEEEEEFGGGIIIIIIILLLLLMNNNNNNOOOOOOOPPRRRRRSTTTTUUUUUUVYYY".lower()[::-1])

slots = { 
     1: { 'direction': 'down',   'x':14, 'y':0,  'length':9  },
     2: { 'direction': 'across', 'x':11, 'y':4,  'length':6  },
     3: { 'direction': 'down',   'x':10, 'y':6,  'length':8  },
     4: { 'direction': 'down',   'x':12, 'y':6,  'length':9  },
     5: { 'direction': 'across', 'x':8,  'y':8,  'length':8  },
     6: { 'direction': 'down',   'x':6,  'y':11, 'length':7  },
     7: { 'direction': 'across', 'x':6,  'y':12, 'length':8  },
     8: { 'direction': 'down',   'x':9,  'y':14, 'length':4  },
     9: { 'direction': 'across', 'x':5,  'y':17, 'length':7  },
    10: { 'direction': 'down',   'x':3,  'y':2,  'length':7  },
    11: { 'direction': 'across', 'x':0,  'y':8,  'length':6  },
    12: { 'direction': 'across', 'x':0,  'y':10, 'length':5  },
    13: { 'direction': 'across', 'x':1,  'y':6,  'length':17 },
    14: { 'direction': 'down',   'x':1,  'y':6,  'length':12 },
    }

#slots = { 
#     1: { 'direction': 'down',   'x':14, 'y':0,  'length':9  },
#     2: { 'direction': 'across', 'x':11, 'y':4,  'length':6  },
#     3: { 'direction': 'down',   'x':10, 'y':6,  'length':8  },
#     4: { 'direction': 'down',   'x':12, 'y':6,  'length':9  },
#     5: { 'direction': 'across', 'x':8,  'y':8,  'length':8  },
#     6: { 'direction': 'down',   'x':6,  'y':11, 'length':7  },
#     7: { 'direction': 'across', 'x':6,  'y':12, 'length':8  },
#     8: { 'direction': 'down',   'x':9,  'y':14, 'length':4  },
#     9: { 'direction': 'across', 'x':5,  'y':17, 'length':7  },
#    10: { 'direction': 'down',   'x':3,  'y':2,  'length':7  },
#    11: { 'direction': 'across', 'x':0,  'y':8,  'length':6  },
#    12: { 'direction': 'across', 'x':0,  'y':10, 'length':5  },
#    13: { 'direction': 'across', 'x':1,  'y':6,  'length':17 },
#    14: { 'direction': 'down',   'x':1,  'y':6,  'length':12 },
#    }


def sort_wordlist(wordlist):
    sorted_dict = {}
    for word in wordlist:
        if len(word) not in sorted_dict:
            sorted_dict[len(word)] = []
        sorted_dict[len(word)].append(word)
    return sorted_dict

def read_wordlist(words_file='nounlist.txt'):
    wordlist=[]
    valid_re=re.compile('^[a-z]+$')
    for word in open(words_file):
        if valid_re.match(word):
            wordlist.append(word.strip())
    import random
    random.shuffle(wordlist)
    return wordlist

def print_board(board):
    BOLD='\033[1m'
    BLUE='\033[94m'
    CLEAR='\033[0m'
    for y in range(0,len(board)):
        for x in range(0,len(board[y])):
            if (x,y) in intersecting_spaces:
                s = BLUE + board[x][y] + CLEAR
            else:
                s = board[x][y]
            sys.stdout.write(s)
        print

wordlist = read_wordlist()
words_with_length = sort_wordlist(wordlist)

def current_slot_regex(slot_num, board):
    regex_string = ''
    direction = slots[slot_num]['direction']
    length = slots[slot_num]['length']
    start_x = slots[slot_num]['x']
    start_y = slots[slot_num]['y']
    if direction == 'down':
        for y in range(length):
            regex_string += board[start_x][start_y + y]
    elif direction == 'across':
        for x in range(length):
            regex_string += board[start_x + x][start_y]
    else: 
        raise "Unknown direction"
    regex = '^' + regex_string + '$'
    #print "Regex for slot " + str(slot_num) + " is " + regex
    return regex

def words_with_right_regex(regex, words):
    matches = []
    for word in words:
        if re.match(regex, word):
            matches.append(word)
    return matches

def seed_board():
    board = [ list(" " * 18) for _ in range(18) ]
    for word_num in range(len(slots)):
        slot = slots[word_num+1]
        for n in range(slot['length']): 
            if slot['direction'] == 'across':
                x = slot['x'] + n
                y = slot['y']
            else:
                y = slot['y'] + n
                x = slot['x']
            board[x][y]='.'
    return board

def possible_normal_words(slot_number, intersect_pool, non_intersect_pool, board_so_far):
    slot_regex = current_slot_regex(slot_number, board_so_far)
    right_length = words_with_length[slots[slot_number]['length']]
    right_regex = words_with_right_regex(slot_regex, right_length)
    return right_regex

def try_to_fit(possible_word, words_so_far, intersect_pool, non_intersect_pool, board):
    slot_number = len(words_so_far) + 1
    slot = slots[slot_number]
    x = slot['x']
    y = slot['y']
    for n in range(slot['length']):
        if (x,y) in intersecting_spaces:
            intersecting = True
        else:
            intersecting = False
        # Remove the letter if it is not already in the board
        if board[x][y] != possible_word[n]:
            if intersecting == True and possible_word[n] in intersect_pool:
                intersect_pool.remove(possible_word[n])
            elif intersecting == False and possible_word[n] in non_intersect_pool:
                non_intersect_pool.remove(possible_word[n])
            else:
                return False 
        board[x][y] = possible_word[n]
        if slot['direction'] == 'across':
            x += 1    
        else:
            y += 1
    #If we did get here, the word fit!
    words_so_far.append(possible_word)
    recursive_solve(copy.deepcopy(words_so_far), copy.deepcopy(intersect_pool), copy.deepcopy(non_intersect_pool), copy.deepcopy(board))

def recursive_solve(words_so_far, intersect_pool, non_intersect_pool, board_so_far):
    solving_for_word = len(words_so_far) + 1
    if solving_for_word == 13 :
        print "OMG WE ARE DONE: Word so far: " + str(words_so_far)
        print "Our remaining intersecting letters should be zero: " + "".join(intersect_pool)
        print "Our remaining non-intersecting letters should be zero: " + ''.join(non_intersect_pool)
        print "The Board: "
        print_board(board_so_far)
        return 
    else:
        for possible_word in possible_normal_words(solving_for_word, intersect_pool, non_intersect_pool, board_so_far):
            try_to_fit(copy.deepcopy(possible_word), copy.deepcopy(words_so_far), copy.deepcopy(intersect_pool), copy.deepcopy(non_intersect_pool), copy.deepcopy(board_so_far))
