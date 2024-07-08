import pandas as pd

# dont need to create data, kinda trivial
def delete_duplicate_emails(person: pd.DataFrame):
    person.sort_values(by='id', inplace=True)
    person.drop_duplicates(subset='email', keep='first', inplace=True)
    