# Radium Files Extractor

Some python3 scripts to extract from kfs, graphic bin, pic and act files
in the Radium game from Karma Studios

## How to install it

You need to have python 3.x installed (see https://www.python.org/downloads/)

You also need to install the pillow package for python3 (see https://pillow.readthedocs.io/en/stable/installation.html)

Then, clone this repository or just download it

## How to use it

### Extract from KFS files

Run in the command line the extract\_kfs.py script: 

python3 extract\_kfs.py in\_file out\_file

in\_file the archive file

out\_file the extracted archive path (a directory)

### Extract from PIC/ACT files

Run in the command line the extract\_pic.py script: 

python3 extract\_pic.py in\_file\_pic \[in\_file\_act\] out\_file

in\_file\_pic the image data (pic file)

in\_file\_act OPTIONAL the palette data (act file); if not given, the output image will have a grayscale palette

out\_file the extracted image (png format)


### Extract from BIN graphic files

Run in the command line the extract\_bin.py script: 

python3 extract\_bin.py in\_file out\_file

in\_file the binary file

out\_file the extracted image (png format)
