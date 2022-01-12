## Set1-2: Fixed XOR

## Problem
the_string = "1c0111001f010100061a024b53535009181c"
xor_against = "686974207468652062756c6c277320657965"
should_produce = "746865206b696420646f6e277420706c6179"

## Solution
def xor_from_hexstring(var1, var2):
    """
    The XOR operator '^' only takes integer. And return integer
    Hence, convert the hex string to integer with base 16, then xor by the operator.
    """
    return int(var1, base=16) ^ int(var2, base=16)


xor_output = xor_from_hexstring(the_string, xor_against)
output_string = hex(xor_output)[2:]

assert output_string == should_produce
