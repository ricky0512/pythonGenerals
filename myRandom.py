# 如果存成 random.py 就跑不動啦 # 和 module 同名
# 亂數, 隨機
import random

rann = random.randint(0, 19)
print(rann)
rann = random.randrange(0, 19, 2)
print(rann)
rann = random.uniform(1.5, 1.9)
print(rann)
rann = round(random.uniform(1.5, 1.9), 1)
print(rann)
