import pandas as pd
data = {
    'player_id': [1, 1, 1, 2, 3],
    'device_id': [2, 2, 3, 4, 4],
    'event_date': ["2016-3-1", "2016-5-2", "2017-6-25", "2016-3-2", "2018-7-3"],
    'games_played': [5, 6, 1, 3, 5]
}

# Creating the DataFrame
df = pd.DataFrame(data)

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.drop(columns = ["games_played", "device_id"])
    activity.rename(columns={"event_date":"first_login"},inplace= True)
    activity = activity.groupby("player_id", as_index=True)["first_login"].min()
    
    return activity;
    
print(game_analysis(df))