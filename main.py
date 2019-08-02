import random
import hashlib


random_string = "".join([random.choice("abcdefghijk") for _ in range(5)])
md5 = hashlib.md5()
print(random_string)
md5.update(f"{random_string}".encode("utf-8"))
print(md5.hexdigest())