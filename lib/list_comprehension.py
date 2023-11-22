#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = []
    for i in num_list:
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers


def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]