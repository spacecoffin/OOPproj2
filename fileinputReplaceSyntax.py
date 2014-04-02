import fileinput

for line in fileinput.FileInput("shortalice2.txt",inplace=1):
    if "Alice" in line:
         line=line.replace("Alice","WOWZERN")
    print line