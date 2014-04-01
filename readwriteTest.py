import fileinput
import sys

def main():
    
    for line in fileinput.input('shortalice2.txt', inplace=True):
        line = line.replace('Alice', 'YOZINZ')
        sys.stdout.write(line)

main()