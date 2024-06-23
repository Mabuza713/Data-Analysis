import pandas as pd
import numpy as np
data = {
    'id': [0,1,2,3,4,5],
    'num': [-9,-9,-9,8,-7,5]
}

df = pd.DataFrame(data)
def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    if len(logs["id"].values) == 0:
        return pd.DataFrame({"ConsecutiveNums":[]})

    new_df = pd.DataFrame({"id":np.arange(logs["id"].values.min(),logs["id"].values.max() + 1, 1),
                           "num":[None for x in range(logs["id"].values.min(), logs["id"].values.max() + 1)]})
    new_df = pd.merge(new_df, logs,how = "left", on = "id")
    new_df = new_df.drop(columns=["num_x"])    
    new_df.set_index("id", inplace= True)
    listOfIndex = []
    new_df["num_y"].rolling(3, center=False).apply(lambda x: listOfIndex.append(x.tolist()) or 0)
    
    result = []
    print(new_df)
    for x in listOfIndex:
        if list(x).count(None) == 0:
            if len(list(set(x))) == 1 and np.mean(x) == x[0]:
                result.append(x[0])
    return pd.DataFrame({"ConsecutiveNums":list(set(result))})
            

    
    
print(consecutive_numbers(pd.DataFrame(data)))
    
    