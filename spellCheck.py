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
    
    def print(self):
        print(self.dict_set)
       
    
if __name__ == '__main__':
    marvin = Dictionary()
    marvin.print()