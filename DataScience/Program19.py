import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data=np.random.randint(low=1,high=100,size=(10,10))
print(" The Data to be plotted:\n")
print(data)
hm=sns.heatmap(data=data)
