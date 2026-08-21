fig=df[df.species=='setosa'].plot(kind='scatter',x='petal_length',y='petal_width',
color='grey',label='setosa')
fig=df[df.species=='versicolor'].plot(kind='scatter',x='petal_length',y='petal_width',
color='pink',label='versicolor',ax=fig)
fig=df[df.species=='virginica'].plot(kind='scatter',x='petal_length',y='petal_width',
color='purple',label='virginica',ax=fig)
fig.set_xlabel('petal_length')
fig.set_ylabel('petal_width')
fig.set_title('Petal length * Petal width')
