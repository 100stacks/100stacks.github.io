# Try - Exception - handling errors in Python

import csv

with open(sample.csv) as csvfile:
  readCSV = csv.reader(csvfile, delimiter=',')
  dates = []
  stats = []
  for row in readCSV
    stat = row[3]
    date = row[0]
    
    dates.append(date)
    stats.append(stat)
    
  print(dates)
  print(stats)
  
  try:
    checkStat = input('What stat are you checking?')
