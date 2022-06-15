import random
import re
import pytest
import requests
from commons import yaml_unit
from commons.ddt_units import parametrize_ddt
from commons.request_unit import RequestUtil
from commons.yaml_unit import write_yaml, clear_yaml, read_yaml, read_yaml_key, get_object_path
from hotload.debug_talk import debug_talk

class Test_api:

    @pytest.mark.parametrize("caseinfo",parametrize_ddt("testcases/test_router_api/t1rand_get.yaml"))
    def test_t1rand_get(self,caseinfo):
        RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)
   
    @pytest.mark.parametrize("caseinfo",parametrize_ddt("testcases/test_router_api/t2md5_login.yaml"))
    def test_t2md5_login(self,caseinfo):
        RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)
   
    @pytest.mark.parametrize("caseinfo",parametrize_ddt("testcases/test_router_api/t3get_login_info.yaml"))
    def test_t3get_login_info(self,caseinfo):
        RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)

    @pytest.mark.parametrize("caseinfo",parametrize_ddt("testcases/test_router_api/t4get_login_status.yaml"))
    def test_t4get_login_status(self,caseinfo):
        RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)

    @pytest.mark.parametrize("caseinfo",parametrize_ddt("testcases/test_router_api/t4set_login_info.yaml"))
    def test_t4set_login_info(self,caseinfo):
        RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)

    @pytest.mark.parametrize("caseinfo",parametrize_ddt("testcases/test_router_api/t5get_retrytimes_and_time.yaml"))
    def test_t5get_retrytimes_and_time(self,caseinfo):
        RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)

