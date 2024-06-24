import pandas as pd
import numpy as np

employee = {
    'id': [ 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'name': [ 'Jane', 'Doe', 'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'salary': [ 80000, 90000, 60000, 75000, 85000, 65000, 70000, 70000, 80000],
    'departmentId': [1, 1, 1, 2, 2, 2, 3, 3, 3, 3]
}

employee = pd.DataFrame(employee)

# Create the Department DataFrame
department = {
    'id': [1, 2, 3],
    'name': ['HR', 'Engineering', 'Marketing']
}
department = pd.DataFrame(department)
def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    if len(employee) == 0 or len(department)==0:
        return pd.DataFrame({"Department":[], "Employee":[], "Salary":[]})
    dataFrame = pd.DataFrame({"id": [] ,
                              "name": [] , 
                              "salary": [] ,
                              "departmentId": []})
    for id in department.id:
        tempFrame = employee[employee["departmentId"] == id]
        tempFrame.sort_values("salary")
        n = 3
        if len(tempFrame.nlargest(n, "salary", keep = "all")["salary"].tolist()) < 3:
            n = len(tempFrame.nlargest(n, "salary", keep = "all")["salary"].tolist())
        else:
            while (len(set(tempFrame.nlargest(n, "salary", keep = "all")["salary"].tolist())) != 3):
                n += 1

        print(tempFrame.nlargest(n, "salary", keep = "all")["salary"].tolist())
        tempFrame = tempFrame.nlargest(n, "salary", keep = "all")
        dataFrame = pd.concat([dataFrame, tempFrame])
    
    dataFrame = pd.merge(dataFrame, department, left_on="departmentId" , right_on="id")
    
    result = dataFrame.drop(columns = ["id_x", "departmentId", "id_y"])
    result.rename(columns={"name_x":"Employee", "salary":"Salary", "name_y":"Department"},inplace= True)
    result = result.loc[:,["Department", "Employee","Salary"]]
    
    return(result)
    
    
print(top_three_salaries(employee, department))