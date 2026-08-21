import seaborn as sns
import pandas as pd
import numpy as mn
import matplotlib.pyplot as plt
df=sns.load_dataset("titanic")
plt.figure(figsize=(5,3))
sns.histplot(data=df,x='fare',bins=50,color='green')
plt.title('DISTRIBUTION OF FARE')
plt.xlabel("fare")
plt.ylabel("frequency")
plt.grid(True)
