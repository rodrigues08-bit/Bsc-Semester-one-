tips=sns.load_dataset("tips")
sns.catplot(data=tips,x='day',jitter=True,y='total_bill')
