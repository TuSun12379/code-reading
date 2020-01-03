# argparse 是python用于解析命令行参数和选项的标准模块
"""
使用步骤：
1.import argparse # 导入模块
2.parser = argparse.ArgumentParser() # 创建一个解析对象
3.parser.add_argumen() # 向对象中添加你要关注的命令行参数和选项，每一个add_argument方法对一个你要关注的参数或选项
4.parser.parser.parse_args() #最后调用parse_args()方法进行解析

ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], 
formatter_class=argpaser.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None,
argument_default=None, conflict_handler='error', add_help=True)

add_argument(name of flags...[,action][,nargs][,const][,default][,type][,choices][,required]
[,help][,metavar][,dest])

name or flags:命令行参数或者选项，其中命令行参数如果没有给定，且没有设置defualt，则出错。但是如果是
选项的话，则设置为None.

nargs:命令行参数的个数，一般使用通配符表示，其中“?”表示只用一个，'*'表示0到多个，'+'表示至少一个

default: 默认值

type: 参数的类型，默认string类型，还有float、int等类型。


"""