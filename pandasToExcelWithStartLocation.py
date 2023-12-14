# much simple and clear then writeExcelBySheetAndLocation.py
# 從 「資料表」工作表的C2 開始輸出
import pandas as pd 
import numpy as np


data = {'a': [1,np.nan],'b': [3,4]}
df = pd.DataFrame(data)
df.to_excel('output.xlsx',sheet_name='資料表',startrow=1,startcol=2)
