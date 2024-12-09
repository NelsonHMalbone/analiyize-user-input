# creating a function to remove punctuation to clean the text
def remove_punctuation(prompt):
    punctuation = ".,!?:;'\"(){}[]"
    for char in punctuation:
        prompt = prompt.replace(char, "")
    return prompt

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


# most frequant word
"build data structure"
word_frequecy = {}
#list of all the words
# word_list = prompt.lower().split() # this was used before the function was created
word_list = remove_punctuation(prompt).lower().split()
# ilterate over the words in block of text
for word in word_list:
    # if word is not in dictionary will add
    if not word in word_frequecy:
        word_frequecy[word] = 1
    else:
        # if word is in dictionary in sees word again it adds 1 to the dictionary
        word_frequecy[word] += 1

# print(word_frequecy) just shows the dictionary
most_used = max(word_frequecy, key=word_frequecy.get)
# print(most_used)



# results
print('Text Analysis Results:')
#print("----------------------")
# or
print('-' * 22)
print(f'Total Characters: {total_chars}')
print(f'Total Words: {total_words}')
print(f'Total Sentences: {total_sentence}')

"""
{word_frequecy[most_used]
using [most_used] as the key for word_frequecy value
"""
print(f'Most Frequent word: {most_used} (used {word_frequecy[most_used]} times)')

# result will be a print statement
"""
showing the total chars words and sentences
most frequent word
average word length
and average sentence lenght

"""