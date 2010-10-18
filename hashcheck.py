#!/usr/bin/env python
# encoding: utf-8


import sys,os

try :
	alg = sys.argv[1]
	datei = sys.argv[2]
	value = sys.argv[3]
except :
	print ("USAGE: python3 hashcheck.py <md5/sha1> <file> <checksum>")
	exit()

rv = os.popen("openssl "+ alg + " " + datei).read()

rv_split = rv.split("=")					
hashvalue = rv_split[1]
length = len(hashvalue)
rvo = (hashvalue [:length-1])
rvz = len(rvo)
rvf = (rvo [1:rvz])

value_l = value.lower()

if value_l == rvf :
	print ("Ok")
else :
	print ("false")
		
