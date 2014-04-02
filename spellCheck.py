import re
from dictionary import Dictionary

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
    output_string = ''
    try:
        # Prompt user for the name of a document she wants spell-checked.
        file_name = input("Name of the document to be spell-checked: ")
        file = open(file_name)
        # spellCheck should read words from the specified document,
        # one-by-one and test if the words appears in its dictionary.
        for line in file.readlines():
            word_list = parse_line(line)
            index = 0
            for word in word_list:
                if not this_dict.verify(word):
                    def user_prompt(word, index, line, dict_name):
                        print("\n{:^62}".format(word))
                        prompt = "replace(R), replace all(P), ignore(I), ignore all(N), exit(E): "
                        while True:
                            user_cmd = input(prompt)
                            user_cmd = user_cmd.lower()
                            if user_cmd == 'i':
                                return line
                                break
                            elif user_cmd == 'r':
                                replacement_word = input("Replacement word: ")
                                line = re.sub(word, replacement_word, line, flags=re.IGNORECASE)
                                return line
                                break
                            elif user_cmd == 'n':
                                dict_name.update('n', word)
                                return line
                                break
                            elif user_cmd == 'p':
                                replacement_word = input("Replacement word: ")
                                line = re.sub(word, replacement_word, line, flags=re.IGNORECASE)
                                dict_name.update('p', word, replacement=replacement_word)
                                return line
                                break
                            elif user_cmd == 'e':
                                raise ExitByUser
                            else:
                                continue
                    line = user_prompt(word, index, line, this_dict)
                else:
                    index += 1
                    continue
            else:
                checked_line = line
                for key in this_dict.replace_dict.keys():
                    repl = this_dict.replace_dict.get(key)
                    checked_line = re.sub(key, repl, checked_line, \
                                          flags=re.IGNORECASE)
                output_string += checked_line
                continue
    except IOError:
        # FileNotFoundError IS NEW FOR 3.3! 3.2 uses IOError!
        print("***Unable to read file \'{}\'!***\n".format(file_name))
    except ExitByUser:
        # User chose 'e' to exit in prompt
        pass
    finally:
        file.close()
        output_name = file_name + '.out'
        output = open(output_name, 'w')
        output.write(output_string)