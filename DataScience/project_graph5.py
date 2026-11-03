import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("Goa_Public_Transport_FINAL.xlsx", sheet_name="Passenger Impact")

plt.scatter(data["actual_wait_min"], data["late_duration_min"])

plt.xlabel("Waiting Time (minutes)")
plt.ylabel("Late Duration (minutes)")
plt.title("Waiting Time vs Late Arrival")

plt.show()