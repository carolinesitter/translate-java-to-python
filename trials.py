"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    # create for loop, iterate through items
    for item in items:
        print(item)


def get_all_evens(nums):
    # create empty list and for loop for even numbers
    even_numbers = []

    for num in nums:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


def get_odd_indices(items):
    # iterate through items and return odd index
    result = []
    for idx in range(len(items)):
        if idx % 2 != 0:
            result.append(items[idx])
        
    return result


def print_as_numbered_list(items):
    # create a numbered list of items
    i = 1

    for item in items:
        print(f"{i}. {item}")
        i += 1


def get_range(start, stop):
    # returns a list of each number between start and stop
    nums = []

    for num in range(start,stop):
        nums.append(num)

    return nums


def censor_vowels(word):
    # replaces vowels in a word with *, leaves nonvowels alone

    chars = []

    for letter in word:
        if letter in "aeiou":
            chars.append("*")
        else:
            chars.append(letter)

    return "".join(chars)


def snake_to_camel(string):
    # make list full of camel case 
    camelCase = []

    for word in string.split("_"):
        camelCase.append(f"{word[0].upper()}{word[1:]}")

    return "".join(camelCase)
    


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
