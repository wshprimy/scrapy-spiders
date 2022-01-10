import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
df = pd.read_csv("iris.csv")
attribute = ['Petal.Length', 'Petal.Width', 'Sepal.Length', 'Sepal.Width']
species = df.Species.unique()

color = ['r', 'g', 'b']
plt.figure(figsize=(30, 30))
plt.legend()
plt.suptitle('IRIS散点图')
for xid, x in enumerate(attribute):
    for yid, y in enumerate(attribute):
        plt.subplot(4, 4, 4 * xid + yid + 1)
        for i, specie in enumerate(species):
            plt.scatter(x=df.loc[df.Species == specie, x], y=df.loc[df.Species == specie, y], s=35, c=color[i], label=specie)
            plt.title(f'{x} - {y}')
            plt.xlabel(x, loc='right', fontsize=10)
            plt.ylabel(y, loc='top', fontsize=10)
            plt.grid(True, alpha=0.7)

plt.savefig('3.jpg')