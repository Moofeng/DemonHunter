from config import BANNER
# from lib.core.log import logger
from lib.core.module import get_modules
from importlib import import_module
from lib.core.threads import run_threads


package = "pocs"
modules = get_modules(package)
module = "test"
module = import_module("." + module, package)
verify = getattr(module, "verify")
run_threads(10, verify)


'''
# 将包下的所有模块，逐个导入，并调用其中的函数
for module in modules:
    module = import_module("." + module, package)
    verify = getattr(module, "verify")
    verify()
'''
