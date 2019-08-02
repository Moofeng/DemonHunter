import uuid
import logging

from config import ROOT_PATH, SYSTEM

# 传入参数
loglevel = "info"
random_string = uuid.uuid4().hex
filename = f"{ROOT_PATH}/data/logs/{random_string}" if "Linux" in SYSTEM else f"{ROOT_PATH}\\data\\logs\\{random_string}"
numeric_level = getattr(logging, loglevel.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError(f'Invalid log level: {loglevel}')

logger = logging.getLogger("HunterLog") 
logger.setLevel(numeric_level)
formatter = logging.Formatter(
    '[%(levelname)s] %(asctime)s  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

# 使用FileHandler输出到文件
fh = logging.FileHandler(filename)
fh.setLevel(numeric_level)
fh.setFormatter(formatter)

# 使用StreamHandler输出到屏幕
ch = logging.StreamHandler()
ch.setLevel(numeric_level)
ch.setFormatter(formatter)

# 添加两个Handler
logger.addHandler(ch)
logger.addHandler(fh)