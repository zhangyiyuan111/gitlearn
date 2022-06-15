import os
def get_cases():
    yaml_testcases = []
    path_file = os.getcwd()
    folders = os.listdir(path_file)
    for file in folders:
        if "yaml" in file:
            yaml_testcases.append(file)
    return yaml_testcases

def load_cases(testpy_name):
    cases_name = get_cases()
    py_name = testpy_name+".py"
    #写入前面模板
    with open(py_name,mode="w",encoding="utf-8") as f:
        f.write("import random\n")
        f.write("import re\n")
        f.write("import pytest\n")
        f.write("import requests\n")
        f.write("from commons import yaml_unit\n")
        f.write("from commons.ddt_units import parametrize_ddt\n")
        f.write("from commons.request_unit import RequestUtil\n")
        f.write("from commons.yaml_unit import write_yaml, clear_yaml, read_yaml, read_yaml_key, get_object_path\n")
        f.write("from hotload.debug_talk import debug_talk\n")
        f.write("\n")
        f.write("class Test_api:\n")
        f.write("\n")

    with open(py_name, mode="a", encoding="utf-8") as f:
        for i in cases_name:
            f.write('    @pytest.mark.parametrize("caseinfo",parametrize_ddt("' + get_base_path() + i + '"))\n')
            f.write('    def '+'test_'+i[:-5]+'(self,caseinfo):\n')
            f.write('        RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)\n')
            f.write('   \n')

def get_base_path():
    path_all = os.getcwd()
    path_fenkai = path_all.split("testcases\\")
    finnal_path = "testcases/" + path_fenkai[1]
    for i in finnal_path:
        if i == "\\":
            finnal_path = finnal_path.replace("\\", "/")
    return finnal_path + '/'

load_cases("test_router_api")

