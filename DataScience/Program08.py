import seaborn 
import matplotlib.pyplot as plt
data=[45,30,15,20,40]
keys=['Mango','Plum','Guava','Apple','Kiwi']
palette_color=seaborn.color_palette("Set3")
plt.pie(data,labels=keys,colors=palette_color,autopct='%.2f%%')
plt.show()
