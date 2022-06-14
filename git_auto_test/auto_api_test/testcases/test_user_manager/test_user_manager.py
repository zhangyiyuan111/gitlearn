import random
import re
import pytest
import requests
import allure
from commons import yaml_unit
from commons.ddt_units import parametrize_ddt
from commons.request_unit import RequestUtil
from commons.yaml_unit import write_yaml, clear_yaml, read_yaml, read_yaml_key, get_object_path
from hotload.debug_talk import debug_talk

@allure.epic("")
@allure.feature("")
class Test_api:

   @pytest.mark.parametrize("caseinfo",parametrize_ddt("testcases/test_user_manager/del_flag.yaml"))
   def del_flag(self,caseinfo):
       RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)

   @pytest.mark.parametrize("caseinfo",parametrize_ddt("testcases/test_user_manager/edit_flag.yaml"))
   def edit_flag(self,caseinfo):
       RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)

   @pytest.mark.parametrize("caseinfo",parametrize_ddt("testcases/test_user_manager/file_upload.yaml"))
   def file_upload(self,caseinfo):
       RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)

   @pytest.mark.parametrize("caseinfo",parametrize_ddt("testcases/test_user_manager/select_flag.yaml"))
   def select_flag(self,caseinfo):
       RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)

   @pytest.mark.parametrize("caseinfo",parametrize_ddt("testcases/test_user_manager/test_token.yaml"))
   def test_token(self,caseinfo):
       RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)

