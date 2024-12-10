"have user input a series of numbers"

# input the numbers
print('Enter a series of numbers separated by spaces')
prompt = input() # is a string
lengthOfNumbers = len(prompt.split())

# coverting input to a intergers
number_list = [int(num) for num in prompt.split()]



# Results
print("Number Analysis Results")
print('-'*22)
print(f"Total Numbers: {lengthOfNumbers}")
print(f"Sum of Numbers: {sumTotal}")

"""
results 
wil show the sum average range frequent of numbers 
"""