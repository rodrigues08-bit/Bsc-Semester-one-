import seaborn as sns
import pandas as pnd
import numpy as np
import matplotlib.pyplot as plt
histogram 
df=sns.load_dataset('titanic')
plt.figure(figsize=(10,5))
sns.histplot(data=df,x='class')
plt.title("distributrion of class")
plt.xlabel("class")
plt.ylabel("frequency")
plt.grid(True)
