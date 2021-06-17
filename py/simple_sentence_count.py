import nltk
import nltk.data
from nltk.tokenize import sent_tokenize
nltk.download('punkt')

def sentence_count(text_file):

    sample_text = open(text_file)
    raw=sample_text.read()

    sentences=nltk.sent_tokenize(raw)

    print (f"Total Sentences: {len(sentences)}")

sentence_count('../sample3.txt')