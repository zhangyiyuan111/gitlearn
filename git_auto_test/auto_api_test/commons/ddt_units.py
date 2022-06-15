import json

from commons.logger import print_log, error_log
from commons.yaml_unit import read_yaml

#将列表字典经过替换成为新的列表字典
def parametrize_ddt(path):
    try:
        data = read_yaml(path)
        data_json =data[0]
        if "parametrize" in data[0].keys():
            data_parametrize = data[0]["parametrize"]
            # print(data_parametrize)
            if data_parametrize:
                for i in range(len(data_parametrize)):
                    if i:
                        if len(data_parametrize[i]) != len(data_parametrize[0]):
                            print_log("第{}行长度有误".format(i+1))
                            continue
                new_caseinfo = []
                #从第二行开始循环
                for i in range(1,len(data_parametrize)):
                    str_data = json.dumps(data_json)
                    for j in range(len(data_parametrize[0])):
                        if str_data.count("$ddt{") >0:
                            str_data = str_data.replace("$ddt{"+data_parametrize[0][j]+"}",str(data_parametrize[i][j]))
                        else:
                            continue
                    new_caseinfo.append(json.loads(str_data))
                return new_caseinfo
        else:
            return data
    except Exception as e:
        error_log("读取测试用例yaml文件失败{}".format(e))
        raise e