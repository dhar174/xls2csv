import pandas as pd
import os





data_xls = pd.read_excel(os.getcwd()+'/Cases_and_Deaths_by_County_2020-07-07_695787_7.xlsx', index_col=None)
data_xls.to_csv('csvfile.csv', encoding='utf-8', index=False)
