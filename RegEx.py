#!/usr/bin/python3
import re

def Twitterusername(txt):
    return (re.search("@\w+", txt))

