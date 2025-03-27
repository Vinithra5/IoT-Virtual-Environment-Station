# IoT Virtual Environment Station

This is a Python-based project that simulates a virtual environment station. It sends temperature, humidity, and CO₂ data to ThingSpeak using MQTT. The data is visualized live on ThingSpeak and can also be accessed using the REST API.

## What This Project Does

- Sends randomly generated sensor values (temperature, humidity, CO₂) to a ThingSpeak channel
- Uses MQTT protocol to publish data every 30 seconds
- Retrieves and displays the latest sensor values using HTTP GET
- Can show past 5 hours of sensor data for any of the three sensors

## Files Included

- `IOT_Assignment_3.py`: Main Python script that contains the menu and functions
- `mqtt_credentials.txt` (not included here): Contains credentials used in the code

## How to Use

1. Run the script using any Python 3 environment
2. Choose from the menu to:
   - Send new sensor data to ThingSpeak
   - View the latest data received
   - Display readings from the last 5 hours

## About

This project was done as part of my IoT course assignment. It helped me understand how to work with MQTT, APIs, and cloud platforms like ThingSpeak.

**GitHub repo maintained by Vinithra Sadras**
