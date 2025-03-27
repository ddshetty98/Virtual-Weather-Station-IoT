# Virtual Weather Station - IoT Assignment

This project simulates an IoT-based weather station that collects and sends temperature, humidity, and CO2 data to the cloud using the MQTT protocol and ThingSpeak.

Name:Divit Shetty 
Syracuse University – IoT Assignment 3  
Email: dishetty@syr.edu
Date: 03/26/2025 

## Project summary

- Simulates virtual sensors using Python.
- Publishes data to a ThingSpeak channel using MQTT.
- Displays real-time data in charts (Temperature, Humidity, CO2).

##  Requirements

To run this project, Python version 3.6 or above is required. Additionally, the paho-mqtt package must be installed using:pip install paho-mqtt

##  MQTT Configuration

1.First, create an account on ThingSpeak and set up a new channel with Field 1 for Temperature, Field 2 for Humidity, and Field 3 for CO2.

2.Then, go to the Devices tab and add a new MQTT device.

3.In your Python script (virtualsensor.py), configure the MQTT settings using:

4.Broker: mqtt3.thingspeak.com

5.Your provided MQTT Client ID, Username, and Password

6.The correct Channel ID and Write API Key

##  How to Run

1.Open the file named virtualsensor.py in Visual Studio Code or any preferred code editor.

2.Replace the placeholders in the script with your actual credentials:

3.Update the channel_id with your ThingSpeak Channel ID.

4.Update the write_api_key with your Write API Key from ThingSpeak.

5.Set the correct values in the client.username_pw_set() function using your MQTT username and password.

6.Save the script and run it using the command:python virtualsensor.py

7.Once the script is running, open your ThingSpeak account and view the live charts under the Private View tab to observe real-time data updates.

## Screenshots

Screenshots showing:

- ThingSpeak live charts
- Terminal output from Python script
- MQTT device configuration









