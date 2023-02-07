from commons.logger import error_log
from hotload.debug_talk import debug_talk


def get_end_index(date):
    cont_start = 0
    cont_end = 0
    for i,j in enumerate(date):
        if date[i] =="(":
            cont_start = cont_start+1
        if date[i] ==")":
            cont_end =cont_end+1
        if cont_end>0 and cont_start==cont_end:
            return i

def get_end_index_da(date):
    cont_start = 0
    cont_end = 0
    for i,j in enumerate(date):
        if date[i:i+2] =="${":
            cont_start = cont_start+1
        if date[i] =="}":
            cont_end =cont_end+1
        if cont_end>0 and cont_start==cont_end:
            return i


def get_times(date):
    cont_start = 0
    cont_end = 0
    time_appear =0
    for i, j in enumerate(date):
        if date[i:i + 2] == "${":
            cont_start = cont_start + 1
        if date[i] == "}":
            cont_end = cont_end + 1
        if cont_start > 0 and cont_start == cont_end:
            time_appear = time_appear+1
    return time_appear

def digui(date):
    try:
        if  "${" in date and "}" in date:
            result = ""
            start_index = date.index("(")
            end_index = get_end_index(date=date)
            fun_name_find = date[date.index("${")+2:start_index]
            fun_value = date[start_index + 1:end_index]
            fun_value_name = date[date.index("${"):get_end_index_da(date)+1]
            if fun_value == "":
                mid = getattr(debug_talk(), fun_name_find)()
                result = date.replace(fun_value_name, mid)
            elif "${" in fun_value:
                fun_value = digui(fun_value)
                fun_value = fun_value.split(",")

                mid = getattr(debug_talk(), fun_name_find)(*fun_value)
                result = date.replace(fun_value_name, mid)
            else:
                fun_value = fun_value.split(",")
                mid = getattr(debug_talk(), fun_name_find)(*fun_value)
                result = date.replace(fun_value_name, mid)
            return result
        else:
            return date
    except Exception as e:
        error_log("递归替换报错:{}".format(e))
        raise e


def replace_all(date):
    #循环次数
    try:
        for_times = get_times(date)
        #循环获取替换后的值
        for i in range(for_times):
            date = digui(date)
        return date
    except Exception as e:
        error_log("热加载替换用例报错:{}".format(e))
        raise e


