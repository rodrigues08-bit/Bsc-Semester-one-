import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('titanic')
df.head()
sns.barplot(x='fare',y='class',hue='sex',data=df,
          order=["Third","Second","First"])
