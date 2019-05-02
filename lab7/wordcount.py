#!/bin/usr/python

# Input format: python3 wordcount.py [input file] [output file]
import sys

ip = open(sys.argv[1], "r").read()
op = open(sys.argv[2], "w")

def wrdcnt (x):
    ar = x
    ar = ar.replace("\n", " ")
    rem = [',', '.', '"', ';', ':', '!', '?', ')', '(']
    for i in rem:
        ar = ar.replace(i, "")
    words = ar.split(" ")
    ans = {}
    for i in words:
        if ans.get(i) == None:
            ans[i] = 1
        else:
            ans[i] = ans[i] + 1
    for key in ans:
	    if key != '':
	    	op.write(key + ": " + str(ans[key]) + "\n")
    return ans

wrdcnt(ip)
