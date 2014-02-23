#!/usr/bin/env python
import copy
import crossword_lib

if __name__ == '__main__':
    board_so_far = crossword_lib.seed_board()
    words_so_far = []
    intersect_pool = list(crossword_lib.intersecting_letters)
    non_intersect_pool = list(crossword_lib.non_intersecting_letters)

#    board_so_far[9][14] = 'i'
#    non_intersect_pool.remove('i')
#    board_so_far[9][15] = 'n'
#    non_intersect_pool.remove('n')
#    board_so_far[9][16] = 'c'
#    non_intersect_pool.remove('c')
#    board_so_far[9][17] = 'h'
#    intersect_pool.remove('h')

#    board_so_far[1][6] = 'a'
#    intersect_pool.remove('a')
   
#    board_so_far[5][17] = 'p'
#    non_intersect_pool.remove('p')
#    board_so_far[6][17] = 'r'
#    intersect_pool.remove('r')
#    board_so_far[7][17] = 'o'
#    non_intersect_pool.remove('o')

    #board_so_far[1][6] = 'm'
    #intersect_pool.remove('m')

 
    crossword_lib.seed_word(2, 'pretzel', intersect_pool, non_intersect_pool, board_so_far)
#    crossword_lib.seed_word(5, 'doughnut', intersect_pool, non_intersect_pool, board_so_far)
#    crossword_lib.seed_word(9, 'prophet', intersect_pool, non_intersect_pool, board_so_far)
#    crossword_lib.seed_word(6, 'saviour', intersect_pool, non_intersect_pool, board_so_far)

    crossword_lib.print_board(board_so_far)

#intersecting_spaces = ( \
#    (14,4), (1,6), (3,6), (10,6), (12,6), (14,6), (14,8), (12,8), (10,8), (3,8), \
#    (1,8), (1,10), (6,12), (10,12), (12,12), (9,17), (6,17) )


    crossword_lib.recursive_solve( \
        copy.deepcopy(words_so_far), \
        copy.deepcopy(intersect_pool), \
        copy.deepcopy(non_intersect_pool), \
        copy.deepcopy(board_so_far) )
