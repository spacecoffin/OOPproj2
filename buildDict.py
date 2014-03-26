# 1) Read document
# 2) Extract words
# 3) Insert into dictionary (file, not object)

# Assignment does not specify that this program should use classes.
# This program is meant to be used in the __init__ method of the
#       "Dictionary" class in the "spellCheck" program.

import re
# import io
# import string

def reader():
    pass

def main():
        # The program buildDict should begin by asking the user for a
        # list of text files to read from. The user should respond by
        # typing the file names as [filename1] [white space] [filename2]
        # [white space] [filename3]...
    inputList = input(
        "Please enter the name[s] of the file[s] (including the file-type \
        extension) from which to create the dictionary. \n\n If entering more \
        than one name, please separate each name by a space.\n\n"
        ).split() # formatting prints fucked up
    print(inputList)
    # wordregex = re.compile('[a-z]{2,}?', flags=re.IGNORECASE)
    word_list = []
    for f in inputList:
        try:
            file = open(f, 'r')
            line = file.readline()
            # print(line)            
            # line_stream = io.StringIO(line)
            # for c in line_stream:
            split_line = re.split(r'[^a-z]+', line, flags=re.IGNORECASE)
            for x in split_line:
                if len(x) >= 2:
                    if x not in word_list:
                        word_list.append(x.lower())
                
            
            
            # print(linewords)
        except IOError:
            # FileNotFoundError IS NEW FOR 3.3! 3.2 uses IOError!
            # Old line: (FileNotFoundError, IOError, IsADirectoryError):
            print("***Unable to read file \'{}\'!***\n".format(f))
    print(word_list)

    
    

main()