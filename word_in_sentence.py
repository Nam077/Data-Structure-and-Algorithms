def word_in_sentence(sentence):
    return sentence.split()


if __name__ == '__main__':
    print("Enter sentence: ")
    sentence_input = input()
    print("Words =", word_in_sentence(sentence_input))
