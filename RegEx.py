#!/usr/bin/python3
import re

#My code will be allowing user to create the twitter handles with any characters
def Twitterusername(txt):
    return (re.search("@\w+", txt))

