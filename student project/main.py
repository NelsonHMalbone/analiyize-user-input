"have user input a series of numbers"

# input the numbers
print('Enter a series of numbers separated by spaces')
prompt = input() # is a string
" first time go around befroe converting to a int type"
#lengthOfNumbers = len(prompt.split())

"better way in less complex way of turing a str to a int"
# coverting input to a intergers
number_list = [int(num) for num in prompt.split()]



# Results
print("Number Analysis Results")
print('-'*22)
print(f"The total number of entries: {len(number_list)}")
print(f"The sum of the numbers: {sum(number_list)}")
#print(f'The range of the numbers: {}')
#print(f'The most frequent number: {}')
#print(f'The average of the numbers: {}')

"""
results 
wil show the sum average range frequent of numbers 
"""