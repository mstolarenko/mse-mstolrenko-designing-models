import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
df = pd.read_csv(r'C:\Users\maxwe\Documents\Grad\Classes\Fall 2022\SimTech\assignment-1-mse-mstolarenko\data\7-dayAVG.csv')

df['Average Days at ANC and Berth'] = df['Average Days at ANC and Berth'].astype('category')

counts = [5.5, 6.4, 4.8, 5, 5.66, 3.25, 0]
ranges = ['7/28/2022', '7/29/2022', '8/1/2022', '8/2/2022', '8/3/2022', '8/4/2022', '8/5/2022']

plt.bar(ranges, counts)
plt.xlabel('Dates')
plt.ylabel('Average in Days')
plt.title('Average Number of Days Vessels Spent Anchored and Berthed')
plt.axhline(y=np.nanmean(counts), color='orange', linestyle='--', linewidth=3, label='Avg')
plt.show()
