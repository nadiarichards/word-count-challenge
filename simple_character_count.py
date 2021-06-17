import re

def character_count(text_file):
    sample_text = open(text_file, "r")
    char_count=0

    for line in sample_text:
        line=line.strip().lower()
        line = re.sub(r'[^\w\s]','',line)
        words=line.split(" ")

        for word in words:
            word.split()
            for character in word:
                char_count+=1

    print (f"Total Characters: {char_count}")

character_count('sample3.txt')