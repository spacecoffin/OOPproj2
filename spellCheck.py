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
    
    def user_prompt(self, word, index):
        print("\n{:^62}".format(word))
        prompt = "replace(R), replace all(P), ignore(I), ignore all(N), exit(E): "
        while True:
            user_cmd = input(prompt)
            user_cmd = user_cmd.lower()
            if user_cmd == 'i':
                break
            elif user_cmd == 'r':
                replacement_word = input("Replacement word: ")
                split_line[index] = replacement_word
                break
            elif user_cmd == 'n':
                this_dict.update('n', index)
                break
            elif user_cmd == 'p':
                replacement_word = input("Replacement word: ")
                split_line[index] = replacement_word
                this_dict.update('p', word, replacement=replacement_word)
                break
            elif user_cmd == 'e':
                raise ExitByUser
            else:
                continue

    def __iter__(self):
        return self
    
    def __next__(self):
        pass

class ExitByUser(Exception):
    pass

def parse_line(line):
    split_line = re.split(r'[^a-z]+', line, flags=re.IGNORECASE)
    word_list = []
    lower_list = []
    for x in split_line:
        if len(x) >= 1:
            if x.lower() not in lower_list:
                word_list.append(x)
                lower_list.append(x.lower())
            else:
                continue
        else:
            continue
    return word_list

if __name__ == '__main__':
    this_dict = Dictionary()
    try:
        # Prompt user for the name of a document she wants spell-checked.
        file_name = input("Name of the document to be spell-checked: ")
        file = open(file_name)
        file_out_name = file_name + '.tmp'
        output = open(file_out_name, 'w')
        # spellCheck should read words from the specified document,
        # one-by-one and test if the words appears in its dictionary.
        for line in file.readlines():
            word_list = parse_line(line)
            index = 0
            for word in word_list:
                if not this_dict.verify(word):
                    this_dict.user_prompt(word, index)
                else:
                    index += 1
                    continue
            else:
                for 
                """
                for replacement in this_dict.replace_dict():
                    this_dict.replace_dict[]
                    checked_line = re.sub()
                output.write(checked_line)
                """
                continue
    except IOError:
        # FileNotFoundError IS NEW FOR 3.3! 3.2 uses IOError!
        print("***Unable to read file \'{}\'!***\n".format(file_name))
    except ExitByUser:
        # User chose 'e' to exit in prompt
        # CLEANUP ACTIONS HERE
        pass