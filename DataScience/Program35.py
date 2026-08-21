cpc=df.groupby('Region of Max Sale')['Product Name'].count().reset_index()
cpc.columns=['Region of Max Sale','Product Count']
display(cpc)
