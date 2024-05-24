#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]

# Example usage
print(return_evens([0, 1, 3, 5, 7, 8, 9]))  # Output: [0, 8]


def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]

# Example usage
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))  
# Output: ["Hello!", "I'm doing great!", "Python is fun!"]
