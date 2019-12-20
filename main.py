#!/usr/bin/env python3

import sys
import csv

with open("customer_pages.csv", 'r', encoding='utf-8-sig') as file:
    datafile = csv.DictReader(file)

    for row in datafile:
      if sys.argv[1] == row['Customer ID']:
        print(row['Page ID'], end=' ')
    print('\n')
