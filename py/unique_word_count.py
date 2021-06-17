import re

def unique_word_count(text_file):

    sample_text = open(text_file, "r")
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
        if dict[key] >= 5:
            print(key, ":", dict[key])

unique_word_count('../sample3.txt')