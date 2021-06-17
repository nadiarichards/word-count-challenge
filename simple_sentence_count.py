import nltk
import nltk.data
from nltk.tokenize import sent_tokenize
nltk.download('punkt')

sample_text = open("sample3.txt")
raw=sample_text.read()

sentences=nltk.sent_tokenize(raw)

print (f"Total Sentences: {len(sentences)}")
