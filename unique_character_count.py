import re
from 

sample_text = open("sample3.txt", "r")
dict = {}

for line in sample_text:
    line=line.strip().lower()
    line = re.sub(r'[^\w\s]','',line)
    words=line.split(" ")

    for word in words:
        word.split()
        for character in word:
            if character in dict:
                dict[character] = dict[character]+1
            else:
                dict[character] =1

for char in sorted (dict):
    print (char, ":", dict[char], /n)


# for key in list(dict.keys()):
#     print(key, ":", dict[key])