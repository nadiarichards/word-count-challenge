import re

sample_text = open("sample3.txt", "r")
dict = {}

for line in sample_text:
    line=line.strip().lower()
    line = re.sub(r'[^\w\s]','',line)
    words=line.split(" ")

    for word in words:
        if word in dict:
            dict[word] = dict[word]+1
        else:
            dict[word] =1

for key in list(dict.keys()):
    print(key, ":", dict[key])