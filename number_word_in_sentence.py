def number_word_in_sentence(sentence):
    return len(sentence.split())


if __name__ == '__main__':
    print("Enter sentence: ")
    sentence_input = input()
    print("Number of words =", number_word_in_sentence(sentence_input))
