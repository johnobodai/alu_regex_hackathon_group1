#!/usr/bin/python3
import re


#My codes will be allowing twittter users to creat their twitter handles using any character
def TwitterUsername(txt):
    return (re.search("@w+", txt))
