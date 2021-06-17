# def insert_line_para_nums(text):
#     text = open(text, 'r')

import re
from collections import Counter
# from itertools import islice, izip

# sample_text = open("sample3.txt", "r")

words = re.findall('\w+', open('sample3.txt').read())
bigram_counter=Counter(zip(words, words[1:]))

for k, v in bigram_counter.items():
    print (k, ':', v)
# print (Counter(zip(words, words[1:])))

# line_count = 0
# paragraph_count = 0
# empty = True
# for i in sample_text:
#     if '\n' in i:
#         line_count += 1
#         if len(i) < 2:
#             empty = True
#         elif len(i) > 2 and empty is True:
#             paragraph_count += 1
#             empty = False
#         if empty is True:
#             paragraph_number = 0
#     else:
#             paragraph_number = paragraph_count
# sample_text.close()

# print (f"Total Paragraphs: {paragraph_count} \nTotal Lines: {line_count}")
