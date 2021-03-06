import numpy as np
import matplotlib.pyplot as plt
import csv
import types

my_data = np.genfromtxt('1516unrefined.csv',
                        delimiter=',', encoding='utf-8', dtype=None)

with open('1516yet.csv', mode='w', newline='') as nicePER:
    perWriter = csv.writer(
        nicePER, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for row in my_data:
        for col in range(len(row)):
            if isinstance(row[col], float):
                continue
            row[col] = row[col].strip().replace('"', "")
        perWriter.writerow(row)

