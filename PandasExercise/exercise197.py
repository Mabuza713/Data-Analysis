import pandas as pd
import numpy as np
data = {
    'id': [1, 2, 3, 4, 5, 6],
    'recordDate': ['2023-06-27', '2023-06-21', '2023-06-22', '2023-06-23', '2023-06-24', '2023-06-25'],
    'temperature': [50, 20, 30, 28, 35, 40]
}

data = pd.DataFrame(data)
def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather["recordDate"] = pd.to_datetime(weather["recordDate"], format='%Y-%m-%d')
    weather = weather.sort_values(by = "recordDate")
    print(weather)
    weather = weather[(weather.temperature > weather.temperature.shift(1)) &
                       (weather.recordDate == weather.recordDate.shift(1) + pd.Timedelta(1, "d"))]
    
    print(weather)
    
    
rising_temperature(data)
    