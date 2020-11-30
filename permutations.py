#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 12:32:34 2020

@author: silasjimmy
"""

def permutations(sequence):
    # Return nothing if sequence is an empty string
    if len(sequence) == 0:
        return
    
    # Return a list containing only sequence if sequence is of length 1
    if len(sequence) == 1:
        return [sequence]
    
    # List to store all the permutations of sequence
    sequence_permutations = []
    
    # Get the list of the permutations
    permutated_sequences = permutations(sequence[1:])
    
    for ps in permutated_sequences:
        # Create a list of the permutation
        sequence_list = list(ps)
        for i in range(len(sequence)):
            # Create a copy of the permutation
            sequence_list_copy = sequence_list[:]
            # Insert the first letter of sequence in each position in the permutation
            sequence_list_copy.insert(i, sequence[0])
            # Add the created permutation to the permutations list
            sequence_permutations.append(''.join(sequence_list_copy))
    
    return sequence_permutations

print(permutations('abcd'))