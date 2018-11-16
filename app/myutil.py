import uuid
import hashlib
import random


def get_unique_str():
    uuid_str = str(uuid.uuid4()).encode('utf-8')
    # 实例化MD5
    md5 = hashlib.md5()
    # 加密
    md5.update(uuid_str)
    # 返回32位16进制数据
    return md5.hexdigest()
def get_random_color():

    r = random.randint(0,256)
    g = random.randint(0,256)
    b = random.randint(0,256)

    return (r,g,b)











