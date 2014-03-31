class Dictionary:
    def __init__(self):
        # This program should start by reading the list of words in the
        # file words.dat into a data structure that can be quickly
        # searched.
        dict_file = open("words.dat")
        for word in dict_file:
            dict_list = []
            dict_list.append(dict_file.readline(word))
        return dict_list