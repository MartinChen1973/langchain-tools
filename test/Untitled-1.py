# Given an integer n
n = int(input("Enter a number: "))

# build an array [n, n+1, ..., 0] (from n to zero), or [0, 1, ..., n] if n >= 0
ints = list(range(n+1)) if n >= 0 else list(range(n, 1))

# build an array [1, 2, 4, 8, ..., 2^63]
powers_of_two = [2**i for i in range(64)]

# build an empty int list named num_ones with the same number of ints.
num_ones = [0] * len(ints)

# foreach of the int in ints, sum the number of power_of_two in powers_of_twos which matches "int & power_of_two == power_of_two"
for i, value in enumerate(ints):
    num_ones[i] = sum(1 for power in powers_of_two if value & power)

# Determine the bit length for the two's complement representation
bit_length = max(max(ints).bit_length(), abs(min(ints)).bit_length()) + 1

# Print each int and its binary (two's complement for negatives) representation
print("Integers and their binary (two's complement for negatives) representation:")
for value in ints:
    binary_representation = format(value & ((1 << bit_length) - 1), f'0{bit_length}b')
    print(f"{value} = {binary_representation}")

print()  # New line for separation
print("Number of powers of two:", num_ones)
