import json

import jsonpath

from commons.logger import print_log, error_log


def assert_result(want_result,real_result):
    try:
        flag = 0
        if not want_result:
            error_log("该用例没有写断言")
            return flag
        else:
            if real_result:
                for want in want_result:
                    for key,value in want.items():
                        if key =="equals":
                            flag = equals_assert(want[key],real_result)+flag
                        elif key =="contains":
                            flag = contains_assert(value,real_result)+flag
                        else:
                            print_log("不支持该断言{}".format(want[key]))
                            raise AssertionError
            else:
                print_log("返回值为空，断言失败")
        return flag
    except Exception as e:
        error_log("断言报错:{}".format(e))
        raise e

def equals_assert(value,real_result):
    flag = 0
    for assert_key,assert_value in value.items():
        lists = jsonpath.jsonpath(real_result,"$.."+assert_key)
        print(lists)
        if lists:
            if assert_value in lists:
                print_log(f"相等断言{assert_key}成功")
                flag+=1
            else:
                print_log("相等断言失败，实际结果与预期结果不符合")
                flag = 0
        else:
            error_log("相等断言失败，实际结果里面没有{}".format(assert_key))
            flag = 0
    return flag

def contains_assert(value,real_result):
    flag = 0
    if str(value) in json.dumps(real_result):
        print_log(f"包含断言{value}成功")
        flag+=1
    else:
        error_log(f"包含断言{value}失败")
        flag = 0
    return flag
