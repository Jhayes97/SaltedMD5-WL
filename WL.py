#!/usr/bin/python3

import hashlib

saltPrefix = "FCC"
saltSuffix = "Cyber"
hashedPass = "0f28845d31dbabc9ba6bab4f06cdc11a"
dictionaryAbsoluteFilePath = '/home/clay/Documents/Brute/rockyou.txt'


f = open(dictionaryAbsoluteFilePath,'r',encoding='utf-8')
lines = f.read().splitlines()

for line in lines: 
    saltedString = saltPrefix + line + saltSuffix
    x = hashlib.md5((saltedString).encode('utf-8')).hexdigest()
    if x.lower() == hashedPass.lower():
        print("The password is: " + line)
