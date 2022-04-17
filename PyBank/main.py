from audioop import avg
from calendar import month
from ctypes.wintypes import LONG
import os

import csv
from pickletools import long1
from statistics import mean

with open("budget_data.csv" ) as csvfile:

    rows = csv.reader(csvfile, delimiter=',')

    entry = []

    month = []

    earnings = []

    change_earn = []

    for row in rows:

        entry.append(row)


for i in entry:

    month.append(i[0])

    earnings.append(i[1])

earnings.pop(0)

month.pop(0)

int_earning = [round(float(s)) for s in earnings]



print("Financial Analysis")

print("----------------------------")

print("Total Months: " + str(len(month))) 

print("Total: $" + str(sum(int_earning))) 

print("Average Change: $" + str(mean(int_earning)))













