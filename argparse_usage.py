import argparse

"""argparse 是Python内置的一个用于命令项选项与参数解析的模块，
通过在程序中定义好我们需要的参数，argparse将会从sys.argv中解析
出这些参数，并自动生成帮助和使用信息。"""

parser = argparse.ArgumentParser()  # 创建ArgumentParser()对象
parser.add_argument('integer', type = int, help = 'display an integer')  # 掉用add_argument()方法添加参数
args = parser.parse_args()  # 使用功能parse_args()解析添加的参数
print(args.integer)

# PowerShell中运行以上代码
# python argparse_usage.py -h 看看会得到什么结果