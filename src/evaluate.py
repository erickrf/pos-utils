# -*- coding: utf-8 -*-

'''
Script to evaluate POS performance over an automatically tagged file.
'''

import argparse
from itertools import izip

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('system', help='File tagged by system')
    parser.add_argument('gold', help='Gold File')
    args = parser.parse_args()
    
    total_tokens = 0
    hits = 0
    
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
                total_tokens += 1
    
    accuracy = float(hits) / total_tokens
    
    print '{} hits out of {}'.format(hits, total_tokens)
    print 'Accuracy: {:f}'.format(accuracy)
