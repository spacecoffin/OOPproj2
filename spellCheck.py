import re
import fileinput

class Dictionary:
    def __init__(self):
        # This program should start by reading the list of words in the
        # file words.dat into a data structure that can be quickly
        # searched.
        self.dict_set = set()
        self.ignore_set = set()
        self.replace_dict = {}
        dict_file = open("words.dat")
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
    
    def user_prompt():
        while True:
            user_cmd = input("""replace(R), replace all(P), ignore(I),
                                ignore all(N), exit(E): """)
            user_cmd = user_cmd.lower()
            if user_cmd == 'i':
                break
            if user_cmd == 'r':
                replacement_word = input("Replacement word: ")
                split_line[word] = replacement_word
                break
            if user_cmd == 'n':
                this_dict.update('n', word)
                break
            if user_cmd == 'p':
                replacement_word = input("Replacement word: ")
                split_line[word] = replacement_word
                this_dict.update('p', word, replacement=replacement_word)
                break
            if user_cmd == 'e':
                raise ExitByUser

    def __iter__(self):
        return self
    
    def __next__(self):
        pass
    
    def print(self):
        print(self.dict_set)

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
                    if not this_dict.verify(word):
                        this_dict.user_prompt
                else:
                    continue
            else:
                continue
            
    except IOError:
        # FileNotFoundError IS NEW FOR 3.3! 3.2 uses IOError!
        print("***Unable to read file \'{}\'!***\n".format(f))
    except ExitByUser:
        # User chose 'e' to exit in prompt
        print('/n')
        # CLEANUP ACTIONS HERE
    
    