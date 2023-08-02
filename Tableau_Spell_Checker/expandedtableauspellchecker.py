wbname = 'C:/Users/Employee/OneDrive - AVAAP/Documents/My Tableau Repository/Workbooks/HB7.twb'

from lxml import etree
from spellchecker import SpellChecker
import re
 
tree = etree.parse(wbname)
elem = tree.getroot()
spell = SpellChecker()

tb = elem.findall('.//dashboard/zones//formatted-text/run')
title = elem.findall('.//worksheet//title/formatted-text/run')
cn = elem.findall('.//datasource//column')
ac = elem.findall('.//action')
al = elem.findall('.//datasource//alias')
n = 0 
for w in tb:

    print('textbox ' + w.text)
    elemparent = 'ancestor::dashboard' 
    elemtype = 'dashboard' 
    for parent in w.xpath(elemparent):
            print('Found in {}: '.format(elemtype) + parent.attrib['name'])
            print('\n')
  
    words = re.sub(r'[^\w\s]','',w.text)
    misspelled_ws = spell.unknown(words.split())
    if len(misspelled_ws) > 0:
        for word in misspelled_ws:
            print('Flagged word: ' + word)
      
print('\n')
for w in title:
    print('title: ' + w.text)
    elemparent = 'ancestor::worksheet' 
    elemtype = 'worksheet' 
    for parent in w.xpath(elemparent):
            print('Found in {}: '.format(elemtype) + parent.attrib['name'])
            print('\n')

 
    words = re.sub(r'[^\w\s]','',w.text)
    misspelled_ws = spell.unknown(words.split())
    if len(misspelled_ws) > 0:
        for word in misspelled_ws:
            print('Flagged word: ' + word)
    print('\n')
print('\n')
for w in cn:
    print( 'column name: ' + w.attrib['name'])
    words = re.sub(r'[^\w\s]','',w.attrib['name'])
    misspelled_ws = spell.unknown(words.split())
    if len(misspelled_ws) > 0:
        for word in misspelled_ws:
            print('Flagged word: ' + word)
    print('\n')
print('\n')

for w in al:
    print( 'aliases: ' + w.attrib['value'])
    words = re.sub(r'[^\w\s]','',w.attrib['value'])
    misspelled_ws = spell.unknown(words.split())
    if len(misspelled_ws) > 0:
        for word in misspelled_ws:
            print('Flagged word: ' + word)
    print('\n')
print('\n')
for w in ac:
    print( 'action caption: ' + w.attrib['caption'])
    words = re.sub(r'[^\w\s]','',w.attrib['caption'])
    misspelled_ws = spell.unknown(words.split())
    if len(misspelled_ws) > 0:
        for word in misspelled_ws:
            print('Flagged word: ' + word)
    print('\n')
print('\n')










