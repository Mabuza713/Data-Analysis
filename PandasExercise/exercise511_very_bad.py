import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.drop(columns = ["games_played", "device_id"])
    activity.rename(columns={"event_date":"first_login"})
    result = {
                'player_id': [],
                'first_login': []
            }

    for id in list(set(activity["player_id"])):
        playerDataFrame = activity[activity["player_id"] == id]
        temp = {
            'player_id': [id],
            'first_login': [playerDataFrame["event_date"].min()]
        }
        result = pd.concat([pd.DataFrame(result), pd.DataFrame(temp)])
    
    
    return pd.DataFrame(result);