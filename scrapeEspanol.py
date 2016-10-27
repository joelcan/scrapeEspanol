#!/usr/bin/env python

"""
scrapeEspanol:
Scrape all verb conjugations from SpanishDict.com for a specific verb.
"""

from __future__ import print_function #This *must* be the first line
import sys

#TODO: Handle when infinitive is not found.
#TODO: Handle when not all conjugations are listed.
#TODO: Convert parameter to lower case.

def scrapeWebpage():

def displayUsage():
    print("Usage:")
    print("  scrapeEspanol <infinitive>")
    print("It saves a CSV file containing all the conjugations.")

def main():
    """Handle command line parameters"""
    if len(sys.argv) != 1:
        displayUsage()
    scrapeWebpage("http://www.spanishdict.com/conjugate/", sys.argv[1])

if __name__ == "__main__":
    main()

