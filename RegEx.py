#!/usr/bin/python3
import re

from pyfiglet import Figlet
from termcolor import colored


f = Figlet(font='standard')
print(colored(f.renderText('RegEx Made Easy'), 'white'))

def Jokes(txt):
    return (re.search("Why did the \w+? Because \w+", txt))

def MovieTitle(txt):
    return (re.search("\w+\s\d{4}", txt))

def SongLyrics(txt):
    return (re.search("Verse \d \w+", txt))

#My codes will be allowing twittter users to creat their twitter handles using any character
def TwitterUsername(txt):
    return (re.search("@w+", txt))

def TVEpisodeTitles(txt):
    return ("\w+ S\d\dE\d\d: \w+")

def ISBNnumbers(txt):
    return (re.search("ISBN \d{3}-\d-\d{3}-\d{5}-\d", txt)
# print(ISBNnumbers("ISBN 616-1-101-536790"))

def TVEpisodeTitles(txt):
    return ("\w+ S\d\dE\d\d: \w+")

def HexColorCode(txt):
    return ("#[a-zA-Z0-9]{6}")

def IPAddress(txt):
    return ("\d{3}\.\d{3}\.{3}\.{3}")  # "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
