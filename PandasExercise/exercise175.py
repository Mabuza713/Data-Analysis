import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    outputDataFrame = pd.merge(person, address, how = "inner", on = "personId")
    outputDataFrame = outputDataFrame["firstName", "lastName", "city", "state"]