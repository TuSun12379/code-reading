import os 
import pandas as pd
# print(os.getcwd())

def get_file_in_dir(ext, drc): # 定义get_file_in_dir()函数，ext传入参数为文件后缀
    for files in os.listdir(drc): # os.listdir()用于获取当前目录文件列表, 包含文件名，小点和后缀的完整信息
        # print(files)
        if files.endswith(ext): # 限定当文件以.hkl结尾
            yield os.path.join(drc, files) # 将文件当前路径和.hkl文件结合组成完整路径。

def load_hkl_files(fns = []):
    for i, fn in enumerate(fns):
        dfn = pd.read_table(fn, sep = '\s*', engine = 'python', index_col=[0,1,2], header=None, names="h k l val sigma".split())
        """参数分别为fn:文件名，sep:分隔符号，index_col:用作结果中行索引的列号或列名，header:用作列名的行号，默认是0，如果没有列名就应该为None
            names:结果的列名列表，和header=None一起使用            
        """
        dfn.index = pd.Index(dfn.index)     
        dfn["frame"] = i
        dfx = dfx.append(dfn)
        return dfx

def merge_entry():
    fns = []
    fn = os.getcwd() # 获取目前路径
    if os.path.isdir(fn): # 判断当前目录是否为目录
        fns.extend(list(get_file_in_dir(".hkl", drc = fn))) # 通过自定义函数获取包含文件名的路径，然后转换成列表，通过extend()函数添加到列表。
    print(fns)
    # dfx = load_hkl_files(fns)
    # print(len(dfx))

if __name__ == '__main__':
    merge_entry()

    