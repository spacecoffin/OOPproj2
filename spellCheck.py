import re
import fileinput

class Dictionary:
    def __init__(self):
        # This program should start by reading the list of words in the
        # file words.dat into a data structure that can be quickly
        # searched.
        dict_file = open("words.dat")
        self.dict_set = set()
        for word in dict_file:
            word = word.rstrip()
            self.dict_set.add(word)
        dict_file.close
        # Valid single letter words such as 'A' and 'I' should also be
        # added to the data structure.
        single_letter_wordlist = ['a', 'i', 'o']
        for word in single_letter_wordlist:
            self.dict_set.add(word)
    
    def verify(self, check_word):
        # This method verifies the word supplied by the spellCheck
        # program. If it finds word in the data structures that it
        # maintains then it returns a 'new word' that must be output.
        # Otherwise, it returns None.
        lcase_word = check_word.lower()
        if lcase_word in self.ignore_set:
            return check_word
        elif lcase_word in self.replace_dict:
            return self.replace_dict.get(lcase_word)
        elif lcase_word in self.dict_set:
            return check_word
        else:
            return None
    
    def update(self, update_cmd, add_word, replacement=''):
        # This method updates the data structures in response to the
        # user input of P or p and N or n.
        update_cmd = update_cmd.lower()
        if update_cmd == 'n':
            self.ignore_set.add(add_word)
        elif update_cmd == 'p':
            self.replace_dict[add_word] = replacement
    
    def __iter__(self):
        return self
    
    def __next__(self):
        pass
    
    def print(self):
        print(self.dict_set)

        """
        if 'a' in self.dict_set:
            print("a is in it")
        if 'i' in self.dict_set:
            print("I is in it")
        if 'o' in self.dict_set:
            print("O is in it")
        if 'zz' in self.dict_set:
            print("bazooka is in it")
        """

if __name__ == '__main__':
    this_dict = Dictionary()
    # Prompt user for the name of a document she wants spell-checked.
    file_name = input("Name of the document to be spell-checked: ")
    try:
        file = open(file_name)
        # spellCheck should read words from the specified document,
        # one-by-one and test if the words appears in its dictionary.
        for line in file.readlines():
            split_line = re.split(r'[^a-z]+', line, flags=re.IGNORECASE)
            for word in split_line:
                if len(word) >= 2:
                    this_dict.verify(word)
                    # if word not in this_dict.dict_set:
                        # print("{} ain't in it.".format(word))
                        # input("replace(R), replace all(P), ignore(I), ignore all(N), exit(E): ")
                else:
                    continue
            else:
                continue
            
    except IOError:
        # FileNotFoundError IS NEW FOR 3.3! 3.2 uses IOError!
        print("***Unable to read file \'{}\'!***\n".format(f))
    
    