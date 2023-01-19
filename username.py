#!/usr/bin/python3
import re

def TwitterUsername(txt):
    return (re.search("@\w+",txt))
