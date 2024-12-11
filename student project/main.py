"have user input a series of numbers"

# input the numbers
print('Enter a series of numbers separated by spaces')
prompt = input() # is a string
" first time go around befroe converting to a int type"
#lengthOfNumbers = len(prompt.split())

"better way in less complex way of turing a str to a int"
# coverting input to a intergers
number_list = [int(num) for num in prompt.split()]

# adding to a list to group
nums_frequency = {}
for nums in nums_frequency:
    if nums not in nums_frequency:
        nums_frequency[nums] = 1
    else:
        nums_frequency[nums] += 1



# calculations
number_totals = len(number_list)
number_sum = sum(number_list)
most_frequent_number = max(nums_frequency, key=nums_frequency.get)





# Results
print("Number Analysis Results")
print('-'*22)
print(f"The total number of entries: {number_totals}")
print(f"The sum of the numbers: {number_sum}")
print(f'The max amount of numbers: {most_frequent_number}')
#print(f'The most frequent number: {}')
#print(f'The average of the numbers: {}')

"""
results 
wil show the sum average range frequent of numbers 
"""