import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("Goa_Public_Transport_FINAL.xlsx", sheet_name="Stop Times")

trips = pd.read_excel("Goa_Public_Transport_FINAL.xlsx", sheet_name="Trips")

data = pd.merge(data, trips, on="trip_id")

data["departure_time"] = pd.to_timedelta(data["departure_time"])

data["gap"] = data.groupby("route_id")["departure_time"].diff().dt.total_seconds() / 60

gap = data.groupby("route_id")["gap"].mean().sort_values(ascending=False).head(10)

plt.barh(gap.index, gap.values, color="#CDB4DB")

plt.xlabel("Average Gap (minutes)")
plt.ylabel("Route")
plt.title("Routes with Longer Gaps Between Buses")

plt.show()