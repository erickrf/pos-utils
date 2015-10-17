# -*- coding: utf-8 -*-

'''
Script to evaluate POS performance over an automatically tagged file.
'''

import argparse
from collections import Counter
from itertools import izip

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('system', help='File tagged by system')
    parser.add_argument('gold', help='Gold File')
    parser.add_argument('-c', type=int, dest='count_words', default=None,
                        help='Count words tagged wrong most often and show the top ones')
    args = parser.parse_args()
    
    total_tokens = 0
    hits = 0
    if args.count_words:
        wrong_words = Counter()
    
    with open(args.system, 'rb') as fs, open(args.gold, 'rb') as fg:
        for line_system, line_gold in izip(fs, fg):
            items_system = line_system.split()
            items_gold = line_gold.split()
            
            for item_system, item_gold in izip(items_system, items_gold):
                token_system, tag_system = item_system.rsplit('_', 1)
                token_gold, tag_gold = item_gold.rsplit('_', 1)
                
                assert token_gold == token_system, 'Tokens differ.'
                
                if tag_gold == tag_system:
                    hits += 1
                elif args.count_words:
                    lowered = token_system.lower()
                    wrong_words[lowered] += 1
                    
                total_tokens += 1
    
    accuracy = 100 * float(hits) / total_tokens
    
    print '{} hits out of {}'.format(hits, total_tokens)
    print 'Accuracy: {:f}'.format(accuracy)
    
    if args.count_words:
        print
        print 'Words tagged wrong most often:'
        top_words = wrong_words.most_common(args.count_words)
        for word, count in top_words:
            print word, count
