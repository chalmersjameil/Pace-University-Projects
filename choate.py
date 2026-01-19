import requests
import statistics

url = 'https://colabprod01.pace.edu/api/influx/sensordata/Alan/delta?days=7'

try:
    response = requests.get(url)
    response.raise_for_status()  
    data = response.json() 
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    exit()

sensors = {
    "Cond": [],
    "DOpct": [],
    "Sal": [],
    "Temp": [],
    "Turb": [],
    "pH": []
}

for record in data:
    for sensor in sensors.keys():
        sensors[sensor].append(record.get('sensors', {}).get(sensor, 0))

def calculate_stats(sensor_data):
    if sensor_data:  
        mean = statistics.mean(sensor_data)
        stdev = statistics.stdev(sensor_data) if len(sensor_data) > 1 else 0
        return mean, stdev
    return 0, 0

print("\nSensor Data Statistics (Mean and Standard Deviation):")
print("-" * 50)

for sensor, values in sensors.items():
    mean, stdev = calculate_stats(values)
    print(f"{sensor} - Mean: {mean:.2f}, Std Dev: {stdev:.2f}")
