import requests


channel_id = "2892342"
read_api_key = "S43HHS3WR6PYMDCW"  

url = f"https://api.thingspeak.com/channels/{channel_id}/feeds.json?results=1&api_key={read_api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    latest_entry = data["feeds"][0]
    temperature = latest_entry["field1"]
    humidity = latest_entry["field2"]
    co2 = latest_entry["field3"]

    print("Latest Sensor Data:")
    print(f"Temperature: {temperature} °C")
    print(f"Humidity: {humidity} %")
    print(f"CO2: {co2} ppm")
else:
    print("Failed to fetch data:", response.status_code)
