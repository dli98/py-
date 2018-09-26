# 程序文件入口 开始文件
import os
import sys
sys.path.append(os.path.dirname(os.getcwd()))

from core.schedule import Schedule

if __name__ == '__main__':
    s = Schedule()
    s.run()