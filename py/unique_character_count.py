import re

def unique_character_count(text_file):

    sample_text = open(text_file, "r")
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

    for k, v in sorted (dict.items()):
        print (k, ':', v)

unique_character_count('../sample3.txt')
