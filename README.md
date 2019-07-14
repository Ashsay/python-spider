1.route config
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

2.install tesseract & tesserocr
安装tresseract  设置变量   设置变量TESSDATA_PREFIX  目标文件 tessdata
tesserocr-2.4.0-cp37-cp37m-win32.whl  pip安装
将tessdata放入python目录下