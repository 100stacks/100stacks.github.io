# Try - Exception - handling errors in Python

import csv

with open(sample.csv) as csvfile:
  readCSV = csv.reader(csvfile, delimiter=',')
  dates = []
  colors = []
  for row in readCSV
    color = row[3]
    date = row[0]
    
    dates.append(date)
    colors.append(color)
    
  print(dates)
  print(colors)
  
