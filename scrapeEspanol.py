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
import csv
import io

#TODO: Handle when infinitive is not found.
#TODO: Handle when not all conjugations are listed.
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

def sortToWordList(itemList, wordList, startIndex, tableWidth):
    """
    wordList must be initialized with the same number of elements as itemList
    """
    index = 0
    endIndex = startIndex + tableWidth * 6
    for item in itemList[startIndex:endIndex]:
        word = removeTags(str(item))
        if word != '-':  #Skip the slot for 1st person imperative
            wordList[startIndex+2+index] = word
            index += 6
            if index >= 6*tableWidth:
                index %= 6*tableWidth
                index += 1

def scrapeSpanishdict(infinitive):
    """
    Scrapes conjugations from SpanishDict.com
    """
    url = 'http://www.spanishdict.com/conjugate/{}'.format(infinitive)
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    wordList = [None] * 61
    wordList[0] = cleanText(soup.find(text='Gerund:').findNext('span').string)
    wordList[1] = cleanText(soup.find(text='Participle:').findNext('span').string)
    itemList = soup.findAll('td', {'class': 'vtable-word'})
    startIndex = 0
    tableWidth = 5
    sortToWordList(itemList, wordList, startIndex, tableWidth)
    startIndex = startIndex + tableWidth*6
    tableWidth = 4
    sortToWordList(itemList, wordList, startIndex, tableWidth)
    startIndex = startIndex + tableWidth*6
    tableWidth = 1
    sortToWordList(itemList, wordList, startIndex, tableWidth)
    return wordList

def displayUsage():
    print("Usage:")
    print("  scrapeEspanol <fileName>")
    print("fileName contains a list of Spanish infinitives to process.")
    print("It saves a CSV file containing all the conjugations.")

def processFile(fileName):
    with io.open(fileName, 'r', encoding='utf8') as f:
        infinitiveList = f.readlines()
    listOfLists = []
    for infinitive in infinitiveList:
        wordList = scrapeSpanishdict(infinitive)
        listOfLists.append(wordList)
    with io.open('spanishConjugations.csv', 'w', encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerows(listOfLists)

def main():
    """Handle command line parameters"""
    if len(sys.argv) != 2:
        displayUsage()
    else:
        processFile(sys.argv[1])

if __name__ == "__main__":
    main()

