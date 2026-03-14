import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    if len(employee.salary.drop_duplicates()) < 2:
        res = None
    else:
        # iloc[1] выбирает второй элемент после сортировки DESC
        res = employee.salary.drop_duplicates().sort_values(ascending=False).iloc[1]
    
    # 3. ВСЕГДА возвращаем DataFrame, даже если результат None
    return pd.DataFrame({'SecondHighestSalary': [res]})