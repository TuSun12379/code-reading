import os 
import pandas as pd
import numpy as np
# print(os.getcwd())

def get_file_in_dir(ext, drc): # 定义get_file_in_dir()函数，ext传入参数为文件后缀
    for files in os.listdir(drc): # os.listdir()用于获取当前目录文件列表, 包含文件名，小点和后缀的完整信息
        if files.endswith(ext): # 限定当文件以.hkl结尾
            yield files # 将文件当前路径和.hkl文件结合组成完整路径。

def load_hkl_files(fns = []):
    dfn1 = pd.read_table(fns[0], sep = '\s* ',index_col = [0, 1, 2], engine = 'python', header = None, names="h k l val sigma".split())
    dfn1.index = pd.Index(dfn1.index) # 这里index的作用是其会根据指定的index_col将前三列即hkl组成一个元组
    dfn1["frame"] = 0
    dfx = dfn1 # 将第一个dataframe赋值给dfx, dfx用于合并所有的dataframe
    for i, fn in enumerate(fns):
        dfn = pd.read_table(fn, sep = '\s* ',index_col = [0, 1, 2], engine = 'python', header = None, names="h k l val sigma".split())
        dfn["frame"] = i
        """参数分别为fn:文件名，sep:分隔符号，index_col:用作结果中行索引的列号或列名，header:用作列名的行号，默认是0，如果没有列名就应该为None
            names:结果的列名列表，和header=None一起使用            
        """  
        if i == 0:  # 因为第一个frame数据已经添加，所以之后从第二个开始添加
            continue 
        else:
            dfx.append(dfn)
        dfn.index = pd.Index(dfn.index)
        dfx = dfx.append(dfn)
    return dfx

def serialmerge(df, kind = 'mean', key = 'val'):
    if kind == "max":
        merged = df.groupby(df.index).max() # 这里会根据相同的hkl对应的其他项的最大值，平均值或其他形式合并，除去重复项
        # print(merged)
    elif kind == "mean":
        merged = df.groupby(df.index).mean()
        # print(merged)
    else:
        raise ValueError("serialmerge - kind =", kind)
    merged["Nobs"] = df.groupby(df.index).size() # 这里添加的一列是得到同一hkl对应的数目
    refs = df.index.drop_duplicates() # 除去hkl之外的其它项，得到非 重复hkl组成的列表类似结构
    # print(refs.size) 
    C = np.eye(refs.size, dtype=np.float32) # refs.size即非重复hkl的数目1495, np.eye()用于创建对角矩阵
    # print(C)
    # print(df.groupby("frame"))
    for frame, subdf in df.groupby("frame"): # 以frame数目作为分组的标准
        subdf = subdf.groupby(subdf.index)[key].first() 
        print(subdf)

def merge_entry():
    fns = []
    fn = os.getcwd() # 获取目前路径
    if os.path.isdir(fn): # 判断当前目录是否为目录
        fns.extend(list(get_file_in_dir(".hkl", drc = fn))) # 通过自定义函数获取包含文件名的路径，然后转换成列表，通过extend()函数添加到列表。

    dfx = load_hkl_files(fns) 
    print("reflections:", len(dfx)) # 打印衍射点数目, 这里指的是所有文件中衍射点数目的简单加和
    print("unique reflections:", len(dfx.groupby(dfx.index))) # 打印非重复的衍射点数目
    print("nframes:", max(dfx["frame"]+1)) # 打印记录的frame，即文件数目 
    # serialmerge(dfx,'mean')

    # print(len(dfx))
    # print(len(dfx))
    # print(len(dfx))
    # key = fns[0]
    # print(key)
    # dfn = pd.read_table(fns[0], sep = '\s* ', engine = 'python', header = None, names="h k l val sigma".split())
    # print(len(dfx))

if __name__ == '__main__':
    merge_entry()

