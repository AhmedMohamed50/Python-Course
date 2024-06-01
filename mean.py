# in the code below: the for loop goes for each string so i can't give range(n), instead i should give str_n
# ❌🔴🟥❎ False Code
# def mean_of_digits(n):
#     sum = 0
#     str_n = str(n)
#     for digit in range(n):
#         sum += int(digit)
#     return sum / len(str_n)

# 🟩✅🟢 Right code
def mean_of_digits(n):
    sum = 0
    str_n = str(n)
    for digit in str_n:
        sum += int(digit)
    return sum / len(str_n)


def mean_of_digits(n):
    return sum(int(digit) for digit in str(n)) / len(str(n))


def mean_of_digits(n):
    # Convert the number to a string to iterate over its digits
    n_str = str(n)
    
    # Calculate the sum of the digits
    digit_sum = 0
    for digit in n_str:
        digit_sum += int(digit)
    
    # Calculate the mean of the digits
    mean = digit_sum / len(n_str)
    
    return mean

# Example usage
n = 12345
result = mean_of_digits(n)
print("Mean of digits:", result)
