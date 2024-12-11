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

for number in number_list:
    if number not in nums_frequency:
        nums_frequency[number] = 1
    else:
        nums_frequency[number] += 1




# Calculate statistics
number_totals = len(number_list)
number_sum = sum(number_list)
most_frequent_number = max(nums_frequency, key=nums_frequency.get)
number_average = round(number_sum/number_totals, 2)
number_range = max(number_list) - min(number_list)




# Results
print("Number Analysis Results")
print('-'*22)
print(f"The total number of entries: {number_totals}")
print(f"The sum of the numbers: {number_sum}")
print(f'The max amount of numbers: {most_frequent_number},(appears {nums_frequency[most_frequent_number]} times)')
print(f"Average Number: {number_average}")
print(f'Range of Numbers: {number_range}')

"""
results 
wil show the sum average range frequent of numbers 
"""