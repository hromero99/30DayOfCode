#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#


def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tip_value = meal_cost * (tip_percent / 100)
    meal_cost_with_tax = meal_cost + (meal_cost * tax_percent/100)
    total = round(meal_cost_with_tax + tip_value)
    print(total)


if __name__ == '__main__':
    meal_cost = float(input().strip())  # 12

    tip_percent = int(input().strip())  # 20

    tax_percent = int(input().strip())  # 8

    solve(meal_cost, tip_percent, tax_percent)
