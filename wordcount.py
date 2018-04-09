def word_count(filename):
    import string


    text_to_count = open(filename)

    word_count_pairs = {}

    for line in text_to_count:
        tokenized_line = line.strip("\n").lower().split(" ")
#.strip(string.punctuation)


        for word in tokenized_line:
            #add words to dictionary
            word = word.strip(string.punctuation)
            word_count_pairs[word] = word_count_pairs.get(word, 0) + 1
                # word_count_pairs[word] += 1

    print word_count_pairs

word_count("test.txt")
