import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Replace with your city and OpenWeatherMap API key
city = "Delhi"
api_key = "986598cfb36fa7c4361e2de8ae271d3c"
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

# Fetch weather forecast data
response = requests.get(url)
data = response.json()

# Extract date-time and temperature information
dates = []
temps = []

for entry in data['list']:
    dates.append(entry['dt_txt'])
    temps.append(entry['main']['temp'])
#Limit data points for readability
dates = dates[:10]
temps = temps[:10]

# Plotting the temperature forecast
plt.figure(figsize=(10, 5))
sns.set(style="whitegrid")
sns.lineplot(x=dates, y=temps, marker='o', color='blue')

plt.xticks(rotation=45)
plt.title(f"5-Day Temperature Forecast for {city}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.grid(True)

# Save the plot as an image
plt.savefig("temperature_forecast.png")
plt.show()