import pandas as pd
import matplotlib.pyplot as plt
import seaborn

data = pd.read_excel("Goa_Public_Transport_FINAL.xlsx", sheet_name="Passenger Impact")

purpose = data["travel_purpose"].value_counts()

keys = purpose.index
values = purpose.values

palette_color = seaborn.color_palette("pastel")

plt.pie(values, labels=keys, colors=palette_color, autopct="%.0f%%")

plt.title("Passenger Travel Purpose")
plt.show()