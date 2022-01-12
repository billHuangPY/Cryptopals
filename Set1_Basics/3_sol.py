## Set1-3: Single-byte XOR cipher

## Problem
encoded_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

## Solution
from string import ascii_letters
import re


def get_keyhex(key, length):
    """
    Make the single character key fit the length of encoded string,
    And make it hex string
    """
    return (key * length).encode("ascii").hex()


def get_decodedhex(input_string, key_string):
    """
    XOR the encoded string and the generated key string,
    make it hex string, remove the '0x' part of the string
    """
    return hex(input_string ^ int(key_string, base=16))[2:]


len_string = int(len(encoded_string) / 2)
int_string = int(encoded_string, base=16)
for key in ascii_letters:
    hex_key = get_keyhex(key, len_string)
    decoded_hex = get_decodedhex(int_string, hex_key)
    try:
        decoded_string = bytes.fromhex(decoded_hex).decode("ascii")
        filtered_string = re.sub(r"[\x00-\x1F]+", "", decoded_string)
        print(key, ":", filtered_string)
    except:
        pass
