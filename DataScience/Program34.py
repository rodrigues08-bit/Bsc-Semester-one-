cpc=df.groupby('Category')['Product Name'].count().reset_index()
  cxv  zcpc.columns=['Category','Product Count']
display(cpc)
