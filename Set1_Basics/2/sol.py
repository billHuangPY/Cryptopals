## Set1-2: Fixed XOR

## Problem
the_string = '1c0111001f010100061a024b53535009181c'
XORd_against = '686974207468652062756c6c277320657965'
should_produce = '746865206b696420646f6e277420706c6179'

## Solution
XOR_output = int(the_string, base=16) ^ int(XORd_against, base=16)
output_string = hex(XOR_output)[2:]

assert output_string == should_produce