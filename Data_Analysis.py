import requests
import pandas as pd
import matplotlib.pyplot as plt

# ThingSpeak parameters
api_key = "Your_ThingSpeak_API_Key"
channel_id = "Your_Channel_ID"
url = f"https://api.thingspeak.com/channels/{channel_id}/feeds.json?api_key={api_key}&results=100"

# Fetch data from ThingSpeak
response = requests.get(url)
data = response.json()

# Load data into Pandas DataFrame
feeds = data['feeds']
df = pd.DataFrame(feeds)

# Convert timestamp to datetime
df['created_at'] = pd.to_datetime(df['created_at'])

# Rename columns for easier access
df = df.rename(columns={'field1': 'Temperature', 'field2': 'Humidity', 'field3': 'Current', 'field4': 'Gas'})

# Convert fields to numeric
df['Temperature'] = pd.to_numeric(df['Temperature'])
df['Humidity'] = pd.to_numeric(df['Humidity'])
df['Current'] = pd.to_numeric(df['Current'])
df['Gas'] = pd.to_numeric(df['Gas'])

# Plotting the data
plt.figure(figsize=(10, 8))

# Temperature and Humidity Plot
plt.subplot(2, 1, 1)
plt.plot(df['created_at'], df['Temperature'], label='Temperature (°C)')
plt.plot(df['created_at'], df['Humidity'], label='Humidity (%)')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Values')
plt.title('Temperature and Humidity over Time')

# Current and Gas Levels Plot
plt.subplot(2, 1, 2)
plt.plot(df['created_at'], df['Current'], label='Current (mA)')
plt.plot(df['created_at'], df['Gas'], label='Gas Level (ppm)')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Values')
plt.title('Current and Gas Levels over Time')

plt.tight_layout()
plt.show()
