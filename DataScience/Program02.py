import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('titanic')
df.head()
sns.barplot(x='class',y='fare',data=df)
