import os
import sys
from scrapy.cmdline import execute

path = r'E:\pycharmprojects\class_python\Python001-class01\week01\maoyanmovie\maoyanmovie\spiders'
base_dir = os.path.dirname(os.path.abspath(path))  # 项目根目录
sys.path.append(base_dir)  # 加入环境变量
os.chdir(base_dir)  # 切换工作目录
execute(['scrapy', 'crawl', 'maoyan'])