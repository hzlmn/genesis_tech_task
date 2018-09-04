from collections import deque


def palindrome(string):
    seq = deque()

    for char in string:
        seq.append(char)

    while len(seq) > 1:
        left = seq.popleft()
        right = seq.pop()

        if left != right:
            return False

    return True


def replace_id(string, idx):
    return string[:idx] + string[idx+1:]


def palindromIndex(string):
    if palindrome(string):
        return -1

    for idx, char in enumerate(string):
        if palindrome(replace_id(string, idx)):
            return idx


print(palindromIndex("baa"))
