tips=sns.load_dataset("tips")
sns.catplot(data=tips,x='day',y='total_bill')
