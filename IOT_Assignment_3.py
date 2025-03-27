import time
import random
import requests
from datetime import datetime, timedelta
import paho.mqtt.client as mqtt

# === ThingSpeak Configuration ===
CHANNEL_ID = "2894189"
READ_API_KEY = "6RXY34MCDEO7MF6O"
WRITE_API_KEY = "65IJUA4K7PZXF1WT"
MQTT_USERNAME = "IBoZOhMeOzcOAwMGMDcpBhM"
MQTT_PASSWORD = "b2pfyBb5LAlbyFWeO6J2P/Jq"
MQTT_CLIENT_ID = "IBoZOhMeOzcOAwMGMDcpBhM"
MQTT_HOST = "mqtt3.thingspeak.com"
MQTT_PORT = 1883
MQTT_TOPIC = f"channels/{CHANNEL_ID}/publish"

# === Create MQTT Client ===
client = mqtt.Client(MQTT_CLIENT_ID)
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
client.connect(MQTT_HOST, MQTT_PORT, 60)

# === Function: Generate Virtual Sensor Data ===
def generate_sensor_data():
    temperature = round(random.uniform(-50, 50), 2)
    humidity = round(random.uniform(0, 100), 2)
    co2 = round(random.uniform(300, 2000), 2)
    return temperature, humidity, co2

# === Function: Send Sensor Data via MQTT ===
def send_sensor_data():
    temp, hum, co2 = generate_sensor_data()
    payload = f"field1={temp}&field2={hum}&field3={co2}"
    client.publish(MQTT_TOPIC, payload)
    print(f"✅ Sent to ThingSpeak: {payload}")

# === Function: Get Latest Data (Part B) ===
def get_latest_data():
    url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds/last.json?api_key={READ_API_KEY}"
    response = requests.get(url)
    data = response.json()

    print("\n📦 Latest Sensor Data:")
    print(f"Temperature: {data['field1']}°C")
    print(f"Humidity: {data['field2']}%")
    print(f"CO₂: {data['field3']} ppm")
    print(f"Timestamp: {data['created_at']}")

# === Function: Get Last 5 Hours Data (Part C) ===
def get_last_five_hours_data(field_number):
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(hours=5)

    url = (
        f"https://api.thingspeak.com/channels/{CHANNEL_ID}/fields/{field_number}.json"
        f"?api_key={READ_API_KEY}&start={start_time.isoformat()}Z&end={end_time.isoformat()}Z"
    )

    response = requests.get(url)
    data = response.json()
    feeds = data.get("feeds", [])

    if not feeds:
        print("❌ No data available for the last 5 hours.")
        return

    print(f"\n📈 Last 5 Hours of Data (Sensor field {field_number}):")
    for entry in feeds:
        print(f"{entry['created_at']} — Value: {entry[f'field{field_number}']}")

# === Main Menu ===
def main():
    while True:
        print("\n📡 Virtual Environment Station — Menu")
        print("1. Send Sensor Data to ThingSpeak (Part A)")
        print("2. Display Latest Sensor Data (Part B)")
        print("3. Display Last 5 Hours of Data (Part C)")
        print("4. Exit")

        choice = input("Choose an option (1/2/3/4): ")

        if choice == "1":
            send_sensor_data()
        elif choice == "2":
            get_latest_data()
        elif choice == "3":
            print("\nWhich sensor?")
            print("1 - Temperature")
            print("2 - Humidity")
            print("3 - CO2")
            sensor = input("Enter sensor number (1/2/3): ")
            if sensor in ["1", "2", "3"]:
                get_last_five_hours_data(int(sensor))
            else:
                print("❌ Invalid sensor choice.")
        elif choice == "4":
            print("Exiting... 👋")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()
