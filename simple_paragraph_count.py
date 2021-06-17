def paragraph_and_line_count(text_file):

    sample_text = open(text_file, "r")
    line_count = 0
    paragraph_count = 0
    empty = True
    for i in sample_text:
        if '\n' in i:
            line_count += 1
            if len(i) < 2:
                empty = True
            elif len(i) > 2 and empty is True:
                paragraph_count += 1
                empty = False
            if empty is True:
                paragraph_number = 0
        else:
                paragraph_number = paragraph_count

    print (f"Total Paragraphs: {paragraph_count} \nTotal Lines: {line_count}")

paragraph_and_line_count('sample3.txt')