#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from sys import maxsize


@dataclass
class Node:
    """Node data class."""
    value: str
    weight: int
    length: int = field(init=False)

    def __post_init__(self):
        self.length = len(self.value)


def compress(filename):
    """Processus to compress an ASCII file with Huffman algorithm.

    :filename: str, path for the file to compress
    """
    try:
        text = get_file_content(filename)
    except FileNotFoundError:
        print("Cannot find the file '%s'!" % filename)
    except PermissionError:
        print("Cannot access to '%s', please check the permission." % filename)
    else:
        print("Compressing...")
        occ_dict = create_occurence_dict(text)
        trans_dict = create_translator(occ_dict)
        create_compressed_file(text, trans_dict)


def get_file_content(filename):
    """Get the content of a file.

    :filename: str, path for the file
    :returns: str, the content of the file
    """
    with open(filename, 'r') as f:
        content = f.readlines()
    return ''.join(content)


def create_occurence_dict(text):
    """Create the occurence dict of characters for a given text.

    :text: str, ascii text
    :returns: Dict[char:int], occurence dict
    """
    result = {}
    for c in text:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result


def get_rarest_node(dictionary):
    """Search the character with the less of occurence.

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
    dictionary.pop(min_value)
    return Node(min_value, min_count)


def update_translator(dictionary, liste, binary=0):
    """Update the translator dictionary for a list of string.

    :dictionary: dict, the translator dictionary
    :liste: str, the liste of character to update
    :binary: int, value to add for update (0 or 1)
    """
    for character in liste:
        if character in dictionary:
            dictionary[character] = str(binary) + dictionary[character]
        else:
            dictionary[character] = str(binary)


def create_translator(occ_dict):
    """Create the translator dict.

    :occ_dict: dict, occurence of ascii character
    :returns: dict, the translator dictionary ascii to binary
    """
    result = {}
    while len(occ_dict) > 1:
        # Update occurence dictionary
        node_1 = get_rarest_node(occ_dict)
        node_2 = get_rarest_node(occ_dict)
        occ_dict[node_1.value + node_2.value] = node_1.weight + node_2.weight

        # Update translator dictionary
        update_translator(result, node_1.value)
        update_translator(result, node_2.value, 1)

    return result


def create_compressed_file(text, translator, compressed_filename="compressed.bin"):
    """Create the compressed file (filename.bin).

    :text: str, ascii string to compress
    :translator: dict, the translator dictionary
    :compressed_filename: str, compressed file name
    """
    with open(compressed_filename, 'w') as f:
        f.write(str(translator) + "\n")  # send the translator for decompression
        for c in text:
            f.write(translator.get(c))
