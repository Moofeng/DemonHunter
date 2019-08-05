from config import BANNER
from lib.core.log import logger
from lib.core.module import get_modules 
from importlib import import_module


package = "pocs"
modules = get_modules(package)

# 将包下的所有模块，逐个导入，并调用其中的函数
for module in modules:
    module = import_module("." + module, package)
    verify = getattr(module, "verify")
    verify()