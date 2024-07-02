
def count_bits(n):
    """" Returns the number of '1' in the binary expression of the parameter 'n' """
    if type(n) != int or n < 0:
        raise Exception("Only positive integers parameters are allowed")
    binary_output = bin(n)[2:]
    print(binary_output)
    return len(binary_output.replace("0", ""))


print(count_bits(1234))
