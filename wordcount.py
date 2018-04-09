def word_count(filename):
    text_to_count = open(filename)

    word_count_pairs = {}

    for line in text_to_count:
        tokenized_line = line.strip("\n").split(" ")

        for word in tokenized_line:
            word_count_pairs[word] = word_count_pairs.get(word, 0) + 1
            # word_count_pairs[word] += 1

    print word_count_pairs

word_count("test.txt")
