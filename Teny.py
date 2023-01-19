#!/usr/bin/python3
# Python regex that matches jokes that start with "Why did the....? and preceeded by Because..."
import re
from pyfiglet import Figlet
from termcolor import colored


f = Figlet(font='standard')
print(colored(f.renderText('RegEx Made Easy'), 'white'))

def Jokes(txt):
    return (re.search("Why did the \w+? Because \w+", txt))