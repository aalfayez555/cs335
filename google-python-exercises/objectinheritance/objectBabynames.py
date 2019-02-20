#!/usr/bin/python -tt

import urllib
import re
import sys


class BabyNames:
    def __init__(self,year,url):
        self.year = year
        self.url=url
        self._sort=False
    def retrieveNames(self):
        self.names={}
        try:
            if (self.year<str(2011)):
                temp={}
                m=0
                hello=[]
                i=0
                text = urllib.urlopen(self.url)
                if text.info().gettype() == 'text/html':
                    for line in text:
                        colect=re.findall(r'</h2><ol>(.*)</ol>',line)
                        if colect:
                            j=0
                            while (j<len(colect)):
                                temp[m]=colect[j].split('</li><li>')
                                hello.extend(temp[m])
                                j += 1
                                m += 1
                            while (i<len(hello)):
                                match = re.search(r'">(.*?)</a>',hello[i])
                                if match:
                                    self.names[match.group(1)]=str(i)
                                i += 1
            elif (self.year>str(2011)):
                m=1
                text = urllib.urlopen(self.url)
                if text.info().gettype() == 'text/html':
                    for line in text:
                        colect=re.search(r'<li> <a href="/babyname/.*">(.*)</a>',line)
                        if colect:
                            self.names[colect.group(1)]=str(m)
                            m += 1
        except IOError:
            print (" could not access web address ")
    def printNames(self):
        print self.year
        print len(self.names)
        if self._sort:
            i=0
            while i<len(self.names):
                print self.names[i][0]+": "+self.names[i][1]
                i += 1
        else:
            for i in  self.names:
                print i + " "+ self.names[i]
    def sortNamesAlfa(self):
        self.names=sorted(self.names.items(),key=lambda  x:x[0])
        self._sort=True
def main():
    args = sys.argv[1:]
    if not args:
        print ("usage: [--summaryfile] file [file ...]")
        sys.exit(1)
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]
    try:
        info=[]
        li_ge={}
        li_y={}
        main_url=re.findall(r'(.*/)',args[0])
        print main_url
        text = urllib.urlopen(args[0])
        if text.info().gettype() == 'text/html':
            for line in text:
                data= re.findall(r'\d\d\d\d\sto\s\d\d\d\d</h2><ul>(.*?)</ul>',line)
                #for year in years:
                if data:
                    info.append(data)
            """for yearURL in yearURLs:
                    bn = BabyNames(yearURL)
                    bn.printNames()
            """
            hello=[]
            for k in info[0]:
                hello.extend(k.split('</li><li>'))
            for rt in hello:
                print rt
            i=0
            while i < len(hello):
                #match=re.search(r'<a href="/(\w.*)">Popular\s(.*).*es\s(\d\d\d\d)</a>',hello[i])
                match_2=re.search(r'<a href="/(\w.*)">.+s\s(\d\d\d\d)</a>',hello[i])
                """if match:
                    #print match
                    li_ge[match.group(1)]=match.group(2)
                    li_y[match.group(1)]=match.group(3)
                """
                if match_2:
                    li_y[match_2.group(1)]=match_2.group(2)
                i += 1
            print i  
            for j in li_y:
                print li_y[j]+" "+j
            z={}
            mm=0
            for q in li_y:
                z[mm]=BabyNames(li_y[q],main_url[0]+q)
                mm += 1
            nn=0
            while nn<len(z):
                z[nn].retrieveNames()
                #z.printNames()
                z[nn].sortNamesAlfa()
                z[nn].printNames()
                nn += 1
    except IOError:
        print (" could not access web address ")
if __name__ == '__main__':
  main()