import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("Goa_Public_Transport_FINAL.xlsx", sheet_name="Trips")

routes = data["route_id"].value_counts().head(20)

plt.bar(routes.index, routes.values, color="#A8DADC")

plt.xlabel("Route")
plt.ylabel("Number of Trips")
plt.title("Top 20 Routes by Number of Scheduled Trips")

plt.xticks(rotation=45, fontsize=8)
plt.show()