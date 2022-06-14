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

   @pytest.mark.parametrize("caseinfo",parametrize_ddt("testcases/test_router_api/get_login_info.yaml"))
   def get_login_info(self,caseinfo):
       RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)

   @pytest.mark.parametrize("caseinfo",parametrize_ddt("testcases/test_router_api/get_login_status.yaml"))
   def get_login_status(self,caseinfo):
       RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)

   @pytest.mark.parametrize("caseinfo",parametrize_ddt("testcases/test_router_api/get_retrytimes_and_time.yaml"))
   def get_retrytimes_and_time(self,caseinfo):
       RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)

   @pytest.mark.parametrize("caseinfo",parametrize_ddt("testcases/test_router_api/md5_login.yaml"))
   def md5_login(self,caseinfo):
       RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)

   @pytest.mark.parametrize("caseinfo",parametrize_ddt("testcases/test_router_api/rand_get.yaml"))
   def rand_get(self,caseinfo):
       RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)

   @pytest.mark.parametrize("caseinfo",parametrize_ddt("testcases/test_router_api/set_login_info.yaml"))
   def set_login_info(self,caseinfo):
       RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)

