import pandas as pd
import numpy as np

data = {
    'x': [3, 5, 1, 2, 7, 1, 10, 6],
    'y': [4, 12, 1, 2, 24, 2, 10, 8],
    'z': [5, 13, 1, 3, 25, 3, 20, 10]
}

data_pd = pd.DataFrame(data)

def triangle_judgement(triangle: pd.DataFrame):
    triangle["triangle"] = np.where((triangle["x"] + triangle["y"] > triangle["z"]) &
                                    (triangle["y"] + triangle["z"] > triangle["x"]) &
                                    (triangle["x"] + triangle["z"] > triangle["y"]), True, False)

    
    return triangle
print(triangle_judgement(data_pd))