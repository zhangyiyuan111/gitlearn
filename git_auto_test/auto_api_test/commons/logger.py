import logging
import os
import time

import yaml


# 函数，用于日志输出
# 错误日志
def error_log(message):
    LoggerUtil().creat_log().error(message)
    print_log("----------接口请求结束----------\n")
    raise AssertionError(message)

# 打印日志
def print_log(message):
    LoggerUtil().creat_log().info(message)


class LoggerUtil:
    def get_path(self):
        return os.getcwd().split("commons")[0]

    def read_config(self, one_key, two_key):
        f = open(self.get_path() + "/config.yaml", mode="r", encoding="utf-8")
        result = yaml.load(stream=f, Loader=yaml.FullLoader)
        f.close()
        return result[one_key][two_key]

    def creat_log(self):
        # 创建日志对象
        self.loger = logging.getLogger(name="log")
        # 设置全局日志级别(debug<info<warning<error<critical)
        self.loger.setLevel(level=logging.DEBUG)

        if not self.loger.handlers:
            ############################文件日志###################################
            # 文件日志的名称规范
            log_file_path = self.get_path() + "/logs/" + self.read_config("log", "log_file_name") + str(
                int(time.time())) + ".log"

            # 创建文件控制器
            file_Handler = logging.FileHandler(log_file_path, encoding="utf-8")

            # 设置级别
            file_log_level = self.read_config("log", "log_level")
            if file_log_level == "debug":
                file_Handler.setLevel(logging.DEBUG)
            elif file_log_level == "info":
                file_Handler.setLevel(logging.INFO)
            elif file_log_level == "warning":
                file_Handler.setLevel(logging.WARNING)
            elif file_log_level == "error":
                file_Handler.setLevel(logging.ERROR)
            elif file_log_level == "critical":
                file_Handler.setLevel(logging.CRITICAL)

            # 设置文件日志格式
            file_Handler.setFormatter(logging.Formatter(self.read_config("log", "log_format")))
            self.loger.addHandler(file_Handler)
            ################################控制台日志###################################
            console_Handler = logging.StreamHandler()

            # 设置级别
            console_log_level = self.read_config("log", "log_level")
            if file_log_level == "debug":
                file_Handler.setLevel(logging.DEBUG)
            elif file_log_level == "info":
                file_Handler.setLevel(logging.INFO)
            elif file_log_level == "warning":
                file_Handler.setLevel(logging.WARNING)
            elif file_log_level == "error":
                file_Handler.setLevel(logging.ERROR)
            elif file_log_level == "critical":
                file_Handler.setLevel(logging.CRITICAL)
            console_Handler.setFormatter(logging.Formatter(self.read_config("log", "log_format")))
            self.loger.addHandler(console_Handler)

        return self.loger



