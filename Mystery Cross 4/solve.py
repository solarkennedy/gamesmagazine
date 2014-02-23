#!/usr/bin/env python
import copy
import crossword_lib

if __name__ == '__main__':
    board_so_far = crossword_lib.seed_board()
    words_so_far = []
    intersect_pool = list(crossword_lib.intersecting_letters)
    non_intersect_pool = list(crossword_lib.non_intersecting_letters)
    crossword_lib.recursive_solve( \
        copy.deepcopy(words_so_far), \
        copy.deepcopy(intersect_pool), \
        copy.deepcopy(non_intersect_pool), \
        copy.deepcopy(board_so_far) )
