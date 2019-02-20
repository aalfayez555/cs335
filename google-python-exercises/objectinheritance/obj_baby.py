#!/usr/bin/python -tt

import urllib
import re
import sys

class Male:
    def __init__(self,year,Name):
        self.year=year
        
class Female:
    def __init__(self,year,Name):
        self.year=year
        


class BabyNames:
    def __init__(self,year):
        self.year = year
        
    def retrieveNames(self,url):
        # creat a method to retrieve the names
        
         self.names = resulte
        
    def printNames(self):
        print self.names

def main():
    
    args = sys.argv[1:]

    if not args:
        print 'usage: [--summaryfile] file [file ...]'
        sys.exit(1)
        
        
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    try:
        text = urllib.urlopen(args[0])
        if text.info().gettype() == 'text/html':
            years= re.findall(r'\d\d\d\d\sto\s\d\d\d\d</h2><ul>(.*?)</ul>',text)
            for year in years:
               print year
                
            """for yearURL in yearURLs:
                bn = BabyNames(yearURL)
                bn.printNames()
            """
        
    except IOError:
        print " could not access web address "
        








if __name__ == '__main__':
  main()