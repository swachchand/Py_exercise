
"""
Explaination:

Given:
mealCost = 12. tipPercent:  = 20, taxPercent=8
calculations:
tip = 12 x 20/100 =2.4
tax = 12 x 8/100 = 0.96.

totcCost = mealCost + tip + tax = 12 +2.4 + 0.96 = 15.36
round(totalCost) = 15

"""
#!/bin/python3

import math
import os
import random
import re
import sys

mealCost = float(input())
tipPercent = float(input())
taxPercent = float(input())


totalTip = float(mealCost * (tipPercent / 100))
totalTax = float(mealCost * (taxPercent/100))

totalMealCost = round (mealCost + totalTip + totalTax)

print (totalMealCost)
