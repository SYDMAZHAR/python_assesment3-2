def sum_of_numbers(num_list):
    total = sum(num_list)
    return total

# Sample List
sample_list = [8, 2, 3, 0, 7]

# Calculating the sum
result = sum_of_numbers(sample_list)

# Printing the result
print("Expected Output:", result)



def reverse_string(input_str):
    return input_str[::-1]

sample_string = "1234abcd"
reversed_string = reverse_string(sample_string)
print("Sample String:", sample_string)
print("Reversed String:", reversed_string)
