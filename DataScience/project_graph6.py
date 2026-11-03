import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Create the summary data directly (matching your original image)
data = {
    "Mon": [12, 8, 25, 45, 20, 5, 4, 3, 6, 10],
    "Tue": [15, 10, 28, 52, 24, 7, 6, 5, 8, 14],
    "Wed": [18, 12, 32, 60, 28, 9, 8, 7, 11, 18],
    "Thu": [20, 14, 35, 64, 32, 11, 10, 9, 13, 22],
    "Fri": [22, 16, 38, 68, 36, 14, 12, 11, 15, 26],
    "Sat": [16, 11, 30, 55, 27, 8, 7, 6, 9, 18]
}

bus_stops = [
    "KTC Porvorim Depot", "Mapusa KTC Bus Stand", "Margao KTC Bus Stand",
    "Panaji KTC Bus Stand", "Vasco Da Gama Bus Stand", "Calangute",
    "Baga", "Palolem", "Cortalim", "Ponda"
]

# 2. Turn it into a pandas table
df = pd.DataFrame(data, index=bus_stops)

# 3. Draw the heatmap
plt.figure(figsize=(10, 7))
sns.heatmap(df,
            annot=True,
            cmap="Purples",
            cbar_kws={'label': 'Number of Scheduled Services'})

# 4. Add the titles and labels
plt.title("Bus Service Availability at Selected Stops", fontsize=16, pad=15)
plt.xlabel("Day of Week", fontsize=12)
plt.ylabel("Bus Stop", fontsize=12)

# 5. Show the image
plt.show()