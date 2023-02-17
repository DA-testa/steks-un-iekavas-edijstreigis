# Edijs Treiģis 221RDB338 17.grupa

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i + 1))
            pass

        if next in ")]}":
            if not opening_brackets_stack:return i + 1
            if not are_matching((opening_brackets_stack.pop()).char,next):
                return i + 1
            pass
    if opening_brackets_stack:return opening_brackets_stack[0].possition
    return"Succes"


def main():
    text = input()
    mismatch = find_mismatch(text)
    if "I" in text: print(find_mismatch(input()))

if __name__ == "__main__":
    main()
