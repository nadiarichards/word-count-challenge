import re

sample_text = open("sample3.txt", "r")
char_count=0

for line in sample_text:
    line=line.strip().lower()
    line = re.sub(r'[^\w\s]','',line)
    words=line.split(" ")

    for word in words:
        word.split()
        for character in word:
            char_count+=1

print (char_count)
