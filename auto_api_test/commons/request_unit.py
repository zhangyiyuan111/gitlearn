import json
import re

import jsonpath
import requests

from commons.assert_units import assert_result
from commons.logger import print_log, error_log
from commons.replace_unit import replace_all
from commons.yaml_unit import write_yaml, read_yaml_key
from hotload.debug_talk import debug_talk


class RequestUtil:

    def __init__(self,obj):
        self.obj = obj

    sess = requests.session()
    #发送请求封装
    def send_all_request(self,method,url,base_url,**kwargs):
        try:
            #method统一小写
            method = str(method).lower()
            print_log("接口请求方式{}".format(method))
            #url进行替换
            url = self.replace_get_value(base_url+url)
            print_log("接口请求路径{}".format(url))
            # params、json、data、headers进行替换
            for key,value in kwargs.items():
                if key in ["headers","params","data","json"]:
                    kwargs[key] = self.replace_get_value(value)
                    print_log("接口请求参数{}".format({key:kwargs[key]}))
                elif key =="files":
                    for file_key,file_value in value.items():
                        value[file_key] = open(file_value,"rb")
            return RequestUtil.sess.request(method,url,**kwargs)
        except Exception as e:
            error_log("发送请求报错{}".format(e))
            raise e
    try:
        #统一接口请求封装
        def standard_yaml_testcase(self,caseinfo):
            print_log("----------接口测试开始-----------")
            caseinfo_keys = caseinfo.keys()
            if "name" in caseinfo_keys and "request" in caseinfo_keys and "validate" in caseinfo_keys:
                print_log(caseinfo["name"])
                request_keys = caseinfo["request"].keys()
                if "method" in request_keys and "url" in request_keys and "base_url" in request_keys:
                    method =caseinfo["request"].pop("method")
                    base_url = caseinfo["request"].pop("base_url")
                    url = caseinfo["request"].pop("url")
                    res = self.send_all_request(method=method,url=url,base_url=base_url,**caseinfo["request"])
                    text_result =res.text
                    # print(text_result)
                    try:
                        json_result = res.json()
                    except:
                        print_log("返回结果不是json格式")
                    #提取接口关联的值
                    if "extract" in caseinfo_keys :
                        for key,value in caseinfo["extract"].items():
                            if "(.*?)" in value or "(.+?)" in value:
                                re_value = re.search(value,text_result)    #正则仅仅支持文本格式
                                if re_value:
                                    re_value = re_value.group(1)
                                    data ={key:re_value}
                                    write_yaml("extract.yaml",data)
                                else:
                                    print_log("extract正则写法有误或者没有提取到值")
                            else:
                                js_value = jsonpath.jsonpath(json_result,value)         #json仅仅支持json格式数据
                                if js_value:
                                    data = {key:js_value[0]}
                                    write_yaml("extract.yaml",data)
                                else:
                                    print_log("json写法有误或者没有提取到值")
                    #断言
                    want_result = caseinfo["validate"]  #预期结果
                    print_log("预期结果{}".format(want_result))
                    real_result = json_result           #实际结果
                    print_log("实际结果{}".format(real_result))
                    flag = assert_result(want_result,real_result)
                    if flag ==0:
                        print_log("----------接口请求结束----------\n")
                        error_log("接口请求失败")
                    else:
                        print_log("接口请求成功")
                    print_log("----------接口请求结束----------\n")
                else:
                    print_log("----------接口请求结束----------\n")
                    error_log("request下必须包含关键字：method、url、base_url")
            else:
                print_log("----------接口请求结束----------\n")
                error_log("yaml用力必须包含一级关键字：name、request、validate")
    except Exception as e:
        error_log("规范yaml测试用例报错{}".format(e))
        raise e

    #替换取值封装
    #可能的值：json、url、params、data、headers
    #各种数据的切换：float、int、str、list、dict
    def replace_get_value(self,data):
        try:
            if data:
                #保存传入数据类型
                data_type = type(data)
                #把不同类型转换成为字符串
                if isinstance(data,list) or isinstance(data,dict):
                    str_data = json.dumps(data)
                else:
                    str_data = str(data)
                #实际数据替换字符串中的表达式
                str_data = replace_all(str_data)
                # cnt = str_data.count("${")
                # for i in range(cnt):
                #     if "${" in str_data and "}" in str_data:
                #         start_index = str_data.index("${")
                #         end_index = str_data.index("}", start_index)
                #         old_value = str_data[start_index:end_index + 1]
                #         function_name = old_value[2:old_value.index("(")]
                #         function_value = old_value[old_value.index("(")+1:old_value.index(")")]
                #         if function_value != '':
                #             function_value = function_value.split(",")
                #             new_value = getattr(self.obj, function_name)(*function_value)
                #         else:
                #             new_value = getattr(self.obj,function_name)()
                #         new_data = str_data.replace(old_value, new_value)
                #         str_data = new_data
                #字符串转换回去
                #json和list转回
                if isinstance(data,list) or isinstance(data,dict):
                    data = json.loads(str_data)
                #字符串转回
                else:
                    data = data_type(str_data)
            else:
                print_log("None不需要进行取值")
            return data
        except Exception as e:
            error_log("热加载报错{}".format(e))
            raise e






