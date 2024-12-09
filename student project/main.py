# inputs
# gonna need a user input

# prompt = input("Enter a block of text for analysis:\n")
# or
print("Enter a block of text for analysis:")
prompt = input()

# calculate number of chars
total_chars = len(prompt)

# calculate number of words
total_words = len(prompt.split())

# calculate number of sentences
"""
so to get all possible cases would use
the re library but for simple use just 
work with the count method

can also + prompt.count('!') or ?
"""
total_sentence = (prompt.count('.') +
                  prompt.count('!') +
                  prompt.count('?'))

# results
print('Text Analysis Results:')
#print("----------------------")
# or
print('-' * 22)
print(f'Total Characters: {total_chars}')
print(f'Total Words: {total_words}')
print(f'Total Sentences: {total_sentence}')

# result will be a print statement
"""
showing the total chars words and sentences
most frequent word
average word length
and average sentence lenght

"""