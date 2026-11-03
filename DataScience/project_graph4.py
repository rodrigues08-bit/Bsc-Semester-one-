import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("Goa_Public_Transport_FINAL.xlsx", sheet_name="Passenger Impact")

sns.histplot(data=data, x="actual_wait_min", bins=50, color="#FFD6A5")

plt.xlabel("Waiting Time (minutes)")
plt.ylabel("Number of Passengers")
plt.title("Distribution of Passenger Waiting Time")

plt.show()