import seaborn
seaborn.set(style="whitegrid")
tip=seaborn.load_dataset("tips")
seaborn.boxplot(x=tip['total_bill'])