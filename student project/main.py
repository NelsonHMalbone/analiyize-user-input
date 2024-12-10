"have user input a series of numbers"

# input the numbers
print('Enter a series of numbers separated by spaces')
prompt = input()

lengthOfNumbers = len(prompt.split())

# Results
print("Number Analysis Results")
print('-'*22)
print(f"Total Numbers: {lengthOfNumbers}")

"""
results 
wil show the sum average range frequent of numbers 
"""