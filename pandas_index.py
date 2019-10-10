
import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(12, 24).reshape((3, 4)), index=["a", "b", "c"], columns=["WW", "XX", "YY", "ZZ"])
print(df)

'''

   WW  XX  YY  ZZ

a  12  13  14  15

b  16  17  18  19

c  20  21  22  23

'''

 
# 查看索引 (索引是可以重复的)

print(df.index)  # Index(['a', 'b', 'c'], dtype='object')

# 修改索引

df.index = ["aa", "bb", "cc"]   # []列表的长度必须与df行数一致。
print(df)
'''

    WW  XX  YY  ZZ

aa  12  13  14  15

bb  16  17  18  19

cc  20  21  22  23

'''

# 根据索引重新构建数据

df2 = df.reindex(["aa", "pp"])  # 索引存在就正常显示数据，不存在的索引其数据就是NaN

print(df2)

'''

      WW    XX    YY    ZZ

aa  12.0  13.0  14.0  15.0

pp   NaN   NaN   NaN   NaN

'''

# 将某列设置为索引

df3 = df.set_index("YY")  # 将"YY"列设为索引（默认同时删除"YY"列的数据）

print(df3)

'''

    WW  XX  ZZ

YY

14  12  13  15

18  16  17  19

22  20  21  23

'''

df4 = df.set_index("YY", drop=False)  #  drop=False 表示保留原先"YY"列的数据。(默认为True)

print(df4)

'''

    WW  XX  YY  ZZ

YY

14  12  13  14  15

18  16  17  18  19

22  20  21  22  23

'''

# unique()某列去重后的内容

print(df["ZZ"].unique())  # [15 19 23]  ndarray类型
df.index = ["ll", "ll", "mm"]  # 索引可以重复

# 去重后的索引
print(df.index.unique())  # Index(['ll', 'mm'], dtype='object')

# index索引有长度
print(len(df.index))  # 3

# index索引对象可以转换成列表类型
print(list(df.index))  # ['ll', 'll', 'mm']

 
