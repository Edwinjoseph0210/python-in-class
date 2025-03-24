import os
import pandas as pd

# File path
file_path = "/Users/apple/Documents/weather.csv"

# Check if the file exists, if not, create it
if not os.path.exists(file_path):
    data = {
        "date": ["2025-03-01", "2025-03-02", "2025-03-03", "2025-03-04", "2025-03-05"],
        "temperature": [25, 30, 15, 18, 10],
        "humidity": [60, 50, 80, 75, 90],
        "windSpeed": [12, 8, 10, 14, 20],
        "precipitationType": ["Rain", "None", "Snow", "Rain", "None"],
        "place": ["New York", "Los Angeles", "Chicago", "Seattle", "Boston"],
        "weather": ["Rainy", "Sunny", "Cloudy", "Rainy", "Cloudy"]
    }

    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print("✅ weather.csv file created successfully!")

# Read the CSV file
df = pd.read_csv(file_path)

# 1️⃣ Print the first 10 rows
print("\n🔹 First 10 rows of weather data:")
print(df.head(10))

# 2️⃣ Find the maximum and minimum temperature
max_temp = df["temperature"].max()
min_temp = df["temperature"].min()
print(f"\n🌡️ Maximum Temperature: {max_temp}°C")
print(f"❄️ Minimum Temperature: {min_temp}°C")

# 3️⃣ List places where temperature is less than 20°C
cold_places = df[df["temperature"] < 20]["place"]
print("\n🏔️ Places with temperature less than 20°C:")
print(cold_places.to_string(index=False))

# 4️⃣ List places where weather is 'Cloudy'
cloudy_places = df[df["weather"] == "Cloudy"]["place"]
print("\n☁️ Places with 'Cloudy' weather:")
print(cloudy_places.to_string(index=False))
