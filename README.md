# Compression: Huffman algorithm

## What it does?

It compress an ASCII file with the huffman algorithm. Of course you can decompress it.


## Why this project?

I use this little project like support for my remedial teaching.

It not the most optimized or effective program but it works. Moreover it is simple, clear and it allows to see the main aspects of the language (lists, classes, strings, files, decorators, import, ...).


## How use it?

First you have to download the repository.
```bash
ftz@zy:~/huffman$ git clone https://github.com/FtZzy/huffman.git
```

To compress the ascii file 'my_file.txt', use the `-c` argument. The result will be saved as 'my_file.bin'.
```bash
ftz@zy:~/huffman$ python main.py -c <my_file.txt>
```

Finally, you can decompress 'my_file.bin' with `-d`. The result will be saved as 'my_decompressed_file.txt'.
```bash
ftz@zy:~/huffman$ python main.py -d <my_file.bin>
```

You can compare the decompressed result and initial file with the bash command `diff <my_file.txt> <my_decompressed_file.txt>`.


## TODO
1. Improve actual source code
    * The compression is actually is in ascii text file, change it to binary file
    * Add tests
1. Add others languages:
    * C/C++
    * JavaScript


# LICENSE
Copyright (c) 2020 Nathan Krupa
