# -*- coding: utf-8 -*-

'''
Script to convert CoNLL formatted files to plain text.
Also works with token_tag formatted files.
Tokens are separated by whitespace. All tags are lost.
'''

import argparse
from nlpnet.pos.pos_reader import POSReader

import utils

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', help='Input CoNLL formatted (or token_tag) file')
    parser.add_argument('output', help='Output file')
    args = parser.parse_args()

    r = POSReader(filename=args.input, load_dictionaries=False)
    utils.write_corpus(r.sentences, args.output, False)




