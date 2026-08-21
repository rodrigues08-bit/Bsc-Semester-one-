Import seaborn as sns
import matplotlib.pyplot as plt
data=[45,58,63,25,37]
keys=['class1','class2','class3','class4','class5']
explode=[0,0,0.2,0,0]
palette_color=seaborn.color_palette('Set2')
plt.pie(data,labels=keys,colors=palette_color,explode=explode,autopct='%.2f%%')
plt.show()
