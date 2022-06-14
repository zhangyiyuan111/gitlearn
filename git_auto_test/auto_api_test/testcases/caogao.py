import os
path_file_root = os.getcwd()

# 写入前面模板
def load_cases(testpy_name,file_path):
    py_name = file_path+"\\\\"+testpy_name+".py"
    with open(py_name,mode="w",encoding="utf-8") as f:
        f.write("import random\n")
        f.write("import re\n")
        f.write("import pytest\n")
        f.write("import requests\n")
        f.write("import allure\n")
        f.write("from commons import yaml_unit\n")
        f.write("from commons.ddt_units import parametrize_ddt\n")
        f.write("from commons.request_unit import RequestUtil\n")
        f.write("from commons.yaml_unit import write_yaml, clear_yaml, read_yaml, read_yaml_key, get_object_path\n")
        f.write("from hotload.debug_talk import debug_talk\n")
        f.write("\n")
        f.write('@allure.epic("")\n')
        f.write('@allure.feature("")\n')
        f.write("class Test_api:\n")
        f.write("\n")

def get_base_path(path_all):
    path_fenkai = path_all.split("testcases\\")
    finnal_path = "testcases/" + path_fenkai[1]
    for i in finnal_path:
        if i == "\\":
            finnal_path = finnal_path.replace("\\", "/")
    return finnal_path + '/'

#写入内容
def write_cases(testpy_name,file_path,cases_name):
    py_name = file_path+"\\\\"+testpy_name+".py"
    with open(py_name, mode="a", encoding="utf-8") as f:
        f.write('   @pytest.mark.parametrize("caseinfo",parametrize_ddt("' + get_base_path(file_path) + cases_name + '"))\n')
        f.write('   def ' +cases_name[:-5]+'(self,caseinfo):\n')
        f.write('       RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)\n')
        f.write("\n")


def get_cases(path_file_root):
    yaml_testcases = []
    folders = os.listdir(path_file_root)
    current_folder_name = path_file_root.split("\\")
    current_folder_name = current_folder_name[len(current_folder_name)-1]
    for name in folders:
        if name.endswith(".yaml"):
            load_cases(current_folder_name,path_file_root)
            # load_cases(current_folder)
    for name in folders:
        if os.path.isdir(os.path.join(path_file_root,name)) and "test_" == name[:5]:
            get_cases(os.path.join(path_file_root,name))
        elif name.endswith(".yaml"):
            write_cases(current_folder_name,path_file_root,name)
            yaml_testcases.append(name)

get_cases(path_file_root)




    # with open(py_name, mode="a", encoding="utf-8") as f:
    #     for i in cases_name:
    #         f.write('   @pytest.mark.parametrize("caseinfo",parametrize_ddt("' + get_base_path() + i + '"))\n')
    #         f.write('   def test_get_token(self,caseinfo):\n')
    #         f.write('       RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)\n')




