#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/



import sys, math, csv


def distance(una, plant):

  # Calculate the great circle distance between two points 
  # on the earth (specified in decimal degrees)
  # **** una and plant are coordiante tuples
 
  # convert decimal degrees to radians for each coordinate tuple
  unaRad = (math.radians(una[0]), math.radians(una[1]))
  plantRad = (math.radians(plant[0]), math.radians(plant[1]))
  # haversine formula 
  dlon = plantRad[0] - unaRad[0] 
  dlat = plantRad[1] - unaRad[1] 
  a = math.sin(dlat/2)**2 + math.cos(unaRad[1]) * math.cos(plantRad[1]) * math.sin(dlon/2)**2
  c = 2 * math.asin(math.sqrt(a)) 
  mi = 3953 * c
  return mi

# Define a main() function that prints a little greeting.
def main():
  # Get the name from the command line, using 'World' as a fallback.
    args = sys.argv[1:]
    if not args:
        print ("error enter the name of the file")
        sys.exit(1)
    else:
      try: 
        f = open(sys.argv[1], 'rb')
        reader = csv.reader(f)
        w=0
        a={}
        for line in reader:
          if w>1:
            x=line.strip(',')
            a[(x[0],x[1])]=(x[2],x[3])  
            
      
            w += 1
            
        q=0
        while (q<len(a)):
          
        
          q += 1
        print q
      except:
        print 'error cannot open'
      
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
