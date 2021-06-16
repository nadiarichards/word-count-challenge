import re

sample_text = open("sample3.txt", "r")
word_count=0

for line in sample_text:
    line=line.strip()
    line = re.sub(r'[^\w\s]','',line)
    words=line.split(" ")

    for word in words:
        word_count+=1

print(word_count)