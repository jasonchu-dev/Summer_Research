import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import pandas as pd

def main():
    df = pd.read_csv('data.csv')

    x = np.array(df['Longitude'])
    y = np.array(df['Latitude'])
    z = np.zeros(len(df['Concentration (PPT)']))

    dx = np.array([.000015])
    dy = np.array([.000015])
    dz = np.array(df['Concentration (PPT)'])

    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')
    cmap = cm.get_cmap('jet')

    max_height = np.max(dz)
    min_height = np.min(dz)

    rgba = [cmap((k-min_height)/max_height) for k in dz]
    plot = ax.bar3d(x, y, z, dx, dy, dz, color=rgba)

    plt.title("SF6 Data")
    ax.set_xlabel('Long', fontweight ='bold')
    ax.set_ylabel('Lat', fontweight ='bold')
    ax.set_zlabel('Conc (PPT)', fontweight ='bold')

    fig.colorbar(plt.cm.ScalarMappable(cmap = 'jet'), ax = ax)

    plt.show()

if __name__ == "__main__": main()