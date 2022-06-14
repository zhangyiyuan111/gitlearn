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

   @pytest.mark.parametrize("caseinfo",parametrize_ddt("testcases/test_phpwind/test_index.yaml"))
   def test_index(self,caseinfo):
       RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)

   @pytest.mark.parametrize("caseinfo",parametrize_ddt("testcases/test_phpwind/test_login.yaml"))
   def test_login(self,caseinfo):
       RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)

