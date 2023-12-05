import numpy as np
import pandas as pd

# 原始的 pivot table 資料
dfWithCols = {
    'Cat1': [1, 2, 3, 4, 5],
    'Cat2': [6, 7, 8, 9, 10],
    'Cat3': [11, 12, 13, 14, 15],
    'Cat4': [0, 0, 0, 0, 0],
    '總計': [16, 17, 18, 0, 19]
}

index = ['Type1', 'Type2', 'Type3', 'Type4', '總計']
columns = ['Cat1', 'Cat2', 'Cat3', 'Cat4', '總計']
columnsOutput = ['Cat1', 'Cat2', 'Cat3', '遺漏值', '總計']
indexCols = ['Types','Cats']
types = ['計數','欄百分比']
indexLv = len(indexCols)
indexSpace = indexLv + 1
countTypes = len(types)
fillV = "-"
outputCol = indexCols + columns
print(outputCol)


pivot_table = pd.DataFrame(dfWithCols, index=index, columns=columns)
# print(pivot_table.shape)
# print(pivot_table)
pivot_table.to_excel('T7count.xlsx')

# 避免除以零的情況
total_column = pivot_table[columns[-1]]
total_column[total_column == 0] = np.nan  # 將總計為零的地方設置為 NaN
percent_table = pivot_table.div(total_column, axis=0) * 100
percent_table.to_excel('T7percent.xlsx')

# 處理百分比為 NaN 的情況，可以設置為特定的值，例如 0
percent_table = percent_table.fillna(fillV)


# 逐列輸出，同時計算百分比 sn, index level1, index level 2
result_array = np.empty((pivot_table.shape[0] * countTypes, pivot_table.shape[1] + (indexLv+1)), dtype=object)

# 留 level 2 index: index 和 計數/欄百分比
result_array[::indexLv, indexSpace:] = pivot_table.values
result_array[1::indexLv, indexSpace:] = percent_table.values
# print(result_array)

# 添加整數行的 index
result_array[:, 0] = np.arange(result_array.shape[0])
print(result_array)

# 判斷 result_array[0, 0] 是否為奇數，是的話將對應的第二列設置為 "欄百分比" if then else
# result_array[:, indexLv] = np.where(result_array[::1, 0] % 2 != 0, '欄百分比', '計數')
switch_types = np.array(types)
# Use np.select to apply the switch logic
result_array[:, indexLv] = np.select(
    [result_array[::1, 0] % countTypes == i for i in range(len(switch_types))],
    switch_types
)
print(result_array)
# 整組重複2次 1234512345
# dupIndex = np.tile(index, 2)
# print(dupIndex)

# 1122334455
repIndex = np.repeat(index,countTypes)
result_array[:, 1] = repIndex

# 轉換為 DataFrame，指定 index 和 columns
outputCol = indexCols + columnsOutput
result_array = result_array[:, 1:]

print(result_array)
print(result_array.shape)

result_df = pd.DataFrame(result_array,columns=outputCol)
result_df.to_excel('T7countPercentIntegrated.xlsx',index=False)

# 顯示結果
print(result_df)
