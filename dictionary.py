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
            self.ignore_set.add(add_word.lower())
        elif update_cmd == 'p':
            self.replace_dict[add_word.lower()] = replacement