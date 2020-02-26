#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ast import literal_eval

from .compress import get_file_content


def decompress(filename):
    """Processus to decompress a file compressed with our program.

    :filename: str, path for the file to decompress
    """
    try:
        content = get_file_content(filename)
        translator, text = split_text(content)
    except FileNotFoundError:
        print("Cannot find the file '%s'!" % filename)
    except PermissionError:
        print("Cannot access to '%s', please check the permission." % filename)
    except TypeError:
        print("Cannot decompress the file '%s'." % filename)
    else:
        print("Decompressing...")
        if translator and text:
            reversed_translator = reverse_dict(translator)
            traduce_file(text, reversed_translator)


def split_text(content):
    """Get the translator and the binary text of a text of two lines (one for
    each information).

    :content: str, text of two line with a dictionary in the first line and a
              text in the second
    :returns: (Dict[char:str], str), the translator and the 0/1 text
    """
    try:
        lines = content.split('\n')
        translator = literal_eval(lines[0])
        text = lines[1]
    except IndexError:
        print("The file need to have 2 lines... Is it the good file?")
    except Exception as e:
        print("Hum, something is wrong with this file... %s. Is it the good file?" % e)
    else:
        return translator, text


def reverse_dict(dictionary):
    """Reverse the keys and the values of a dictionary.

    :dictionary: Dict[char:str], the dictionary with UNIQUES values to reverse.
    :returns: Dict[str, char], the reversed dictionary
    """
    return {dictionary[key]: key for key in dictionary}


def traduce_file(text, translator, decompressed_filename="./files/my_decompressed_file.txt"):
    """Create and write the decompressed file.

    :text: str, 0/1 string to decompress
    :translator: Dict[str: char], the translator dictionary
    :decompressed_filename: str, decompressed file name
    """
    begin = 0
    end = 1
    with open(decompressed_filename, 'w') as f:
        while end <= len(text):
            if text[begin:end] in translator:
                f.write(translator.get(text[begin:end]))
                begin = end
            end += 1
