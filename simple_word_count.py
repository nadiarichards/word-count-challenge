import re

def word_count(text_file):

    sample_text = open(text_file, "r")
    word_count=0

    for line in sample_text:
        line=line.strip()
        line = re.sub(r'[^\w\s]','',line)
        words=line.split(" ")

        for word in words:
            word_count+=1

    print (f"Total Words: {word_count}")

word_count('sample3.txt')

