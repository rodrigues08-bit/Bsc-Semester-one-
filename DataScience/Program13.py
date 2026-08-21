import seaborn as sns
import pandas as pd
import numpy as mn
import matplotlib.pyplot as plt
df=sns.load_dataset("titanic")
plt.figure(figsize=(5,3))
sns.histplot(data=df,x='class',hue='adult_male',bins=30,color='green',kde=True,alpha=0.3)
plt.title('DISTRIBUTION OF class')
plt.xlabel("class")
plt.ylabel("frequency")
plt.grid(True)
