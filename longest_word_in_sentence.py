def longest_word(sentence: str):
    words = sentence.split()
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


if __name__ == '__main__':
    print("Enter sentence: ")
    sentence_input = input()
    print("Longest word =", longest_word(sentence_input))
