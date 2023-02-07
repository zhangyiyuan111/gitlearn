import hashlib
import os
import random
import string

import yaml

from commons.yaml_unit import get_object_path


class debug_talk:


    def get_random(self,min,max):
        a = random.randint(int(min),int(max))
        return str(a)

    def read_extract(self,key):
        with open(get_object_path() + "/extract.yaml", "r", encoding="utf-8") as f:
            res = yaml.load(stream=f, Loader=yaml.FullLoader)
            return res[key]

    def get_8_random_str(self):
        str_8 = ''
        for i in range(8):
            str_8 = str_8 + random.choice(string.ascii_lowercase)
        return str_8

    def md5_jm(self,date):
        utf8_str = str(date).encode("utf-8")
        md5_str = hashlib.md5(utf8_str).hexdigest()
        return md5_str

    def read_config_yaml(self,key):
        with open(os.getcwd() + "/config.yaml" , "r", encoding="utf-8") as f:
            res = yaml.load(stream=f, Loader=yaml.FullLoader)
            return res[key]

    def int_api(self,date:str):
        if date.isdecimal():
            return int(date)
        else:
            return date