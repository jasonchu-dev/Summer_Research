import pandas as pd
import numpy as np
import csv

def isNaN(num):
    return num != num

def main():
    df = pd.read_excel('ChinoData.xlsx')

    set_1 = []
    set_2 = []

    for i, row in df.iterrows():
        if row[2] == 1: set_1.append(row)
        else: set_2.append(row)

    set_1 = np.array(set_1)
    set_2 = np.array(set_2)

    medians = []

    for i in range(len(set_1)):
        if not isNaN(set_1[i][3]) and not isNaN(set_2[i][3]):
            medians.append(np.median(np.concatenate([set_1[i][3:], set_2[i][3:]])))
        elif isNaN(set_1[i][3]) and not isNaN(set_2[i][3]):
            medians.append(np.median(set_2[i][3:]))
        elif isNaN(set_2[i][3]) and not isNaN(set_1[i][3]):
            medians.append(np.median(set_1[i][3:]))

    pts_df = pd.read_csv('Waypoints_8_2.csv')

    data = []

    for i in range(len(medians)):
        data.append([set_1[i][0], set_1[i][1], pts_df['Latitude'][i], pts_df['Longitude'][i], medians[i]])

    with open('data.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Row', 'Col', 'Latitude', 'Longitude', 'Concentration (PPT)'])
        writer.writerows(data)

if __name__ == "__main__": main()