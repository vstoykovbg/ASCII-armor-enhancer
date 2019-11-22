#!/usr/bin/python3

import sys

import argparse

parser = argparse.ArgumentParser(description='Encoding ASCII armored data by replacing some characters with different Unicode characters. STDIN and STDOUT are being used for input and oputput data.')
parser.add_argument("--action", 
                    choices=["encode", "decode"],
                    required=False, type=str, default="encode", help="Encode or decode")

args = parser.parse_args()

action = args.action

tab1 = "Q0lIG"
tab2 = "ЯθлДЖ"

if action == "encode":
    intab =  tab1
    outtab = tab2
elif action == "decode":
    intab =  tab2
    outtab = tab1

trantab = str.maketrans(intab, outtab)

data = sys.stdin.buffer.read()

data = data.decode()

data = data.translate(trantab)

sys.stdout.write(data)
