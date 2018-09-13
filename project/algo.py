def lookup_word(word, text, words_shift=2):
    word = word.strip().split(" ")
    text = text.strip().split(" ")

    cursor = 0
    index = 0
    skipped = 0

    while cursor < len(text):
        curr_word = text[cursor]
        part = word[index]

        if curr_word == part:
            if index == len(word) - 1:
                return True

            skipped = 0
            index += 1
        else:
            if skipped < words_shift:
                skipped += 1
            else:
                index = 0
                skipped = 0

        cursor += 1

    return False
