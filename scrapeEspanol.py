#!/usr/bin/env python

"""
scrapeEspanol:
Scrape all verb conjugations from SpanishDict.com for a specific verb.
"""

from __future__ import print_function #This *must* be the first line
import sys
import urllib2
from bs4 import BeautifulSoup
import re

#TODO: Handle when infinitive is not found.
#TODO: Handle when not all conjugations are listed.
#TODO: Convert parameter to lower case.
#TODO: Allow inputting a csv file that contains a list of infinitives to process.

def cleanText(string):
    if string.startswith('&nbsp'):
        string = string[5:]
    if string.endswith(';'):
        string = string[:-1]
    return string

def removeTags(string):
    cleanre = re.compile('<.*?>')
    cleanString = re.sub(cleanre, '', string)
    return cleanString

def scrapeWebpage(url):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")

    gerund = cleanText(soup.find(text='Gerund:').findNext('span').string)
    print(gerund)

    participle = cleanText(soup.find(text='Participle:').findNext('span').string)
    print(participle)
    print('---')

    items = soup.findAll('td', {'class': 'vtable-word'})
    for item in items[:60]:
        word = removeTags(str(item))
        print(word)


def displayUsage():
    print("Usage:")
    print("  scrapeEspanol <infinitive>")
    print("It saves a CSV file containing all the conjugations.")

def main():
    """Handle command line parameters"""
    if len(sys.argv) != 2:
        displayUsage()
    else:
        scrapeWebpage(
                'http://www.spanishdict.com/conjugate/{}'.format(sys.argv[1]))

if __name__ == "__main__":
    main()

