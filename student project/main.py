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



# results
print('Text Analysis Results:')
#print("----------------------")
# or
print('-' * 22)
print(f'Total Characters: {total_chars}')
print(f'Total Words: {total_words}')

# result will be a print statement
"""
showing the total chars words and sentences
most frequent word
average word length
and average sentence lenght

"""