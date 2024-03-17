"""
Word Occurrences Program
Estimate: 15 minutes
Actual: 18 minutes
"""
def main():
    text = input("Text: ")
    word_counts = count_words(text)
    longest_word = max(len(word) for word in word_counts)

    for word in sorted(word_counts):
        print(f"{word:{longest_word}} : {word_counts[word]}")



def count_words(text):
    words = text.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts



if __name__ == "__main__":
    main()
