cpc = df_csv.groupby(['Category', 'Region of Max Sale'])['Product Name'].count().reset_index()
cpc.columns=['Category','Region','Product Name']
cpc.head()
