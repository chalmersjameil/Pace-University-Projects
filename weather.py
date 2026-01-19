import json
import requests
import pandas as pd

def main():
    response = requests.get('https://colabprod01.pace.edu/api/influx/sensordata/Odin/delta?days=1')
    
    weather_json = response.json()

    print("Raw JSON response:", json.dumps(weather_json, indent=2))

    weather = pd.json_normalize(weather_json)

    print("DataFrame columns:", weather.columns.tolist())
    
    if not weather.empty:
        most_recent_data = weather.iloc[-1] 
        print("Most recent weather data:", most_recent_data.to_dict())
    else:
        print("No data available.")

if __name__ == '__main__':
    main()
