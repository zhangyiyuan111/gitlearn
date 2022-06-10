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

    @pytest.mark.parametrize("caseinfo",parametrize_ddt("/testcases/user_manager/test_token.yaml"))
    def test_get_token(self,caseinfo):
        RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)


    @pytest.mark.parametrize("caseinfo",parametrize_ddt("/testcases/user_manager/edit_flag.yaml"))
    def test_edit_flag(self,caseinfo):
        RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)
    #
    # @pytest.mark.parametrize("caseinfo", parametrize_ddt("/testcases/user_manager/select_flag.yaml"))
    # def test_select_flag(self,caseinfo):
    #     RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)
    #
    # @pytest.mark.parametrize("caseinfo", parametrize_ddt("/testcases/user_manager/del_flag.yaml"))
    # def test_del_flag(self,caseinfo):
    #     RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)
    #
    # @pytest.mark.parametrize("caseinfo", parametrize_ddt("/testcases/user_manager/file_upload.yaml"))
    # def test_file_upload(self,caseinfo):
    #     RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)

    # @pytest.mark.parametrize("caseinfo", parametrize_ddt("/testcases/user_manager/rand_get.yaml"))
    # def test_rand_get(self, caseinfo):
    #     RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)
    #
    # @pytest.mark.parametrize("caseinfo", parametrize_ddt("/testcases/user_manager/md5_login.yaml"))
    # def test_md5_login(self,caseinfo):
    #     RequestUtil(debug_talk()).standard_yaml_testcase(caseinfo)

