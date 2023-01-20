#!/usr/bin/python3
import re

#My code will be allowing user to create the twitter handles with any characters
def Twitterusername(txt):
    return (re.search("@\w+", txt))
# Python regex that matches jokes that start with "Why did the....? and preceeded by Because..."
import re
from pyfiglet import Figlet
from termcolor import colored


f = Figlet(font='standard')
print(colored(f.renderText('RegEx Made Easy'), 'white'))

def Jokes(txt):
    return (re.search("Why did the \w+? Because \w+", txt))
