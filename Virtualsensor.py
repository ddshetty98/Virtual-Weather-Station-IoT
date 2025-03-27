import random
import time
import paho.mqtt.client as mqtt

# Replace these with your actual ThingSpeak details
channel_id = "2892342"
write_api_key = "NKEIIMSY6JH6JOEX"


# MQTT settings
broker = "mqtt.thingspeak.com"
port = 1883
topic = f"channels/{channel_id}/publish"

client = mqtt.Client()
client.username_pw_set("anything", write_api_key)
client.connect(broker, port, 60)

print("Starting Virtual Sensor Station...")

while True:
    temperature = round(random.uniform(-50, 50), 2)
    humidity = round(random.uniform(0, 100), 2)
    co2 = round(random.uniform(300, 2000), 2)

    payload = f"field1={temperature}&field2={humidity}&field3={co2}"
    client.publish(topic, payload)
    print("Data sent ->", payload)

    time.sleep(15)
