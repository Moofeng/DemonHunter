import random
import hashlib


def random_md5():
    string = "abcdefghijklmnopqrstuvwxyz"
    random_string = "".join([random.choice(string) for _ in range(5)])
    md5 = hashlib.md5()
    md5.update(f"{random_string}".encode())
    random_md5 = md5.hexdigest()
    return (random_string, random_md5)
