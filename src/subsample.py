# -*- coding: utf-8 -*-

'''
Read a POS tagged corpus and extract sentences until a given number
of tokens is achieved. The extracted sentences are saved in a new file.
'''

import argparse
from nlpnet.pos.pos_reader import POSReader

import utils

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', help='Corpus file')
    parser.add_argument('output', help='Output file')
    parser.add_argument('num_tokens', help='Minimum number of tokens', type=int)
    args = parser.parse_args()
    
    r = POSReader(filename=args.input, load_dictionaries=False)
    new_sentences = []
    total_tokens = 0
    
    for sent in r.sentences:
        if total_tokens >= args.num_tokens:
            break
        
        new_sentences.append(sent)
        total_tokens += len(sent)
    
    utils.write_corpus(new_sentences, args.output)