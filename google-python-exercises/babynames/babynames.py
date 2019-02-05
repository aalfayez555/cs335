#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  f=open(filename,'r') # this to open the file and read from it 
  info_m={}
  info_f={}
  temp=True

  for l in f:
    match_y=re.search(r'<h3 align="center">Popularity in ([\d]+.)</h3>',l)
    
    if match_y and temp:
      temp=False
      year=match_y.groups(1)
    match =re.search(r'<tr align="right"><td>([\d].*)</td><td>([\w].+)</td><td>([\w].+)</td>',l)
    if match:
      
      info_m[match.group(1)]= match.group(2)
      info_f[match.group(1)]= match.group(3)
    else: 
      continue

  q_m= sorted(info_m.items(),key=lambda  x:x[1])
  q_f= sorted(info_f.items(),key=lambda  x:x[1])
  q_m[0]=year[0]
  q_f[0]=year[0]
  print_baby(q_m)
  print_baby(q_f)
  f.close()
  return 0
def babynames_m(filename):
  
  f=open(filename,'r') # this to open the file and read from it 
  info_m={}
  
  temp=True

  for l in f:
    match_y=re.search(r'<h3 align="center">Popularity in ([\d]+.)</h3>',l)
    
    if match_y and temp:
      temp=False
      year=match_y.groups(1)
    match =re.search(r'<tr align="right"><td>([\d].*)</td><td>([\w].+)</td><td>([\w].+)</td>',l)
    if match:
      
      info_m[match.group(1)]= match.group(2)

    else: 
      continue

  q_m= sorted(info_m.items(),key=lambda  x:x[1])

  q_m[0]=year[0]
  print_baby(q_m)
  f.close()
  
  
  

  return 0
def babynames_f(filename):
  f=open(filename,'r') # this to open the file and read from it 
  info_f={}
  temp=True

  for l in f:
    match_y=re.search(r'<h3 align="center">Popularity in ([\d]+.)</h3>',l)
    
    if match_y and temp:
      temp=False
      year=match_y.groups(1)
    match =re.search(r'<tr align="right"><td>([\d].*)</td><td>([\w].+)</td><td>([\w].+)</td>',l)
    if match:
      
      info_f[match.group(1)]= match.group(3)
    else: 
      continue


  q_f= sorted(info_f.items(),key=lambda  x:x[1])

  q_f[0]=year[0]
  print_baby(q_f)
  f.close()
  
  return 0
def print_baby(list):

  list_baby_m=[]
  list_baby_m.append(list[0])
  templist=[]
  i=1
  while i<len(list)-1:
    templist.append("{}  {}".format(list[i][1],list[i][0]))
    list_baby_m.extend(templist)
    templist=[]
    i += 1
  print list_baby_m
  
  return 0
def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
    for i in args:
      extract_names(i)
  
  if args[0]=='--male':
    babynames_m(args[1])
  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  if args[0]=='--female':
    babynames_f(args[1])
  
if __name__ == '__main__':
  main()
