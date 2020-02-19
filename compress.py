#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import maxsize


def compress(filename):
    """Processus to compress an ASCII file with Huffman algorithm.

    :filename: str, path for the file to compress
    """
    occ_dict = create_occurence_dict(filename)
    trans_dict = create_translator(occ_dict)
    print(trans_dict)


def create_occurence_dict(filename):
    """Create the occurence dict of characters for a given file.

    :filename: str, path for the file
    :returns: Dict[char:int], occurence dict
    """
    result = {}
    with open(filename, 'r') as f:
        content = f.readlines()

    for line in content:
        for c in line:
            if c in result:
                result[c] += 1
            else:
                result[c] = 1

    return result


def get_rarest_character(dictionary):
    """Search the the character with the less of occurence.

    :dictionary: Dict[char:int], dict of char to int
    :returns: char, the character with the less of occurence in the dictionary
    """
    # Nice version
    # import operator
    # return min(dictionary.iteritems(), key=operator.itemgetter(1))[0]

    # Learning version
    min_value = None
    min_count = maxsize
    for c in dictionary:
        if dictionary.get(c) < min_count:
            min_value = c
            min_count = dictionary.get(c)

    return min_value


def create_translator(occ_dict):
    """Create the translator dict.

    :occ_dict: dict, occurence of ascii character
    :returns: TODO
    """
    result = {}
    return result
