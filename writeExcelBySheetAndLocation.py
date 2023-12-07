import pandas as pd
import numpy as np

# 讀取 input, output 保留 output 原本的欄位資料 把 input 的資料從 B2 蓋過去, input 和 output 的欄位數並不相同，
# 讀取 input 檔案 header=None: 將標題視為數據讀進來
# input_df = pd.read_excel(r'D:\somewhere\input.xlsx', sheet_name='Sheet1', header=None)
input_df = pd.read_excel(r'D:\somewhere\input.xlsx', header=None)

# 選取第2列起的所有資料
data_to_copy = input_df.iloc[1:, :]
print(data_to_copy.shape)
print(data_to_copy)

# 讀取 output 檔案
# output_df = pd.read_excel(r'D:\somewhere\output.xlsx', sheet_name='Sheet1')
output_df = pd.read_excel(r'D:\somewhere\output.xlsx', header=None)
print(output_df.shape)
print(output_df)

# # 將資料貼到指定位置
# 這個方式必須要 input 和 output 的位置大小一致
# output_df.iloc[2:2+data_to_copy.shape[0], 1:] = data_to_copy.values
# 將資料蓋過指定位置，不管行數是否一致
# 取 input 和 output 中水平方向和垂直方向的最大值，填入空白值
# 計算起始位置的偏移
x_offset_input = 1  # B列的位置 1
y_offset_input = 2  # 3列的位置 2

x_offset_output = 0  # A列的位置
y_offset_output = 0  # 1列的位置

# 取 input 和 output 中水平方向和垂直方向的最大值，值都是空白
max_shape = (max(data_to_copy.shape[0] + y_offset_input, output_df.shape[0] + y_offset_output), 
             max(data_to_copy.shape[1] + x_offset_input, output_df.shape[1] + x_offset_output))

max_values = np.full(max_shape, np.nan, dtype=object)

# 填入 output 的值，從 A1 開始
max_values[y_offset_output:output_df.shape[0] + y_offset_output, x_offset_output:output_df.shape[1] + x_offset_output] = output_df.values

# 將 input 的值蓋上去，從 B3 開始
max_values[y_offset_input:y_offset_input + data_to_copy.shape[0], x_offset_input:x_offset_input + data_to_copy.shape[1]] = data_to_copy.values

# 轉為 DataFrame
result_df = pd.DataFrame(max_values)

# 儲存修改後的 output 檔案
# output_df.to_excel(r'D:\somewhere\output.xlsx', sheet_name='Sheet1', index=False)
result_df.to_excel(r'D:\somewhere\output.xlsx', index=False, header=False)
