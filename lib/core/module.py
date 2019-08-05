import os


# 获取包名下所有非__init__的模块名
def get_modules(package="."):
    modules = []
    files = os.listdir(package)
    for file in files:
        if not file.startswith("__"):
            name, _ = os.path.splitext(file)
            modules.append(name)
    return modules