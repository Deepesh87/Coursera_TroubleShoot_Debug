#!/usr/bin/env python3

import argparse

"""
argparse is used to pass any data structure from the CLI (example a list)
for passing simple numbers, we can use sys.argv.

An example of calling this py file is 

./linear_search --any_list 1 4 3 2 1 55  --key 4

will return 1 as 4 is present at index 1
"""



CLI=argparse.ArgumentParser()

CLI.add_argument(
'--any_list', # name on the CLI -drop the -- for positional argument
nargs='*',
type=int,
)


CLI.add_argument(
"--key",
#nargs='*',
type=int,
)


args=CLI.parse_args()

any_list=args.any_list
key=args.key


def linear_search(any_list,key):
    """If key is in the list return
    its position else return -1"""
    for position,element in enumerate(any_list):
        if element==key:
            return position
    return -1


print(linear_search(any_list,key))
