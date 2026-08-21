fig=df[df.species=='setosa'].plot(kind='scatter',x='sepal_length',y='sepal_width',
color='grey',label='setosa')
fig=df[df.species=='versicolor'].plot(kind='scatter',x='sepal_length',y='sepal_width',
color='pink',label='versicolor',ax=fig)
fig=df[df.species=='virginica'].plot(kind='scatter',x='sepal_length',y='sepal_width',
color='purple',label='virginica',ax=fig)
fig.set_xlabel('sepal_length')
fig.set_ylabel('sepal_width')
fig.set_title('Sepal length * Sepal width')
