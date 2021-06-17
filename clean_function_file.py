import re
import nltk
import nltk.data
from nltk.tokenize import sent_tokenize
nltk.download('punkt')

def upscaled_word_counter(text):
    text = open(sample, 'r')

    sample_text = open("sample3.txt")
    raw=sample_text.read()

sentences=nltk.sent_tokenize(raw)

print (f"Total Sentences: {len(sentences)}")


