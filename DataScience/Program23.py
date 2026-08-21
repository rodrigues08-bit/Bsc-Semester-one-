tips=sns.load_dataset("tips")
sns.catplot(data=tips,x='sex',y='tip')
