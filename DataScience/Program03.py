import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('titanic')
df.head()
sns.barplot(y='fare',x='class',hue='sex',data=df)
