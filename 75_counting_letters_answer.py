# 75_counting_letters_answer.py

import collections

def solution_one(letters):
    letters = letters.lower()
    count = collections.Counter(letters)
    return count.most_common(3)


def solution_two(letters):
    letters = letters.lower()
    my_dict = {}
    for letter in letters:
        if letter in my_dict:
            my_dict[letter] += 1
        else:
            my_dict[letter] = 1
    sorted_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))
    return list(sorted_by_value.items())[-3:]

if __name__ == "__main__":
    # Find the top 3 letter counts in the following string:
    words = "The little red fox jumped over a fence and bit a python"
    print(f"Counter solution: {solution_one(words)}")
    print(f"Regular dict solution: {solution_two(words)}")