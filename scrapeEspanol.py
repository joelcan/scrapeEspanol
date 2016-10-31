#!/usr/bin/env python

"""
scrapeEspanol:
Scrape all verb conjugations from SpanishDict.com for a specific verb.
"""

from __future__ import print_function #This *must* be the first line
import sys
import urllib2
from bs4 import BeautifulSoup

#TODO: Handle when infinitive is not found.
#TODO: Handle when not all conjugations are listed.
#TODO: Convert parameter to lower case.
#TODO: Allow inputting a csv file that contains a list of infinitives to process.

def scrapeWebpage(url):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")

    curr = soup.find(text='Gerund:')
    while getattr(curr, 'name', None) != 'span':
        curr = curr.next
    gerund = curr.string
    if gerund.startswith('&nbsp'):
        gerund = gerund[5:]
    if gerund.endswith(';'):
        gerund = gerund[:-1]
    print(gerund)

    curr = soup.find(text='Participle:')
    while getattr(curr, 'name', None) != 'span':
        curr = curr.next
    participle = curr.string
    if participle.startswith('&nbsp'):
        participle = participle[5:]
    if participle.endswith(';'):
        participle = participle[:-1]
    print(participle)

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

