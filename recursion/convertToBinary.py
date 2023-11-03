def decimalToBinary(n):
    assert int(n)==n, "n must be a whole integer only"
    if n == 0:
        return 0
    else:
        return n%2 + 10*decimalToBinary(int(n/2))


# print(decimalToBinary(10))


# support for fractions and decimals
def decimalToBinary(n, decimal_places=0):
    if n == 0:
        return 0
    else:
        integer_part = int(n)
        binary = integerToBinary(integer_part)
        fractional_part = n - integer_part

        if decimal_places > 0:
            binary += "."
            for _ in range(decimal_places):
                fractional_part *= 2
                bit = int(fractional_part)
                binary += str(bit)
                fractional_part -= bit

        return binary

def integerToBinary(n):
    if n == 0:
        return ""
    else:
        return integerToBinary(n // 2) + str(n % 2)

# Example usage:
print(decimalToBinary(10.625, 3))  # Converts 10.625 with 3 decimal places to binary

