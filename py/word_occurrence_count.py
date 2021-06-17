def word_occurrence(text_file, word):

    sample_text = open(text_file, "r")
    data = sample_text.read()

    occurrences = data.count(word)

    print (f'Number of Occurrences of the word "{word}": {occurrences}')

word_occurrence('sample3.txt', 'esse')