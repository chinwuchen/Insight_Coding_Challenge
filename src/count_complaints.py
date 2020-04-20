"""
Insight Coding Challenge

Sort and count consumer complaints from CCDB
using default data structure 

written by Chin-Wu Chen, 04/19/2020
"""

# Import libraries

import sys
import csv
from collections import namedtuple
from datetime import datetime
from collections import Counter

# File I/O

if len(sys.argv) < 3 or len(sys.argv) > 3:
   print('usage: count_complaints.py <inputfile> <outputfile>')
   sys.exit(2)

inputfile = sys.argv[1]
outputfile = sys.argv[2]

#    print ('Input file is: ', inputfile)
#    print ('Output file is: ', outputfile)


# Create data structure as a namedtuple

class Event(namedtuple('Event', ['product', 'year', 'company'])):
    __slots__ = ()

# Function to read data 

def read_events(csvfile):
    
    def _getyear(date):
        return datetime.strptime(date, '%Y-%m-%d').date().year
    
    def _lower(x):
        if x is None:
            return ''
        return x.lower()
    
    with open(csvfile) as infile:
        reader = csv.DictReader(infile)
        
        for row in reader:
            yield Event(_lower(row['Product']), _getyear(row['Date received']),
                        _lower(row['Company']))


# Read data
            
events = tuple(read_events(inputfile))

count_prod = Counter(x.product for x in events) # list of all distinct products

count_year = Counter(x.year for x in events) # list of all years

# Function for main calculation

def cal_counts(count):
    csum = 0                      # total number of complaints
    cmax = 0                      # number of most complaints against one company
    for (n, c) in count.items():
        if c >= cmax:
            cmax = c
        csum += c
    return csum,len(count),round(cmax/csum*100)

# Loop over data and write to output file

fout = open(outputfile, 'w', newline='')

writer = csv.writer(fout, quoting=csv.QUOTE_MINIMAL, delimiter=',')

for k in sorted(count_prod.keys()):
    for y in sorted(count_year.keys()):
        count_com = Counter(x.company for x in events if x.product==k and 
                           x.year==y)
        if len(count_com) != 0:
            [tot, tot_com, perc] = cal_counts(count_com)
            row = [k, y, tot, tot_com, perc]
#            print('{},{},{},{},{}'.format(k,y,tot,tot_com,perc)) #optional for printing out results
            writer.writerow(row)

fout.close()


