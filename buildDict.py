# 1) Read document
# 2) Extract words
# 3) Insert into dictionary (file, not object)

# Assignment does not specify that this program should use classes.
# It seems like it is meant to be used in the __init__ method of the "Dictionary" class in the "spellCheck" program.

def main():
        #The program buildDict should begin by asking the user for a list of text files to read from. The user should respond by typing the file names as [filename1] [white space] [filename2] [white space] [filename3]...
    inputList = input("Please enter the name[s] of the file[s] (including the file-type extension) from which to create the dictionary. \n\n If entering more than one name, please separate each name by a space.\n\n").split()
    print(inputList)
    

main()