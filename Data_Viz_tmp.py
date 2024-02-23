import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Represent data as a dictionary, represent key as names and values ages
data = {'Mari' : 40, 'George' : 39, 'Mia' : 13, 'Neo' : 8, 'Ada' : 4}

x = list(data.keys())
y = (data.values())

# Figure margins
fig = plt.figure(figsize = (10, 5))

# Label and Titles
plt.xlabel('Name')
plt.ylabel('Age')

plt.title('Name by Age')
# Plotting
plt.bar(x, y, color = 'maroon', width = 0.6)
# plt.(x, y)

plt.show()
