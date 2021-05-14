#!/usr/bin/env python3

import argparse

CLI=argparse.ArgumentParser()

CLI.add_argument(
'--sorted_list',
nargs='*',
type=int,
)

CLI.add_argument(
'--key',
type=int,
)

args=CLI.parse_args()
sorted_list=args.sorted_list
key=args.key


def binary_search(sorted_list,key):
	"""
	returns the postion of the key in the sorted list else returns -1
	"""
	start=0
	end=len(sorted_list)-1
	while start<=end:
		mid=(end+start)//2
		if sorted_list[mid]==key:
			return mid
		elif sorted_list[mid]>key:
			end=mid-1
		else:
			start=mid+1

	return -1

print(binary_search(sorted_list,key))
