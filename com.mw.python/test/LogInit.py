# encoding:utf-8
from pip.utils import logging


def initlog():
    # 配置日志信息
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s] [%(levelname)s] %(message)s',
                        datefmt='%y-%m-%d %H:%M:%S',
                        filename='feedservice.log',
                        filemode='a')
    # 定义一个Handler打印INFO及以上级别的日志到sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # 设置日志打印格式
    formatter = logging.Formatter('%(levelname)s %(message)s')
    console.setFormatter(formatter)
    # 将定义好的console日志handler添加到root logger
    logging.getLogger('').addHandler(console)

initlog()