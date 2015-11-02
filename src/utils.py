# -*- coding: utf-8 -*-

'''
Utility functions
'''


def write_corpus(sentences, filename, write_tags=True):
    '''
    Write a list of sentences to a file.
    '''
    with open(filename, 'wb') as f:
        for sent in sentences:
            if write_tags:                
                line = u'{}\n'.format(u' '.join(u'{}_{}'.format(token, tag) 
                                                for token, tag in sent))
            else:
                line = u'{}\n'.format(u' '.join(token for token, _ in sent))
            f.write(line.encode('utf-8'))
