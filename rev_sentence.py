def reverse(input):
    split=input.split()
    rev_words=split[::-1]
    rev_sentence=" ".join(rev_words)
    return rev_sentence