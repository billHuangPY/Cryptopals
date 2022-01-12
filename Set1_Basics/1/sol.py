## Set1-1: Convert hex to base64

## Problem
the_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
should_produce = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

## Solution
import base64
fromhex_string = bytes.fromhex(the_string)
base64_string = base64.b64encode(bytes.fromhex(the_string))
output_string = base64_string.decode("utf-8")

assert output_string == should_produce